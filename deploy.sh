#!/bin/bash

# Website deployment script
# Usage: ./deploy.sh "Your commit message here"

set -e

# Check if commit message provided
if [ -z "$1" ]; then
    echo "❌ Error: Please provide a commit message"
    echo "Usage: ./deploy.sh \"Your commit message\""
    exit 1
fi

COMMIT_MSG="$1"

echo "🔨 Starting website deployment..."
echo ""

# Step 1: Kill any running Hugo servers
echo "1️⃣  Killing any running Hugo servers..."
pkill -f "hugo server" 2>/dev/null || true
sleep 1

# Step 2: Clean and rebuild
echo "2️⃣  Building site..."
rm -rf docs
hugo --minify
echo "✅ Site built successfully (CNAME auto-restored)"
echo ""

# Step 3: Commit
echo "3️⃣  Committing changes..."
git add -A
git commit -m "$COMMIT_MSG" || echo "⚠️  No changes to commit"
echo "✅ Committed"
echo ""

# Step 4: Show status
echo "📊 Git Status:"
git status
echo ""

# Step 5: Ready to push
echo "🚀 Ready to push!"
echo ""
echo "To push to GitHub, run:"
echo "  git push origin master"
echo ""
echo "Or you can use the push script:"
echo "  ./push.sh"
