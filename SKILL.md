---
name: stock-knowledge-base
description: 股票知識庫操作手冊。使用時機：(1) 整理 raw/ 中的學習素材到 wiki/ (2) 查詢股票知識 (3) lint 掃描知識庫 (4) 新增學習素材 (5) 同步部署到 Quartz 網站。觸發詞：整理知識庫、查股票、lint 知識庫、新增素材、同步部署、股票知識庫。
---

# Stock Knowledge Base Skill

## 目錄結構

```
stock-knowledge-base/
├── SCHEMA.md     ← Schema（規則和方向）
├── SKILL.md      ← 操作手冊（這份檔案）
├── raw/          ← 原始學習素材（每日學習的原始內容）
│   └── YYYY-MM-DD/  ← 按日期分類
├── wiki/         ← 整理好的概念筆記（Markdown，帶 cross-links）
│   ├── index.md  ← 概念目錄
│   ├── 基本面分析/
│   ├── 技術分析/
│   ├── 操作策略/
│   ├── 籌碼面分析/
│   └── 風險管理/
├── outputs/      ← AI 產出的報告、問答、分析
└── scripts/      ← 自動化腳本
```

知識庫根目錄：`~/.openclaw/workspace/stock-knowledge-base/`

**重要：先讀 SCHEMA.md，它定義了知識庫的規則和方向。**

## Quartz 網站部署

知識庫透過 Quartz v4 部署到 GitHub Pages，讓老綸可以在任何網頁瀏覽器查看。

- **本地 Quartz 專案**：`~/.openclaw/workspace/stock-quartz-site/`
- **同步腳本**：`stock-quartz-site/sync-wiki-to-quartz.sh`
- **部署方式**：Push 到 main → GitHub Actions 自動 build + deploy

### 更新流程

1. 整理完知識庫後，執行 `sync-wiki-to-quartz.sh`
2. `cd stock-quartz-site && npx quartz sync`
3. GitHub Actions 自動部署

### 同步指令詳解

```bash
# 1. 同步 wiki 內容到 Quartz
~/.openclaw/workspace/stock-quartz-site/sync-wiki-to-quartz.sh

# 2. 推送到 GitHub（會自動 build + deploy）
cd ~/.openclaw/workspace/stock-quartz-site && npx quartz sync

# 或者手動步驟：
cd ~/.openclaw/workspace/stock-quartz-site
rsync -av --delete --exclude='SCHEMA.md' --exclude='SKILL.md' \
  ~/.openclaw/workspace/stock-knowledge-base/wiki/ content/
git add -A
git commit -m "Update stock knowledge base"
git push

# 本地預覽：
cd ~/.openclaw/workspace/stock-quartz-site && npx quartz build --serve
```

## 操作流程

### 1. 新增素材（add）

每日學習 cron 會自動將學習內容存到 `raw/YYYY-MM-DD/`。
手動新增時：

1. 如果是 URL：用 `web_fetch` 抓取內容，存到 `raw/YYYY-MM-DD/title.md`
2. 如果是文字：直接存到 `raw/YYYY-MM-DD/title.md`
3. 檔案開頭加 YAML frontmatter：
   ```yaml
   ---
   source: URL 或 "daily-learning"
   date: YYYY-MM-DD
   tags: [相關標籤]
   ---
   ```
4. 告知用戶已新增

### 2. 整理知識庫（compile）

當用戶說「整理知識庫」或 `raw/` 有未整理素材時：

1. 列出 `raw/` 中所有日期資料夾
2. 讀取每個素材的內容
3. 提取核心概念，為每個概念建立或更新 `wiki/` 筆記：
   - 檔名用中文：`wiki/分類/主題名稱.md`
   - 內容結構：
     ```markdown
     # 主題名稱
     
     > 一句話摘要
     
     ## 核心概念
     （整理後的知識）
     
     ## 實戰應用
     （如何實際使用）
     
     ## 注意事項
     （陷阱、誤區、限制）
     
     ## 相關主題
     - [[相關主題A]]
     - [[相關主題B]]
     
     ## 來源
     - [文章標題](../raw/YYYY-MM-DD/檔名.md)
     ```
4. 更新 `wiki/index.md` 的概念列表
5. 整理完的 `raw/` 檔案保留（不刪除，作為溯源用）
6. **🔄 自動同步：執行 sync-wiki-to-quartz.sh → npx quartz sync 推送到 GitHub**

### 3. 查詢知識（query）

當用戶說「查 [問題]」時：

1. 用 `memory_search` 搜尋 `wiki/` 和 `raw/` 的內容（corpus=memory）
2. 讀取最相關的 wiki 筆記
3. 整合回答，附上參考來源
4. 如果答案是新的有用知識，存回 wiki 並更新 index.md
5. **🔄 如果有修改 wiki：自動同步部署**

### 4. Lint 知識庫（lint）

當用戶說「lint 知識庫」時：

1. 掃描所有 wiki 筆記
2. 檢查：
   - 斷掉的 cross-links（`[[]]` 指向不存在的筆記）
   - 未整理的 raw 素材（raw/ 中未被 wiki 引用的）
   - 矛盾內容（不同筆記間的衝突陳述）
   - LaTeX 數學公式中的中文標點問題
   - frontmatter 缺失或不完整
3. 回報結果，建議修復方式
4. **🔄 如果有修改 wiki：自動同步部署**

### 5. 同步部署（deploy）

將 wiki 內容同步到 Quartz 並部署：

```bash
# 完整流程
~/.openclaw/workspace/stock-quartz-site/sync-wiki-to-quartz.sh
cd ~/.openclaw/workspace/stock-quartz-site && npx quartz sync
```

## 中文 slug 處理

Stock KB 大量使用中文檔名。Quartz v4 原生支援 UTF-8 slug，中文 URL 在現代瀏覽器中可正常顯示和搜尋。

- 檔名：使用中文，例如 `技術分析/MACD指標實戰判讀.md`
- URL：瀏覽器會自動將中文編碼為 `%E6%8A%80%E8%A1%93...` 格式，但顯示時仍為中文
- 搜尋：Quartz 內建全文搜尋，中文內容可正常搜尋

## 注意事項

- wiki 筆記用 WikiLink 語法 `[[主題名稱]]` 做交叉連結
- 每次整理都更新 index.md
- raw/ 素材永遠不刪，只增加
- 整理時以概念為單位，不是以來源為單位（多篇 raw 可能合併成一個概念）
- **每次 compile / lint 修改 wiki 後，必須自動同步部署到 GitHub Pages**
- Stock KB 的分類：技術分析、基本面分析、籌碼面分析、操作策略、風險管理