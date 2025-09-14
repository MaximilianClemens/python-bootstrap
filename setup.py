#!/usr/bin/env python3
"""
Setup script for python-bootstrap
"""

from setuptools import setup, find_packages
from pathlib import Path

# Read version from bootstrap/version.txt
version_file = Path(__file__).parent / "bootstrap" / "version.txt"
if version_file.exists():
    with version_file.open(encoding="utf-8") as f:
        version_content = f.read().strip()
        # Remove 'v' prefix if present (e.g., v5.3.8 -> 5.3.8)
        version = version_content.lstrip('v')
else:
    version = "0.0.0"

# Read long description from README
readme_file = Path(__file__).parent / "README.md"
if readme_file.exists():
    with readme_file.open(encoding="utf-8") as f:
        long_description = f.read()
else:
    long_description = "A Python wrapper to distribute Bootstrap CSS/JS assets"

setup(
    name="python-bootstrap",
    version=version,
    description="A Python wrapper to distribute Bootstrap CSS/JS assets",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Maximilian Clemens",
    author_email="maximilian.clemens@gmail.com",
    url="https://github.com/MaximilianClemens/python-bootstrap",
    packages=find_packages(),
    package_data={
        "python_bootstrap": ["dist/**/*"],
    },
    include_package_data=True,
    python_requires=">=3.7",
    license="MIT",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    keywords=["bootstrap", "css", "javascript", "web", "frontend"],
)