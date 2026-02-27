#!/usr/bin/env bash
# Сборка для деплоя (Render и др.): Python-зависимости + сборка Vue.
set -e

pip install -r requirements.txt
python manage.py migrate --noinput

# Node нужен для сборки фронта; на Render в Python-сервисе его может не быть — ставим через nvm
if ! command -v node &>/dev/null; then
  export NVM_DIR="$HOME/.nvm"
  if [ -s "$NVM_DIR/nvm.sh" ]; then
    . "$NVM_DIR/nvm.sh"
  fi
  if ! command -v node &>/dev/null; then
    echo "Installing Node via nvm..."
    curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.40.1/install.sh | bash
    export NVM_DIR="$HOME/.nvm"
    [ -s "$NVM_DIR/nvm.sh" ] && . "$NVM_DIR/nvm.sh"
    nvm install 20
    nvm use 20
  fi
fi

cd frontend
corepack enable 2>/dev/null || true
if command -v pnpm &>/dev/null; then
  pnpm install --frozen-lockfile
  pnpm run build
elif command -v npm &>/dev/null; then
  npm install
  npm run build
else
  npm install -g pnpm
  pnpm install --frozen-lockfile
  pnpm run build
fi
