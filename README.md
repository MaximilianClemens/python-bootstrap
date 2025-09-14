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
from pathlib import Path
import importlib.metadata

app = FastAPI()

# Get Bootstrap assets path
dist = importlib.metadata.distribution("bootstrap-wrapper")
static_path = Path(dist.locate_file("bootstrap_wrapper/dist"))

# Mount Bootstrap static files
app.mount("/bootstrap", StaticFiles(directory=str(static_path)), name="bootstrap")

# Access Bootstrap at:
# http://localhost:8000/bootstrap/css/bootstrap.min.css
# http://localhost:8000/bootstrap/js/bootstrap.bundle.min.js
```

**Flask Example:**
```python
from flask import Flask, send_from_directory
import importlib.metadata
from pathlib import Path

app = Flask(__name__)

dist = importlib.metadata.distribution("bootstrap-wrapper")
BOOTSTRAP_PATH = Path(dist.locate_file("bootstrap_wrapper/dist"))

@app.route('/bootstrap/<path:filename>')
def bootstrap_static(filename):
    return send_from_directory(str(BOOTSTRAP_PATH), filename)
```

**Django Example:**
```python
# In settings.py
import importlib.metadata
from pathlib import Path

dist = importlib.metadata.distribution("bootstrap-wrapper")
BOOTSTRAP_STATIC_ROOT = Path(dist.locate_file("bootstrap_wrapper/dist"))

STATICFILES_DIRS = [
    BOOTSTRAP_STATIC_ROOT,
]
```

### Automatic Updates

- **Schedule**: The Bootstrap assets are automatically updated weekly on Mondays at 09:00 UTC
- **Manual Trigger**: You can manually trigger an update by running the "Sync Bootstrap Dist" workflow
- **Pull Requests**: When a new Bootstrap version is available, the workflow automatically creates a pull request with the updated files
- **Version Tags**: When Bootstrap updates, a corresponding git tag is automatically created (e.g., `5.3.8`)

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
5. Creates a git tag matching the Bootstrap version for PyPI releases

## Development

Run the example script to see usage examples:

```bash
python example_usage.py
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

Bootstrap itself is also licensed under the MIT License.
