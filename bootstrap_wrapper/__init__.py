"""
Python Bootstrap - A wrapper to distribute Bootstrap CSS/JS assets via Python packaging

This package provides easy access to Bootstrap's compiled CSS and JavaScript files
through Python's packaging system.
"""

from pathlib import Path

try:
    # Get version from bootstrap/version.txt
    version_file = Path(__file__).parent.parent / "bootstrap" / "version.txt"
    if version_file.exists():
        with version_file.open(encoding="utf-8") as f:
            version_content = f.read().strip()
            # Remove 'v' prefix if present (e.g., v5.3.8 -> 5.3.8)
            __version__ = version_content.lstrip('v')
    else:
        __version__ = "0.0.0"
except Exception:  # pylint: disable=broad-exception-caught
    __version__ = "0.0.0"


def get_bootstrap_dir():
    """
    Get the path to the Bootstrap assets directory.
    
    Returns:
        Path: Path to the bootstrap directory containing CSS and JS files
    """
    return Path(__file__).parent.parent / "bootstrap"


def get_bootstrap_css_dir():
    """
    Get the path to the Bootstrap CSS directory.
    
    Returns:
        Path: Path to the bootstrap/css directory
    """
    return get_bootstrap_dir() / "css"


def get_bootstrap_js_dir():
    """
    Get the path to the Bootstrap JS directory.
    
    Returns:
        Path: Path to the bootstrap/js directory
    """
    return get_bootstrap_dir() / "js"


__all__ = ["__version__", "get_bootstrap_dir", "get_bootstrap_css_dir", "get_bootstrap_js_dir"]