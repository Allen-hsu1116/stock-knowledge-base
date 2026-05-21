#!/usr/bin/env python3
"""Stock Knowledge Base Lint Checker — comprehensive health check."""

import os
import re
import json
from pathlib import Path
from collections import defaultdict
from datetime import datetime

KB_ROOT = Path(os.path.expanduser("~/.hermes/workspace/stock-knowledge-base"))
WIKI_DIR = KB_ROOT / "wiki"
RAW_DIR = KB_ROOT / "raw"

# --- Collect all wiki & raw files ---
def collect_files(base_dir, glob_pattern="*.md"):
    files = []
    for root, dirs, filenames in os.walk(base_dir):
        for f in filenames:
            if f.endswith(".md"):
                full_path = Path(root) / f
                rel_path = full_path.relative_to(base_dir)
                files.append((full_path, rel_path))
    return files

wiki_files = collect_files(WIKI_DIR)
raw_files = collect_files(RAW_DIR)

# --- Build wiki slug set (filename without .md, for cross-link matching) ---
wiki_slugs = set()
wiki_by_slug = {}
for full_path, rel_path in wiki_files:
    slug = str(rel_path.with_suffix(""))  # e.g. "技術分析/KD指標隨機指標"
    wiki_slugs.add(slug)
    wiki_by_slug[slug] = full_path

# Also build a mapping of just the basename (without dir) for cross-link resolution
wiki_basenames = {}
for full_path, rel_path in wiki_files:
    basename = rel_path.stem  # filename without .md
    if basename in wiki_basenames:
        wiki_basenames[basename].append(str(rel_path.with_suffix("")))
    else:
        wiki_basenames[basename] = [str(rel_path.with_suffix(""))]

# --- 1. Cross-links check ---
broken_links = defaultdict(list)  # source_file -> [broken_links]
cross_link_pattern = re.compile(r'\[\[([^\]|]+)(?:\|[^\]]+)?\]\]')

# Also need to check standard markdown links to raw/
raw_link_pattern = re.compile(r'\[([^\]]+)\]\(([^)]+)\)')
frontmatter_pattern = re.compile(r'^---\s*\n(.*?)\n---', re.DOTALL)

for full_path, rel_path in wiki_files:
    try:
        content = full_path.read_text(encoding='utf-8')
    except:
        continue
    
    # Check WikiLinks [[]]
    for match in cross_link_pattern.finditer(content):
        link = match.group(1).strip()
        # Try exact slug match
        if link in wiki_slugs:
            continue
        # Try basename match
        if link in wiki_basenames and len(wiki_basenames[link]) > 0:
            continue
        # Try partial match (link might be a substring of a slug)
        found = False
        for slug in wiki_slugs:
            if slug.endswith("/" + link) or slug == link:
                found = True
                break
        if not found:
            # Also try matching just the last part of the link
            for slug in wiki_slugs:
                if Path(slug).stem == link or Path(slug).name == link:
                    found = True
                    break
        if not found:
            broken_links[str(rel_path)].append(link)

# --- 2. Raw素材未整理检查 ---
# Check which raw files are referenced in wiki
referenced_raw_files = set()
for full_path, rel_path in wiki_files:
    try:
        content = full_path.read_text(encoding='utf-8')
    except:
        continue
    for match in raw_link_pattern.finditer(content):
        url = match.group(2)
        if '../raw/' in url or 'raw/' in url:
            # Extract the raw file reference
            parts = url.split('raw/')
            if len(parts) > 1:
                referenced_raw_files.add(parts[1])

unreferenced_raw = []
for full_path, rel_path in raw_files:
    raw_rel = str(rel_path)
    # Check if this raw file is referenced in any wiki
    is_referenced = False
    for ref in referenced_raw_files:
        if ref in raw_rel or raw_rel.endswith(ref):
            is_referenced = True
            break
    # Also check by filename in wiki content
    if not is_referenced:
        basename = full_path.stem
        # More thorough check: any wiki mentions this raw file?
        for wfull, wrel in wiki_files[:]:  # We'll do a quick scan via earlier content if cached
            pass  # Too slow, skip deep scan
    unreferenced_raw.append((str(rel_path), is_referenced))

# --- 3. Frontmatter check ---
frontmatter_issues = defaultdict(list)
for full_path, rel_path in wiki_files:
    try:
        content = full_path.read_text(encoding='utf-8')
    except:
        continue
    
    if content.startswith('---'):
        fm_match = frontmatter_pattern.match(content)
        if fm_match:
            fm_text = fm_match.group(1)
            # Check for tags residue
            if 'tags:' in fm_text.lower():
                # This is OK for Quartz, but check if it's a residual frontmatter tag
                # that shouldn't be there (e.g., from raw migration)
                lines = fm_text.split('\n')
                for line in lines:
                    stripped = line.strip()
                    if stripped.lower().startswith('tags:'):
                        # Check if tags are empty or just []
                        tag_val = stripped.split(':', 1)[1].strip()
                        if tag_val in ('[]', ''):
                            frontmatter_issues[str(rel_path)].append("tags 欄位為空或空陣列，考慮移除")
            # Check for other frontmatter issues
            if 'draft:' in fm_text.lower():
                frontmatter_issues[str(rel_path)].append("含有 draft 欄位殘留")
        else:
            frontmatter_issues[str(rel_path)].append("frontmatter 格式異常（--- 未正確關閉）")
    else:
        # 產業地圖 和 每日分析 可能有不同的格式要求
        if not str(rel_path).startswith("產業地圖/") and not str(rel_path).startswith("每日分析/") and not str(rel_path).startswith("YouTube頻道/") and str(rel_path) != "INDEX.md":
            frontmatter_issues[str(rel_path)].append("缺少 YAML frontmatter")

# --- 4. Orphan pages (wiki pages not linked by any other wiki page, not in INDEX.md) ---
# Build reverse link map
linked_pages = set()
for full_path, rel_path in wiki_files:
    try:
        content = full_path.read_text(encoding='utf-8')
    except:
        continue
    for match in cross_link_pattern.finditer(content):
        link = match.group(1).strip()
        linked_pages.add(link)
        # Also add resolved slugs
        if link in wiki_basenames:
            for s in wiki_basenames[link]:
                linked_pages.add(s)

# Check INDEX.md
try:
    index_content = (WIKI_DIR / "INDEX.md").read_text(encoding='utf-8')
    for match in cross_link_pattern.finditer(index_content):
        link = match.group(1).strip()
        linked_pages.add(link)
        if link in wiki_basenames:
            for s in wiki_basenames[link]:
                linked_pages.add(s)
except:
    pass

orphan_pages = []
for full_path, rel_path in wiki_files:
    if str(rel_path) == "INDEX.md":
        continue
    slug = str(rel_path.with_suffix(""))
    basename = rel_path.stem
    # Check if this page is linked from anywhere
    is_linked = False
    if slug in linked_pages or basename in linked_pages:
        is_linked = True
    if not is_linked:
        # Also check partial matches
        for lp in linked_pages:
            if slug.endswith("/" + lp) or lp.endswith("/" + basename):
                is_linked = True
                break
    if not is_linked:
        orphan_pages.append(str(rel_path))

# --- 5. Format template compliance ---
format_issues = defaultdict(list)
required_sections = ["核心概念", "實戰應用", "注意事項", "相關主題"]

for full_path, rel_path in wiki_files:
    if str(rel_path) == "INDEX.md":
        continue
    # Skip special categories that have different format
    if str(rel_path).startswith("產業地圖/") or str(rel_path).startswith("每日分析/") or str(rel_path).startswith("YouTube頻道/"):
        continue
    
    try:
        content = full_path.read_text(encoding='utf-8')
    except:
        continue
    
    # Check for required sections
    for section in required_sections:
        if f"## {section}" not in content:
            format_issues[str(rel_path)].append(f"缺少 ## {section} 段落")

    # Check for one-line summary (> 一句話摘要)
    if "> " not in content[:500]:
        # Allow some flexibility
        first_500 = content[:500]
        if not re.search(r'^>\s+', first_500, re.MULTILINE):
            format_issues[str(rel_path)].append("缺少一句話摘要（> 開頭）")

    # Check for 來源 section
    if "## 來源" not in content:
        format_issues[str(rel_path)].append("缺少 ## 來源 段落")

# --- 6. 資料時效性 ---
# Check 每日分析 pages for staleness
stale_pages = []
for full_path, rel_path in wiki_files:
    if str(rel_path).startswith("每日分析/"):
        # Extract date from filename or content
        fname = rel_path.stem  # e.g. "2026-05-18"
        try:
            page_date = datetime.strptime(fname, "%Y-%m-%d")
            days_old = (datetime.now() - page_date).days
            if days_old > 30:
                stale_pages.append((str(rel_path), days_old, "每日分析超過30天"))
        except ValueError:
            pass

# Check YouTube pages for date references
for full_path, rel_path in wiki_files:
    if str(rel_path).startswith("YouTube頻道/"):
        try:
            content = full_path.read_text(encoding='utf-8')
            # Look for date patterns in frontmatter
            fm_match = frontmatter_pattern.match(content)
            if fm_match:
                fm_text = fm_match.group(1)
                date_match = re.search(r'date:\s*(\d{4}-\d{2}-\d{2})', fm_text)
                if date_match:
                    page_date = datetime.strptime(date_match.group(1), "%Y-%m-%d")
                    days_old = (datetime.now() - page_date).days
                    if days_old > 60:
                        stale_pages.append((str(rel_path), days_old, f"YouTube分析超過60天（{days_old}天前）"))
        except:
            pass

# --- 7. 矛盾內容檢測 (heuristic) ---
# Look for conflicting statements across similar topics
potential_contradictions = []

# Check for duplicate/overlapping concepts
overlap_check = {}
for full_path, rel_path in wiki_files:
    if str(rel_path).startswith("產業地圖/") or str(rel_path).startswith("每日分析/") or str(rel_path).startswith("YouTube頻道/") or str(rel_path) == "INDEX.md":
        continue
    stem = rel_path.stem
    # Normalize: remove English suffixes for comparison
    base_name = re.sub(r'[-\s](實戰|進階|判讀|策略|指標|應用|方法|理論|概念|指標|分析|概論|總論|Complete|Guide|Advanced|Practical|Strategy|Indicator|Theory|Concept|Method|Analysis|Overview|Response|Passivation|Confirmation|Framework|Index|Oscillator|System)$', '', stem, flags=re.IGNORECASE)
    if base_name in overlap_check:
        overlap_check[base_name].append(str(rel_path))
    else:
        overlap_check[base_name] = [str(rel_path)]

for base, pages in overlap_check.items():
    if len(pages) > 1:
        potential_contradictions.append((base, pages))

# --- Also check for 假突破三道過濾 duplication ---
dup_check = {}
for full_path, rel_path in wiki_files:
    stem = rel_path.stem
    if stem in dup_check:
        dup_check[stem].append(str(rel_path))
    else:
        dup_check[stem] = [str(rel_path)]

duplicates = []
for stem, pages in dup_check.items():
    if len(pages) > 1:
        duplicates.append((stem, pages))

# === OUTPUT REPORT ===
report = []
report.append("# 🔍 股票知識庫 Lint 報告")
report.append(f"**掃描時間**: {datetime.now().strftime('%Y-%m-%d %H:%M')}")
report.append(f"**Wiki 頁數**: {len(wiki_files)} | **Raw 素材數**: {len(raw_files)}")
report.append("")

# Broken cross-links
report.append("## 1. 🔗 斷掉的 Cross-Links")
if broken_links:
    count = sum(len(v) for v in broken_links.values())
    report.append(f"**發現 {count} 個斷连**")
    for source, links in sorted(broken_links.items()):
        for link in links:
            report.append(f"- `{source}` → `[[{link}]]` ❌ 目標不存在")
else:
    report.append("✅ 無斷掉的 cross-links")

report.append("")

# Orphan pages
report.append("## 2. 🏝️ 孤兒頁（無其他頁面連入）")
if orphan_pages:
    report.append(f"**發現 {len(orphan_pages)} 個孤兒頁**")
    # Group by category
    by_cat = defaultdict(list)
    for p in orphan_pages:
        cat = p.split("/")[0] if "/" in p else "根目錄"
        by_cat[cat].append(p)
    for cat, pages in sorted(by_cat.items()):
        report.append(f"\n### {cat} ({len(pages)})")
        for p in sorted(pages)[:20]:
            report.append(f"- `{p}`")
        if len(pages) > 20:
            report.append(f"- ... 還有 {len(pages)-20} 個")
else:
    report.append("✅ 無孤兒頁")

report.append("")

# Unreferenced raw files
unreferenced_count = sum(1 for _, ref in unreferenced_raw if not ref)
report.append("## 3. 📦 未整理的 Raw 素材")
report.append(f"**未在 wiki 中被引用的 raw 檔案**: {unreferenced_count} / {len(unreferenced_raw)}")
# Group by date
by_date = defaultdict(list)
for raw_path, is_ref in unreferenced_raw:
    if not is_ref:
        by_date["其他"].append(raw_path)
        # Try to extract date
        parts = raw_path.split("/")
        for p in parts:
            if re.match(r'\d{4}-\d{2}-\d{2}', p):
                by_date[p].append(raw_path)
                by_date["其他"].pop()
                break

for date, files in sorted(by_date.items()):
    if date == "其他" and not files:
        continue
    report.append(f"\n### {date} ({len(files)})")
    for f in sorted(files)[:15]:
        report.append(f"- `{f}`")
    if len(files) > 15:
        report.append(f"- ... 還有 {len(files)-15} 個")

report.append("")

# Potential contradictions / overlapping pages
report.append("## 4. ⚠️ 可能重複或矛盾的頁面")
if potential_contradictions:
    report.append(f"**發現 {len(potential_contradictions)} 組可能重疊的概念**")
    for base, pages in potential_contradictions[:20]:
        report.append(f"- **{base}**:")
        for p in pages:
            report.append(f"  - `{p}`")
else:
    report.append("✅ 無明顯重複概念")

if duplicates:
    report.append(f"\n**完全同名的頁面**: {len(duplicates)} 組")
    for stem, pages in duplicates:
        report.append(f"- `{stem}` 出現在: {', '.join(f'`{p}`' for p in pages)}")

report.append("")

# Frontmatter issues
report.append("## 5. 🏷️ Frontmatter 問題")
has_fm_issues = any(v for v in frontmatter_issues.values())
if has_fm_issues:
    count = sum(len(v) for v in frontmatter_issues.values() if v)
    report.append(f"**{count} 個問題**")
    for source, issues in sorted(frontmatter_issues.items()):
        for issue in issues:
            report.append(f"- `{source}`: {issue}")
else:
    report.append("✅ 無 frontmatter 問題")

report.append("")

# Format compliance
report.append("## 6. 📋 格式模板合規性")
has_format_issues = any(v for v in format_issues.values())
if has_format_issues:
    count = sum(len(v) for v in format_issues.values() if v)
    report.append(f"**{count} 個格式問題**（缺少必要段落）")
    # Only show the most common issues
    issue_counts = defaultdict(int)
    for source, issues in format_issues.items():
        for issue in issues:
            issue_counts[issue] += 1
    report.append("\n### 問題分布")
    for issue, cnt in sorted(issue_counts.items(), key=lambda x: -x[1]):
        report.append(f"- {issue}: {cnt} 頁")
    
    # List some examples
    report.append("\n### 範例（前10個）")
    shown = 0
    for source, issues in sorted(format_issues.items()):
        if issues and shown < 10:
            report.append(f"- `{source}`: {'; '.join(issues)}")
            shown += 1
else:
    report.append("✅ 所有頁面符合格式模板")

report.append("")

# Data staleness
report.append("## 7. ⏰ 資料時效性")
if stale_pages:
    report.append(f"**{len(stale_pages)} 個過舊頁面**")
    for path, days, note in sorted(stale_pages, key=lambda x: -x[1])[:20]:
        report.append(f"- `{path}` — {note}")
else:
    report.append("✅ 無過舊內容")

report.append("")

# Summary
report.append("## 📊 總結")
report.append(f"| 項目 | 數量 |")
report.append(f"|------|------|")
report.append(f"| 斷掉 cross-links | {sum(len(v) for v in broken_links.values())} |")
report.append(f"| 孤兒頁 | {len(orphan_pages)} |")
report.append(f"| 未引用 raw | {unreferenced_count} |")
report.append(f"| 重疊概念 | {len(potential_contradictions)} |")
report.append(f"| 完全同名頁面 | {len(duplicates)} |")
report.append(f"| Frontmatter 問題 | {sum(len(v) for v in frontmatter_issues.values())} |")
report.append(f"| 格式不合規 | {sum(len(v) for v in format_issues.values())} |")
report.append(f"| 過舊頁面 | {len(stale_pages)} |")

report.append("")
report.append("## 🔧 建議修復方式")
report.append("")

if broken_links:
    report.append("### 斷掉 cross-links")
    report.append("- 檢查連結名稱是否與實際頁面 slug 完全匹配")
    report.append("- 若目標頁面存在但名稱不同，更新連結或建立 alias")
    report.append("- 若目標頁面不存在，考慮建立或移除連結")
    report.append("")

if orphan_pages:
    report.append("### 孤兒頁")
    report.append("- 在 INDEX.md 或相關頁面的「相關主題」中加入連結")
    report.append("- 檢查是否為過時內容，可考慮合併或歸檔")
    report.append("")

if unreferenced_count > 0:
    report.append("### 未整理 raw 素材")
    report.append("- compile 流程應將這些素材整理進 wiki")
    report.append("- 注意：部分 raw 檔案可能是同名素材被不同 wiki 引用，此為估計值")
    report.append("")

if potential_contradictions:
    report.append("### 重疊概念")
    report.append("- 如果是同一主題的重複頁面，合併為一份")
    report.append("- 如果是相關但不同的主題，建立交叉連結並明確區分")
    report.append("")

if duplicates:
    report.append("### 完全同名頁面")
    report.append("- 這是嚴重問題，需要合併或重新命名")
    report.append("")

if has_format_issues:
    report.append("### 格式不合規")
    report.append("- 補齊缺少的段落（核心概念、實戰應用、注意事項、相關主題、來源）")
    report.append("- 加入一句話摘要（> 開頭）")
    report.append("")

# Output
output = "\n".join(report)
print(output)

# Also save to file
report_path = KB_ROOT / "outputs" / f"lint-report-{datetime.now().strftime('%Y%m%d-%H%M')}.md"
report_path.parent.mkdir(parents=True, exist_ok=True)
report_path.write_text(output, encoding='utf-8')
print(f"\n---\n報告已儲存至: {report_path}")