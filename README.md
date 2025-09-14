# python-bootstrap
Python Wrapper for Bootstrap

## Bootstrap Assets

This repository automatically syncs with the latest Bootstrap distribution files from the official [Bootstrap repository](https://github.com/twbs/bootstrap).

### Automatic Updates

- **Schedule**: The Bootstrap assets are automatically updated weekly on Mondays at 09:00 UTC
- **Manual Trigger**: You can manually trigger an update by running the "Sync Bootstrap Dist" workflow
- **Pull Requests**: When a new Bootstrap version is available, the workflow automatically creates a pull request with the updated files

### Bootstrap Files

The Bootstrap distribution files are stored in the `bootstrap/` directory:
- `bootstrap/css/` - Bootstrap CSS files (minified and source)
- `bootstrap/js/` - Bootstrap JavaScript files (minified and source)  
- `bootstrap/version.txt` - Current Bootstrap version

### Workflow

The sync process uses the GitHub Actions workflow located at `.github/workflows/sync-bootstrap-dist.yml` which:

1. Checks the latest Bootstrap release via GitHub API
2. Compares with the current version in `bootstrap/version.txt`
3. Downloads and extracts the official Bootstrap dist ZIP if an update is needed
4. Creates a pull request with the updated files
