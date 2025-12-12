# Website Deployment Scripts

Quick automation scripts for building, committing, and deploying your website.

## Quick Start

### One-step deploy (build + commit + push):
```bash
cd /Users/bordoloi/WORK/Website/rongmon.github.io
./deploy.sh "Your change description"
./push.sh
```

## Scripts

### `deploy.sh` - Build and Commit
Automates the local build and commit process.

**Usage:**
```bash
./deploy.sh "Updated research page"
```

**What it does:**
1. Kills any running Hugo servers
2. Deletes old `docs/` folder
3. Rebuilds site with `hugo --minify`
4. Restores CNAME file
5. Cleans up `public/` folder
6. Commits all changes with your message
7. Shows git status

### `push.sh` - Push to GitHub
Pushes committed changes to GitHub.

**Usage:**
```bash
./push.sh
```

**What it does:**
1. Pushes to `origin master`
2. Shows success message
3. Site goes live in 30 seconds to 2 minutes

## Full Workflow Example

```bash
# 1. Edit content
nano content/academics/_index.md

# 2. Preview locally (optional)
hugo server -D
# Visit http://localhost:1313

# 3. Build and commit
./deploy.sh "Update academics page with new degree"

# 4. Push to GitHub
./push.sh

# 5. Check live site
# Visit https://rongmonbordoloi.com
```

## What to Edit

✅ **Edit these:**
- `content/` - All website content (markdown files)
- Images in `docs/images/` or reference via `/images/filename.jpg`

❌ **Don't edit these:**
- `docs/` - Auto-generated (gets deleted and rebuilt)
- `public/` - Old folder (will be removed)
- `config.toml` - Hugo configuration
- `themes/` - Hugo theme

## Commit Message Examples

Good commit messages:
```bash
./deploy.sh "Add new research area: Fermi Bubbles"
./deploy.sh "Update publication list with 2025 papers"
./deploy.sh "Fix broken image link in mass-acquisition page"
./deploy.sh "Add team member profile for new grad student"
```

## Troubleshooting

**If deploy.sh fails:**
```bash
# Check what's wrong
git status

# See the error
hugo --minify

# Fix the issue, then try again
./deploy.sh "Your message"
```

**If push fails:**
```bash
# Check your authentication
git push origin master

# If still failing, use personal access token or SSH
```

**To undo last commit:**
```bash
git reset --hard HEAD~1
```

## Manual Steps (if you prefer)

If you don't want to use scripts:

```bash
# Kill servers
pkill -f "hugo server"

# Build
rm -rf docs
hugo --minify
echo "rongmonbordoloi.com" > docs/CNAME
rm -rf public

# Commit
git add -A
git commit -m "Your message"

# Push
git push origin master
```

---

**Created:** December 11, 2025
