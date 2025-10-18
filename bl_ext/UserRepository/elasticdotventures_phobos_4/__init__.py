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
    from . import phobos
except ImportError as e:
    if "scipy" in str(e) or "numpy" in str(e) or "yaml" in str(e):
        print("Phobos: Installing required dependencies...")
        if install_wheels():
            print("Phobos: Dependencies installed, please restart Blender to activate the addon.")
            # Try import again after install
            try:
                from . import phobos
            except ImportError:
                phobos = None
        else:
            print("Phobos: Failed to install dependencies")
            phobos = None
    else:
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
    global __addon_enabled__
    if phobos:
        phobos.register()
        __addon_enabled__ = True
    else:
        import bpy
        def draw(self, context):
            self.layout.label(text="Phobos dependencies installed. Please restart Blender to activate the addon.")
        bpy.context.window_manager.popup_menu(draw, title="Phobos: Restart Required")


def unregister() -> None:
    """Unregister the Phobos addon."""
    global __addon_enabled__
    if phobos:
        phobos.unregister()
    __addon_enabled__ = False


__all__ = ["bl_info", "register", "unregister", "__addon_enabled__"]
