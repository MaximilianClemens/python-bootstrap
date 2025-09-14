#!/usr/bin/env python3
"""
Example usage of bootstrap-wrapper package

This demonstrates how to use the bootstrap-wrapper package in web applications
to serve Bootstrap CSS and JavaScript files.
"""

from pathlib import Path
import importlib.metadata

def get_bootstrap_assets():
    """Get the path to Bootstrap assets after package installation"""
    try:
        # This will work after pip install bootstrap-wrapper
        import bootstrap_wrapper
        return bootstrap_wrapper.get_bootstrap_dir()
    except ImportError:
        # Fallback for development - use local bootstrap directory
        return Path(__file__).parent / "bootstrap"

def fastapi_example():
    """Example FastAPI setup"""
    code = '''
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from pathlib import Path
import importlib.metadata

app = FastAPI()

# Get Bootstrap assets path
try:
    import bootstrap_wrapper
    static_path = bootstrap_wrapper.get_bootstrap_dir()
except ImportError:
    # Development fallback
    static_path = Path("bootstrap")

# Mount Bootstrap static files
app.mount("/bootstrap", StaticFiles(directory=str(static_path)), name="bootstrap")

# Now you can access:
# http://localhost:8000/bootstrap/css/bootstrap.min.css
# http://localhost:8000/bootstrap/js/bootstrap.bundle.min.js

@app.get("/")
async def root():
    return {
        "message": "Bootstrap assets available at /bootstrap/",
        "css": "/bootstrap/css/bootstrap.min.css",
        "js": "/bootstrap/js/bootstrap.bundle.min.js"
    }
'''
    return code

def django_example():
    """Example Django setup"""
    code = '''
# In your Django settings.py:
import importlib.metadata
from pathlib import Path

try:
    import bootstrap_wrapper
    BOOTSTRAP_STATIC_ROOT = bootstrap_wrapper.get_bootstrap_dir()
except ImportError:
    BOOTSTRAP_STATIC_ROOT = Path("bootstrap")

# Add to STATICFILES_DIRS
STATICFILES_DIRS = [
    BOOTSTRAP_STATIC_ROOT,
]

# Or configure as a custom static files finder
# and use {% load static %} with {% static "css/bootstrap.min.css" %} in templates
'''
    return code

def flask_example():
    """Example Flask setup"""
    code = '''
from flask import Flask, send_from_directory
import importlib.metadata
from pathlib import Path

app = Flask(__name__)

try:
    import bootstrap_wrapper
    BOOTSTRAP_PATH = bootstrap_wrapper.get_bootstrap_dir()
except ImportError:
    BOOTSTRAP_PATH = Path("bootstrap")

@app.route('/bootstrap/<path:filename>')
def bootstrap_static(filename):
    return send_from_directory(str(BOOTSTRAP_PATH), filename)

# Now you can access:
# http://localhost:5000/bootstrap/css/bootstrap.min.css
# http://localhost:5000/bootstrap/js/bootstrap.bundle.min.js
'''
    return code

if __name__ == "__main__":
    print("🎯 bootstrap-wrapper Package Usage Examples")
    print("=" * 50)
    
    # Show current package info
    try:
        import bootstrap_wrapper
        print(f"📦 Version: {bootstrap_wrapper.__version__}")
    except ImportError:
        print("📦 Package not installed - use: pip install bootstrap-wrapper")
    
    # Show assets location
    bootstrap_path = get_bootstrap_assets()
    if bootstrap_path.exists():
        css_files = list(bootstrap_path.glob("css/*.min.css"))
        js_files = list(bootstrap_path.glob("js/*.min.js"))
        print(f"📂 Bootstrap assets: {bootstrap_path}")
        print(f"🎨 CSS files: {len(css_files)}")
        print(f"⚡ JS files: {len(js_files)}")
    
    print("\n🔧 Framework Integration Examples:")
    print("\n1. FastAPI:")
    print(fastapi_example())
    
    print("\n2. Django:")
    print(django_example())
    
    print("\n3. Flask:")
    print(flask_example())
    
    print("\n💡 Installation:")
    print("pip install bootstrap-wrapper==5.3.8")