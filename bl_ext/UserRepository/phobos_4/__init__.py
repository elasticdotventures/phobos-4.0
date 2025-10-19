"""
Entry point module for the Phobos 4 Blender extension.

Blender maps installed extensions to the ``bl_ext.UserRepository.<id>`` namespace.
We simply forward registration to the legacy ``phobos`` package so existing code
paths continue to work unchanged.
"""

import sys
import subprocess
from pathlib import Path

# Required by Blender 4.x extensions
__addon_enabled__ = False

# Extension directory for finding wheels
_extension_dir = Path(__file__).parent


def install_wheels():
    """Install wheel dependencies bundled with the extension."""
    wheels_dir = _extension_dir / "wheels"
    if not wheels_dir.exists():
        return False

    installed_any = False
    for wheel_file in wheels_dir.glob("*.whl"):
        try:
            print(f"Installing {wheel_file.name}...")
            subprocess.check_call([
                sys.executable, "-m", "pip", "install",
                "--no-deps",  # Don't install dependencies of dependencies
                str(wheel_file)
            ], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            installed_any = True
        except subprocess.CalledProcessError as e:
            print(f"Warning: Failed to install {wheel_file.name}: {e}")

    return installed_any


# Try to import phobos using relative import (no sys.path modification needed)
print("="*70)
print("PHOBOS LOADER v2.3 - FIXED MODULE SHADOWING BUG")
print("="*70)

# Clear any cached phobos modules from previous installations
print("Phobos: Clearing module cache...")
import sys as _sys
_module_prefix = __name__ + ".phobos"
_cached_modules = [key for key in _sys.modules.keys() if key.startswith(_module_prefix)]
for _mod_name in _cached_modules:
    print(f"Phobos: Removing cached module: {_mod_name}")
    del _sys.modules[_mod_name]
print(f"Phobos: Cleared {len(_cached_modules)} cached modules")

# Use different variable name to avoid any shadowing issues
_phobos_module = None
try:
    print("Phobos: Attempting to import phobos package...")
    from . import phobos as _phobos_module
    print(f"Phobos: Import statement completed without exception")
    print(f"Phobos: _phobos_module variable = {_phobos_module}")
    print(f"Phobos: type(_phobos_module) = {type(_phobos_module)}")
    if _phobos_module:
        print(f"Phobos: Module file: {getattr(_phobos_module, '__file__', 'NO __file__')}")
        print(f"Phobos: Has register: {hasattr(_phobos_module, 'register')}")
        print(f"Phobos: Has bl_info: {hasattr(_phobos_module, 'bl_info')}")
except ImportError as e:
    print(f"Phobos: Import error - {type(e).__name__}: {e}")
    print(f"Phobos: Full error: {repr(e)}")
    import traceback
    print("Phobos: Full traceback:")
    traceback.print_exc()
    if "scipy" in str(e) or "numpy" in str(e) or "yaml" in str(e):
        print("Phobos: Installing required dependencies...")
        if install_wheels():
            print("Phobos: Dependencies installed, please restart Blender to activate the addon.")
            # Try import again after install
            try:
                from . import phobos as _phobos_module
                print(f"Phobos: Successfully imported after installing dependencies")
            except ImportError as e2:
                print(f"Phobos: Still failed after dependency install: {e2}")
                _phobos_module = None
        else:
            print("Phobos: Failed to install dependencies")
            _phobos_module = None
    else:
        print(f"Phobos: Unexpected import error, re-raising: {e}")
        import traceback
        traceback.print_exc()
        raise
except Exception as e:
    print(f"Phobos: Unexpected exception during import: {type(e).__name__}: {e}")
    import traceback
    traceback.print_exc()
    raise

print(f"Phobos: After import attempts, _phobos_module = {_phobos_module}")

# Expose bl_info for Blender
bl_info = _phobos_module.bl_info if _phobos_module else {
    "name": "Phobos 4",
    "description": "Installing dependencies... Please restart Blender.",
    "author": "DFKI RIC",
    "version": (4, 0, 0),
    "blender": (4, 2, 0),
    "category": "Development",
}


def register() -> None:
    """Register the Phobos addon."""
    print("Phobos: register() called")
    global __addon_enabled__
    if _phobos_module:
        print(f"Phobos: Calling _phobos_module.register() (module={_phobos_module})...")
        try:
            _phobos_module.register()
            __addon_enabled__ = True
            print("Phobos: Successfully registered!")
        except Exception as e:
            print(f"Phobos: Error during registration: {type(e).__name__}: {e}")
            import traceback
            traceback.print_exc()
            raise
    else:
        print("Phobos: _phobos_module is None - dependencies may need to be installed")
        print("Phobos: Please restart Blender to complete activation")
        # Note: Cannot show popup during extension loading as context is not available


def unregister() -> None:
    """Unregister the Phobos addon."""
    global __addon_enabled__
    if _phobos_module:
        _phobos_module.unregister()
    __addon_enabled__ = False


__all__ = ["bl_info", "register", "unregister", "__addon_enabled__"]
