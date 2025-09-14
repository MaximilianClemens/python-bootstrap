# bootstrap-wrapper
Python Wrapper for Bootstrap CSS/JavaScript Assets

## Overview

This repository automatically syncs with the latest Bootstrap distribution files from the official [Bootstrap repository](https://github.com/twbs/bootstrap) and packages them for easy distribution via Python's packaging system.

**✨ NEW: Now installable as a Python package!**

```bash
pip install bootstrap-wrapper==5.3.8
```

## Bootstrap Assets

This repository automatically syncs with the latest Bootstrap distribution files from the official [Bootstrap repository](https://github.com/twbs/bootstrap).

### Installation & Usage

#### Install from PyPI (Recommended)

```bash
pip install bootstrap-wrapper==5.3.8
```

#### Usage in Web Frameworks

**FastAPI Example:**
```python
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
import bootstrap_wrapper

app = FastAPI()

# Get Bootstrap assets path
static_path = bootstrap_wrapper.get_bootstrap_dir()

# Mount Bootstrap static files
app.mount("/bootstrap", StaticFiles(directory=str(static_path)), name="bootstrap")

# Access Bootstrap at:
# http://localhost:8000/bootstrap/css/bootstrap.min.css
# http://localhost:8000/bootstrap/js/bootstrap.bundle.min.js
```

**Flask Example:**
```python
from flask import Flask, send_from_directory
import bootstrap_wrapper

app = Flask(__name__)

BOOTSTRAP_PATH = bootstrap_wrapper.get_bootstrap_dir()

@app.route('/bootstrap/<path:filename>')
def bootstrap_static(filename):
    return send_from_directory(str(BOOTSTRAP_PATH), filename)
```

**Django Example:**
```python
# In settings.py
import bootstrap_wrapper

BOOTSTRAP_STATIC_ROOT = bootstrap_wrapper.get_bootstrap_dir()

STATICFILES_DIRS = [
    BOOTSTRAP_STATIC_ROOT,
]
```

### Automatic Updates

- **Schedule**: The Bootstrap assets are automatically updated weekly on Mondays at 09:00 UTC
- **Manual Trigger**: You can manually trigger an update by running the "Sync Bootstrap Dist" workflow
  - **Force Update**: Use the `force_update` option to force an update even if the version is the same
- **Auto-Merge**: When a new Bootstrap version is available, the workflow automatically:
  1. Creates a pull request with the updated files
  2. Auto-merges the PR (no manual review required)
  3. Creates a git tag matching the Bootstrap version (e.g., `5.3.8`)
  4. Creates a GitHub release automatically
  5. Triggers PyPI publishing via the existing publish workflow

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
5. Auto-merges the pull request immediately (no manual review required)
6. Creates a git tag matching the Bootstrap version for PyPI releases
7. Creates a GitHub release automatically
8. Triggers PyPI package publishing through the existing publish workflow

## Development

Run the example script to see usage examples:

```bash
python example_usage.py
```

### Publishing to PyPI

The project is automatically published to PyPI as `bootstrap-wrapper` when:
1. A new GitHub release is created 
2. The GitHub Actions workflow runs successfully

For manual publishing (if needed):

```bash
# Install build tools
pip install build twine

# Build the package
python -m build

# Upload to PyPI (requires API token)
twine upload dist/*
```

**Note**: The package uses trusted publishing via GitHub Actions, so manual uploads should generally not be necessary.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

Bootstrap itself is also licensed under the MIT License.
