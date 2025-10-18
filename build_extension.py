#!/usr/bin/env python3
"""
Build script for Phobos 4 Blender extension.

This script packages Phobos as a Blender 4.x extension by:
1. Creating the proper extension directory structure
2. Copying the phobos package into the extension directory
3. Downloading required Python wheels
4. Creating a zip file for distribution
"""

import shutil
import zipfile
import urllib.request
from pathlib import Path


def build_extension():
    """Build the Blender extension package."""

    # Define paths
    root_dir = Path(__file__).parent
    build_dir = root_dir / "build" / "extension"
    dist_dir = root_dir / "dist"
    extension_id = "elasticdotventures_phobos_4"
    extension_dir = build_dir / extension_id

    print(f"Building Phobos 4 Blender extension...")
    print(f"Root directory: {root_dir}")
    print(f"Build directory: {build_dir}")
    print(f"Extension directory: {extension_dir}")

    # Clean build directory
    if build_dir.exists():
        print(f"Cleaning build directory: {build_dir}")
        shutil.rmtree(build_dir)

    # Create build directory structure
    extension_dir.mkdir(parents=True, exist_ok=True)
    dist_dir.mkdir(parents=True, exist_ok=True)

    # Copy the extension entry point
    print("Copying extension entry point...")
    entry_point_src = root_dir / "bl_ext" / "UserRepository" / extension_id / "__init__.py"
    entry_point_dst = extension_dir / "__init__.py"
    shutil.copy2(entry_point_src, entry_point_dst)

    # Copy the phobos package
    print("Copying phobos package...")
    phobos_src = root_dir / "phobos"
    phobos_dst = extension_dir / "phobos"

    def ignore_patterns(dir, files):
        """Filter out files we don't want to copy."""
        ignored = []
        for f in files:
            if f == '__pycache__' or f.endswith('.pyc') or f.endswith('.pyo'):
                ignored.append(f)
        return ignored

    shutil.copytree(phobos_src, phobos_dst, ignore=ignore_patterns)

    # Download Python wheels for dependencies using pip
    print("Downloading Python wheels...")
    wheels_dir = extension_dir / "wheels"
    wheels_dir.mkdir(exist_ok=True)

    dependencies = ["numpy", "scipy", "pyyaml", "pycollada", "pydot", "pyparsing"]

    import subprocess
    import sys

    for dep in dependencies:
        print(f"  Downloading {dep} wheel...")
        try:
            subprocess.check_call([
                sys.executable, "-m", "pip", "download",
                "--only-binary", ":all:",
                "--dest", str(wheels_dir),
                "--platform", "win_amd64",
                "--python-version", "311",
                "--no-deps",
                dep
            ], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        except subprocess.CalledProcessError as e:
            print(f"  Warning: Failed to download {dep}: {e}")

    # Copy manifest
    print("Copying blender_manifest.toml...")
    shutil.copy2(root_dir / "blender_manifest.toml", extension_dir / "blender_manifest.toml")

    # Copy documentation files
    print("Copying documentation files...")
    for doc_file in ["README.md", "LICENSE"]:
        src = root_dir / doc_file
        if src.exists():
            shutil.copy2(src, extension_dir / doc_file)

    # Create zip file for distribution
    zip_path = dist_dir / f"{extension_id}.zip"
    print(f"Creating zip file: {zip_path}")

    with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for file_path in extension_dir.rglob('*'):
            if file_path.is_file():
                arcname = file_path.relative_to(build_dir)
                zipf.write(file_path, arcname)

    print(f"\n{'='*60}")
    print(f"Extension built successfully!")
    print(f"{'='*60}")
    print(f"Extension directory: {extension_dir}")
    print(f"Zip file: {zip_path}")
    print(f"\nTo install in Blender:")
    print(f"1. Open Blender 4.2+")
    print(f"2. Go to Edit > Preferences > Get Extensions")
    print(f"3. Click the dropdown menu (top right) > Install from Disk")
    print(f"4. Select: {zip_path}")
    print(f"\nAlternatively, extract to:")
    print(f"  Windows: %APPDATA%\\Blender Foundation\\Blender\\4.x\\extensions\\user_default\\")
    print(f"  macOS: ~/Library/Application Support/Blender/4.x/extensions/user_default/")
    print(f"  Linux: ~/.config/blender/4.x/extensions/user_default/")

    return zip_path


if __name__ == "__main__":
    build_extension()
