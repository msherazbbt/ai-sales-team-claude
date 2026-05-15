#!/bin/bash
# Sets up LibreChat (https://github.com/danny-avila/LibreChat) from source.
# Requires: Node.js 18+, npm, MongoDB 5+.
# Optional: Docker + Docker Compose for the full stack (MongoDB, MeiliSearch, pgvector).
set -e

LIBRECHAT_DIR="${LIBRECHAT_DIR:-$HOME/LibreChat}"

# ── Clone ──────────────────────────────────────────────────────────────────
if [ ! -d "$LIBRECHAT_DIR" ]; then
    echo "Cloning LibreChat..."
    git clone --depth 1 https://github.com/danny-avila/LibreChat.git "$LIBRECHAT_DIR"
fi

cd "$LIBRECHAT_DIR"

# ── SheetJS CDN workaround ─────────────────────────────────────────────────
# SheetJS is distributed via a private CDN; replace with the npm registry version.
for f in api/package.json packages/api/package.json; do
    if [ -f "$f" ]; then
        sed -i 's|"xlsx": "https://cdn.sheetjs.com/[^"]*"|"xlsx": "^0.18.5"|g' "$f"
    fi
done
sed -i 's|"resolved": "https://cdn.sheetjs.com/[^"]*"|"resolved": "https://registry.npmjs.org/xlsx/-/xlsx-0.18.5.tgz"|g' package-lock.json 2>/dev/null || true
sed -i 's|"xlsx": "https://cdn.sheetjs.com/[^"]*"|"xlsx": "^0.18.5"|g' package-lock.json 2>/dev/null || true

# ── Install dependencies ───────────────────────────────────────────────────
echo "Installing npm dependencies..."
npm install

# ── Create .env ────────────────────────────────────────────────────────────
if [ ! -f .env ]; then
    cp .env.example .env
    # Generate secure secrets
    sed -i "s/^JWT_SECRET=.*/JWT_SECRET=$(openssl rand -hex 32)/" .env
    sed -i "s/^JWT_REFRESH_SECRET=.*/JWT_REFRESH_SECRET=$(openssl rand -hex 32)/" .env
    sed -i "s/^CREDS_KEY=.*/CREDS_KEY=$(openssl rand -hex 32)/" .env
    sed -i "s/^CREDS_IV=.*/CREDS_IV=$(openssl rand -hex 16)/" .env
    sed -i "s/^MEILI_MASTER_KEY=.*/MEILI_MASTER_KEY=$(openssl rand -hex 24)/" .env
    echo ".env created with generated secrets. Edit it to add your LLM API keys."
fi

# ── Build ──────────────────────────────────────────────────────────────────
echo "Building LibreChat..."
npm run build

echo ""
echo "LibreChat built successfully."
echo ""
echo "To start (requires MongoDB on localhost:27017):"
echo "  cd $LIBRECHAT_DIR && npm run backend"
echo ""
echo "Or start the full stack with Docker Compose (requires docker login):"
echo "  cd $LIBRECHAT_DIR && docker compose up -d"
echo "  Then open http://localhost:3080"
