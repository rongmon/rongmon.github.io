#!/bin/bash

# Push to GitHub script
# Usage: ./push.sh

set -e

echo "🚀 Pushing to GitHub..."
git push origin master

if [ $? -eq 0 ]; then
    echo ""
    echo "✅ Successfully pushed to GitHub!"
    echo ""
    echo "Your changes will be live in 30 seconds to 2 minutes."
    echo "Visit: https://rongmonbordoloi.com"
else
    echo ""
    echo "❌ Push failed. Check your authentication and try again."
    exit 1
fi
