#!/bin/bash
# lint-wiki.sh
# 掃描知識庫 wiki/ 中的常見問題
# 用法: bash scripts/lint-wiki.sh [--fix]
#   --fix: 自動修復可修復的問題（目前僅回報）

set -e

KB_DIR="$(cd "$(dirname "$0")/.." && pwd)"
WIKI_DIR="$KB_DIR/wiki"

FIX_MODE=false
[[ "$1" == "--fix" ]] && FIX_MODE=true

echo "🔍 Stock KB Wiki Lint"
echo "====================="
echo ""

ERRORS=0
WARNINGS=0

# 1. 檢查斷掉的 cross-links
echo "1️⃣ 檢查交叉連結..."
BROKEN_LINKS=0
while IFS= read -r file; do
    # 找出所有 [[連結]]
    LINKS=$(grep -oE '\[\[[^]|]+' "$file" | sed 's/\[\[//')
    for link in $LINKS; do
        # 在 wiki/ 下搜尋對應檔案
        FOUND=$(find "$WIKI_DIR" -name "${link}.md" -o -name "${link}" 2>/dev/null | head -1)
        if [[ -z "$FOUND" ]]; then
            # 也檢查子目錄
            FOUND=$(find "$WIKI_DIR" -name "*${link}*.md" 2>/dev/null | head -1)
            if [[ -z "$FOUND" ]]; then
                REL_FILE="${file#$WIKI_DIR/}"
                echo "  ❌ 斷連結: $REL_FILE → [[$link]]"
                ((BROKEN_LINKS++))
            fi
        fi
    done
done < <(find "$WIKI_DIR" -name "*.md" -not -name "index.md" -not -name "INDEX.md")

if [[ $BROKEN_LINKS -eq 0 ]]; then
    echo "  ✅ 所有交叉連結正常"
else
    echo "  ⚠️  發現 $BROKEN_LINKS 個斷連結"
    ((ERRORS+=BROKEN_LINKS))
fi
echo ""

# 2. 檢查 LaTeX 中的中文標點
echo "2️⃣ 檢查 LaTeX 中文標點..."
LATEX_ISSUES=0
while IFS= read -r file; do
    # 找出 $...$ 或 $$...$$ 中含中文標點的行
    ISSUES=$(grep -nP '\$[^$]*[\u3001\u3002\uff0c\uff0e\uff1b\uff1a\uff01\uff1f]\$' "$file" 2>/dev/null || true)
    if [[ -n "$ISSUES" ]]; then
        REL_FILE="${file#$WIKI_DIR/}"
        echo "  ⚠️  $REL_FILE"
        echo "$ISSUES" | head -3 | while IFS= read -r line; do
            echo "      $line"
        done
        ((LATEX_ISSUES++))
    fi
done < <(find "$WIKI_DIR" -name "*.md")

if [[ $LATEX_ISSUES -eq 0 ]]; then
    echo "  ✅ LaTeX 公式無中文標點問題"
else
    echo "  ⚠️  $LATEX_ISSUES 個檔案有 LaTeX 中文標點"
    ((WARNINGS+=LATEX_ISSUES))
fi
echo ""

# 3. 檢查 frontmatter
echo "3️⃣ 檢查 frontmatter..."
MISSING_FM=0
while IFS= read -r file; do
    FIRST_LINE=$(head -1 "$file")
    if [[ "$FIRST_LINE" != "---" ]]; then
        REL_FILE="${file#$WIKI_DIR/}"
        echo "  ⚠️  缺少 frontmatter: $REL_FILE"
        ((MISSING_FM++))
    fi
done < <(find "$WIKI_DIR" -name "*.md" -not -name "index.md" -not -name "INDEX.md")

if [[ $MISSING_FM -eq 0 ]]; then
    echo "  ✅ 所有筆記都有 frontmatter"
else
    echo "  ⚠️  $MISSING_FM 個筆記缺少 frontmatter"
    ((WARNINGS+=MISSING_FM))
fi
echo ""

# 4. 檢查未整理的 raw 素材
echo "4️⃣ 檢查未整理的 raw 素材..."
RAW_DIR="$KB_DIR/raw"
TOTAL_RAW=0
UNREFERENCED=0

for date_dir in "$RAW_DIR"/*/; do
    for raw_file in "$date_dir"*.md; do
        [[ -f "$raw_file" ]] || continue
        ((TOTAL_RAW++))
        # 檢查是否有 wiki 筆記引用這個 raw 檔
        BASENAME=$(basename "$raw_file" .md)
        REFERENCED=$(grep -rl "$BASENAME" "$WIKI_DIR" 2>/dev/null | head -1)
        if [[ -z "$REFERENCED" ]]; then
            REL_PATH="${raw_file#$KB_DIR/}"
            # 不逐一列出，太多
            ((UNREFERENCED++))
        fi
    done
done

echo "  📊 Raw 素材總數: $TOTAL_RAW"
if [[ $UNREFERENCED -gt 0 ]]; then
    echo "  ⚠️  未被 wiki 引用: $UNREFERENCED 個（可能尚未整理）"
    ((WARNINGS+=1))
else
    echo "  ✅ 所有 raw 素材都已被 wiki 引用"
fi
echo ""

# 5. 統計
echo "📊 統計"
echo "-------"
WIKI_COUNT=$(find "$WIKI_DIR" -name "*.md" -not -name "index.md" -not -name "INDEX.md" | wc -l | tr -d ' ')
echo "  Wiki 筆記數: $WIKI_COUNT"
echo "  Raw 素材數: $TOTAL_RAW"
echo ""

# 總結
echo "🎯 總結"
echo "-------"
if [[ $ERRORS -eq 0 && $WARNINGS -eq 0 ]]; then
    echo "  ✅ 知識庫健康！"
elif [[ $ERRORS -eq 0 ]]; then
    echo "  ⚠️  有 $WARNINGS 個警告，但不影響使用"
else
    echo "  ❌ 有 $ERRORS 個錯誤和 $WARNINGS 個警告需要修復"
fi