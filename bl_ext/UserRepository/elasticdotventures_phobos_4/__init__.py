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
phobos = None
try:
    print("Phobos: Attempting to import phobos package...")
    from . import phobos
    print("Phobos: Successfully imported phobos package")
except ImportError as e:
    print(f"Phobos: Import error - {type(e).__name__}: {e}")
    if "scipy" in str(e) or "numpy" in str(e) or "yaml" in str(e):
        print("Phobos: Installing required dependencies...")
        if install_wheels():
            print("Phobos: Dependencies installed, please restart Blender to activate the addon.")
            # Try import again after install
            try:
                from . import phobos
                print("Phobos: Successfully imported after installing dependencies")
            except ImportError as e2:
                print(f"Phobos: Still failed after dependency install: {e2}")
                phobos = None
        else:
            print("Phobos: Failed to install dependencies")
            phobos = None
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

# Expose bl_info for Blender
bl_info = phobos.bl_info if phobos else {
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
    if phobos:
        print("Phobos: Calling phobos.register()...")
        try:
            phobos.register()
            __addon_enabled__ = True
            print("Phobos: Successfully registered!")
        except Exception as e:
            print(f"Phobos: Error during registration: {type(e).__name__}: {e}")
            import traceback
            traceback.print_exc()
            raise
    else:
        print("Phobos: phobos module is None - dependencies may need to be installed")
        print("Phobos: Please restart Blender to complete activation")
        # Note: Cannot show popup during extension loading as context is not available


def unregister() -> None:
    """Unregister the Phobos addon."""
    global __addon_enabled__
    if phobos:
        phobos.unregister()
    __addon_enabled__ = False


__all__ = ["bl_info", "register", "unregister", "__addon_enabled__"]
