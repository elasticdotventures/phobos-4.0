"""
Common utilities and definitions used throughout Phobos.

This subpackage contains shared functionality that was previously at the package root.
Moved here to comply with Blender 4.x extension policy which discourages top-level modules.
"""

from .commandline_logging import (
    setup_logger_level,
    get_logger,
    SUPPORTED_LEVELS,
    LOGGER_NAME,
    BASE_LOG_LEVEL,
    LOG_FILE_CONVENTION,
    ColoredFormatter,
)

from .defs import (
    EULER_CONVENTION,
    RPY_CONVENTION,
    MESH_TYPES,
    EXPORT_TYPES,
    IMPORT_TYPES,
    KINEMATIC_TYPES,
    SCENE_TYPES,
    HYRODYN_AVAILABLE,
    BPY_AVAILABLE,
    PYBULLET_AVAILABLE,
    YAML_AVAILABLE,
    check_pybullet_available,
    dump_json,
    dump_yaml,
    load_json,
)

__all__ = [
    # commandline_logging exports
    'setup_logger_level',
    'get_logger',
    'SUPPORTED_LEVELS',
    'LOGGER_NAME',
    'BASE_LOG_LEVEL',
    'LOG_FILE_CONVENTION',
    'ColoredFormatter',
    # defs exports
    'EULER_CONVENTION',
    'RPY_CONVENTION',
    'MESH_TYPES',
    'EXPORT_TYPES',
    'IMPORT_TYPES',
    'KINEMATIC_TYPES',
    'SCENE_TYPES',
    'HYRODYN_AVAILABLE',
    'BPY_AVAILABLE',
    'PYBULLET_AVAILABLE',
    'YAML_AVAILABLE',
    'check_pybullet_available',
    'dump_json',
    'dump_yaml',
    'load_json',
]
