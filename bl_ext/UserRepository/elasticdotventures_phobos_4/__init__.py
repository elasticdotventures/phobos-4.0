"""
Entry point module for the Phobos 4 Blender extension.

Blender maps installed extensions to the ``bl_ext.UserRepository.<id>`` namespace.
We simply forward registration to the legacy ``phobos`` package so existing code
paths continue to work unchanged.
"""

from importlib import import_module
from types import ModuleType

_phobos: ModuleType = import_module("phobos")

bl_info = getattr(_phobos, "bl_info", {})


def register() -> None:
    _phobos.register()


def unregister() -> None:
    _phobos.unregister()


__all__ = ["bl_info", "register", "unregister"]
