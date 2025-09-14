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

__all__ = ["__version__"]