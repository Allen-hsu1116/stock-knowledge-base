#!/bin/bash
# sync-and-deploy.sh
# 一次性同步 wiki 到 Quartz 並部署到 GitHub Pages
# 用法: bash scripts/sync-and-deploy.sh

set -e

KB_DIR="$(cd "$(dirname "$0")/.." && pwd)"
QUARTZ_DIR="$KB_DIR/../stock-quartz-site"

echo "🐍 Stock KB → Quartz 同步部署"
echo "================================"

# Step 1: 同步 wiki → Quartz content
echo ""
echo "📥 Step 1: 同步 wiki → Quartz content/"
bash "$QUARTZ_DIR/sync-wiki-to-quartz.sh"

# Step 2: Build & push
echo ""
echo "🚀 Step 2: 推送到 GitHub"
cd "$QUARTZ_DIR"
npx quartz sync

echo ""
echo "✅ 部署完成！"
echo "   GitHub Actions 將在 1-2 分鐘後完成部署"