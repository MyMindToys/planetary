#!/usr/bin/env bash
# Сборка для деплоя (Render и др.): Python-зависимости + сборка Vue.
set -e
pip install -r requirements.txt
cd frontend
if command -v pnpm &>/dev/null; then
  pnpm install --frozen-lockfile
  pnpm run build
elif command -v npm &>/dev/null; then
  npm ci
  npm run build
else
  echo "Need pnpm or npm to build frontend"
  exit 1
fi
