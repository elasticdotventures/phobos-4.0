#!/usr/bin/env python3
"""Test script to debug the import issue"""

import sys
from pathlib import Path

# Add the build extension directory to path
ext_dir = Path(__file__).parent / "build" / "extension" / "elasticdotventures_phobos_4"
sys.path.insert(0, str(ext_dir))

print(f"Extension dir: {ext_dir}")
print(f"Extension dir exists: {ext_dir.exists()}")
print(f"Phobos subdir exists: {(ext_dir / 'phobos').exists()}")

# Try importing
print("\n" + "="*60)
print("Attempting import...")
print("="*60)

try:
    import phobos as phobos_module
    print(f"Import succeeded!")
    print(f"phobos_module = {phobos_module}")
    print(f"type = {type(phobos_module)}")
    print(f"Has __file__: {hasattr(phobos_module, '__file__')}")
    if hasattr(phobos_module, '__file__'):
        print(f"__file__ = {phobos_module.__file__}")
    print(f"Has register: {hasattr(phobos_module, 'register')}")
    print(f"Has bl_info: {hasattr(phobos_module, 'bl_info')}")
    if hasattr(phobos_module, 'bl_info'):
        print(f"bl_info = {phobos_module.bl_info}")
except Exception as e:
    print(f"Import failed: {type(e).__name__}: {e}")
    import traceback
    traceback.print_exc()
