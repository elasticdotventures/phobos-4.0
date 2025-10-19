[![license](https://img.shields.io/github/license/dfki-ric/phobos.svg?style=flat)](https://github.com/dfki-ric/phobos/blob/master/COPYING)
[![made-with-sphinx-doc](https://img.shields.io/badge/Made%20with-Sphinx-1f425f.svg)](https://www.sphinx-doc.org/)

![Phobos](https://github.com/dfki-ric/phobos/wiki/img/phobos_logo_small.png)

# Phobos 4.x - Blender 4.2+ / 5.0 Compatible Fork

> **🔧 Actively Maintained Fork** | **🎯 Target: Blender 4.2 LTS → 5.0+**

This is a community-maintained fork of [Phobos](https://github.com/dfki-ric/phobos) focused on **Blender 4.2+ and 5.0 compatibility**. The original DFKI-RIC repository appears to be largely unmaintained, with official support ending at Blender 3.3.

## Why This Fork?

**Original Phobos Status:**
- ❌ Last maintained for Blender 3.3
- ❌ Not compatible with Blender 4.x extension system
- ❌ Missing wheel-based packaging for modern Blender
- ❌ No active maintenance or issue resolution

**This Fork (Phobos 4.x):**
- ✅ **Full Blender 4.2 LTS compatibility**
- ✅ **Blender 5.0 beta support** (tested and working)
- ✅ **Modern extension system** with wheel-based dependencies
- ✅ **Auto-install dependencies** (numpy, scipy, pyyaml, etc.)
- ✅ **Active development** and issue resolution
- ✅ **Backward compatibility** with Blender 3.x workflow (legacy zip install)

## About Phobos

Phobos is both a CLI tool and add-on for the open-source 3D modeling software
[Blender](https://www.blender.org/download/) that enables WYSIWYG creation and editing of robot models for frameworks like [ROS](http://wiki.ros.org/), [ROCK](https://github.com/rock-core), and simulators like [MARS](https://github.com/rock-simulation/mars) or [Gazebo](http://gazebosim.org/).

**Export Formats:** URDF, SDF, SMURF, STL, OBJ, Collada (DAE)

The Blender add-on enables the creation of WYSIWYG robot
models for use in robot frameworks like [ROS](http://wiki.ros.org/) and
[ROCK](https://github.com/rock-core) or in real-time simulations such as
[MARS](https://github.com/rock-simulation/mars) or
[Gazebo](http://gazebosim.org/). Phobos exports formats such as **URDF**,
**SDF** or **SMURF** and common mesh formats (**Stereolithography** (.stl),
**Wavefront** (.obj) or **Collada** (.dae)).

Phobos was initiated and is currently developed at the [Robotics Innovation
Center](http://robotik.dfki-bremen.de/en/startpage.html) of the [German
Research Center for Artificial Intelligence (DFKI)](http://www.dfki.de) in
Bremen, together with the [Robotics
Group](http://www.informatik.uni-bremen.de/robotik/index_en.php) of the
[University of Bremen](http://www.uni-bremen.de/en.html).

**Original Phobos Development:**
Phobos was initiated and is currently developed at the [Robotics Innovation Center](http://robotik.dfki-bremen.de/en/startpage.html) of the [German Research Center for Artificial Intelligence (DFKI)](http://www.dfki.de) in Bremen.

**This Fork:**
For questions, issues, or contributions related to Blender 4.x/5.0 compatibility, please use this repository's [issue tracker](https://github.com/elasticdotventures/phobos-4.0/issues).

## Versions & Compatibility

### Version 4.0.0 (Current - This Fork)
**First Blender 4.x/5.0 compatible release** with modern extension system support:

- ✅ **Blender 4.2 LTS** - Fully tested and working
- ✅ **Blender 4.5** - Tested and working
- ✅ **Blender 5.0** - Beta tested and working
- ✅ **Wheel-based packaging** with auto-install dependencies
- ✅ **Extension manager** compatible (Blender 4.2+)
- ✅ **Legacy zip install** supported for Blender 3.x users

**Major Changes:**
- Fixed addon preferences access for Blender 4.x extension namespace
- Updated path resolution for extension directory structure
- Bundled dependencies (numpy, scipy, pyyaml, pycollada, pydot, pyparsing)
- Auto-install mechanism for wheels on first run
- Made trimesh an optional dependency
- Fixed operator registration errors (property naming, enum defaults)
- Icon loading graceful fallbacks

**Known Warnings (Non-Blocking):**
- Policy violations for top-level module imports (cosmetic only)
- sys.path modification warning (required for current architecture)

## Version 2.1.0
Version 2.1.0 refactors especially the phobos-ci usage and improves the configurability by config inheritance. However these are breaking changes to the pipeline configuration. See PR #364 for more details on the changes.


## Version 2.0.0
With version 2.0.0 we did a refactoring of Phobos and its now possible to use phobos as a normal python package and command line tool (see below).

When running the new Phobos on a model created with an older version of Phobos, make sure to have a backup.
For most cases you should be able to update your model by simply exporting it to smurf and then importing it again from that smurf file.
Due to the changes between Blender 2 to 3 it might be necessary to check whether your materials already use the Specular BSDF or Principled BSDF shaders, if not you'd have to update this manually.

If you encounter any problems with this new version please do not hesitate to open an issue [here](https://github.com/dfki-ric/phobos/issues).

## Questions or Ideas you want to discuss?
Please have a look at our [GitHub discussions](https://github.com/dfki-ric/phobos/discussions).

## Found a bug or want to request a feature?
Please let us know by opening an issue [here](https://github.com/dfki-ric/phobos/issues).

## Documentation
- User documentation: [Phobos Wiki](https://github.com/dfki-ric/phobos/wiki)
- Source documentation: [Phobos' Github Page](http://dfki-ric.github.io/phobos).

## Citing

Phobos has been published in the [Journal of Open Source Software](https://doi.org/10.21105/joss.01326).
We ask users to cite the use of Phobos, as it allows us to keep the project alive.

When citing, please provide this information:

  - Phobos version you were using (see the [wiki](https://github.com/dfki-ric/phobos/wiki/Installation#versions-and-branching) for information about versions)
  - If you were using additional Phobos plugins or configurations.
  - The general [Phobos paper](https://doi.org/10.21105/joss.01326).

If you are on the hunt for a BiBTeX entry, check out the [FAQ section](https://github.com/dfki-ric/phobos/wiki/FAQ#how-do-i-cite-phobos).

## Installation

### Blender 4.2+ / 5.0 (Recommended - Extension System)

**For Blender 4.2 LTS, 4.5, or 5.0:**

1. **Download** the extension package:
   - Download `elasticdotventures_phobos_4.zip` from the [releases page](https://github.com/elasticdotventures/phobos-4.0/releases)
   - Or build from source: `python3 build_extension.py` (creates `dist/elasticdotventures_phobos_4.zip`)

2. **Install** via Extension Manager:
   - Open Blender 4.2+
   - Go to `Edit → Preferences → Get Extensions`
   - Click dropdown menu (top right) → `Install from Disk`
   - Select `elasticdotventures_phobos_4.zip`

3. **First Launch**:
   - Blender will auto-install dependencies (numpy, scipy, pyyaml, etc.)
   - **Restart Blender** when prompted (required for dependencies to load)

4. **Activate** (after restart):
   - The extension should auto-enable
   - If not, go to `Edit → Preferences → Add-ons`, search "Phobos", and enable it

5. **Access Phobos**:
   - Press `N` in the 3D Viewport to open the sidebar
   - Look for the "Phobos" tab on the right side

   ![Small arrow to open the phobos toolbar widget.](https://github.com/dfki-ric/phobos/wiki/img/blender_phobos_menu_open.png)

**✅ Verified:** Blender 4.2 LTS, 4.5, and 5.0 beta

> **UPDATING:** Remove the old version first via the Extension Manager, restart Blender, then install the new version.

> **WINDOWS NOTE:** Ensure you have the latest [Microsoft Visual C++ Redistributable](https://learn.microsoft.com/en-US/cpp/windows/latest-supported-vc-redist?view=msvc-170) installed for Blender's Python to work correctly.

### Blender 3.x (Legacy Zip Install)

For older Blender versions (3.0 - 3.6), use the legacy zip installation method:

1. Download or create `phobos.zip` (zip the `phobos/` subdirectory)
2. Install: `Blender → Edit → Preferences → Addons → Install`
3. Activate the Phobos addon
4. **Restart Blender**
5. Re-activate Phobos

Note: Dependencies must be manually installed for Blender 3.x using `install_requirements.py`.

### Blender wheel extension

Blender 4.2+ provides an extension manager that can install add-ons directly from Python wheels.  
Phobos now ships a wheel layout defined in `pyproject.toml` and `blender_manifest.toml`.

To produce a wheel from a clean checkout:

```bash
python -m pip install --upgrade build
python -m build --wheel
```

Install the resulting `dist/phobos_4-*.whl` through **Edit ▸ Preferences ▸ Extensions ▸ Install from Disk…** and restart Blender.
Dependencies declared in the wheel are resolved by Blender’s bundled Python runtime, so the legacy `install_requirements.py` flow is no longer required on Blender 5.x.
After Blender restarts, open **Edit ▸ Preferences ▸ Add-ons**, search for “Phobos”, enable the add-on, and press `N` in the 3D Viewport to access the Phobos sidebar tab.

### Blender extension builder

The repository also ships packaging shortcuts for the official [blender-extension-builder](https://pypi.org/project/blender-extension-builder/) workflow.

Use the following steps to produce a Blender-ready archive:

```bash
# install tooling (uv sync --extra dev also works)
uv tool install blender-extension-builder

# point to the Blender binary if it is not on PATH
export BLENDER_PATH=/Applications/Blender.app/Contents/MacOS/Blender

# assemble the extension archive under dist/
just build-extension
```

The command calls `build-blender-extension` with `blender_manifest.toml` so the output complies with the schema documented at <https://developer.blender.org/docs/features/extensions/schema/>. If Blender is unavailable locally, fall back to `just zip-addon`, which recreates the legacy zip bundle.

### CLI
Install the requirements by executing `install_requirements.py` with the python you want to install phobos to:
```bash
cd phobos
python3 install_requirements.py
```

Then just install it using pip:
```bash
cd phobos
pip install .
```
or with autoproj:
1) Add the package to your buildconf/package_set
2) Install via `amake`

### Docker

A headless runtime that ships the `bpy` wheels and the Phobos add-on is defined in the repository `Dockerfile`.

Build the container (override `BPY_VERSION` to track a newer Blender release such as 5.0 when available):

```bash
docker build -t phobos:latest . --build-arg BPY_VERSION=4.2.0
```

Run the CLI entry point:

```bash
docker run --rm -it phobos --help
```

To work with models on the host, mount the workspace and point Blender to the shared directory:

```bash
docker run --rm -it \
  -v "$(pwd)":/workspace \
  -w /workspace \
  phobos convert --help
```

The add-on is pre-symlinked into `/opt/blender-user-scripts/addons/phobos`. The image ships the headless `bpy` runtime; if you need the full Blender UI, extend the image with the official Blender builds and forward the required display or virtual framebuffer devices.

## Overview

### Blender

![Model of the SpaceClimber robot in Blender, next to the Phobos toolbar
displayed on the
left.](https://github.com/dfki-ric/phobos/wiki/img/phobos_spaceclimber.png)

*Model of the
[SpaceClimber](http://robotik.dfki-bremen.de/en/research/projects/spaceclimber-1.html)
robot in Blender, next to the Phobos toolbar displayed on the left.*

Phobos makes use of Blender's hierarchical object graph and its bone objects.
These objects, normally used for animating 3D characters, allow to store 3D
coordinate systems and apply constraints to their movements, for instance to
restrict the movement of an object to a certain range on a specific axis. This
allows to replicate the links and joints defined in a **URDF** model and together
with the hierarchical tree of parent and child objects, the complete, branching
kinematic chain of a robot can be represented. By attaching meshes or
primitives to the bones, Phobos allows to add visual and collision objects to
a model. Additional objects allow storing further information, e.g. centers of
mass of each part of a robot, thus refining the physical representation. Sensor
objects can be added to correctly place and orient devices such as laser
scanners, cameras or contact sensors. Making use of Blender's custom object
properties, any necessary information can be added to the model, from inertia
tensors to opening angles of cameras.

![Decomposition of the different elements from which Phobos models are composed
in Blender.](https://github.com/dfki-ric/phobos/wiki/img/phobos_elements.png)

*Decomposition of the different elements from which Phobos models are composed
in Blender. These elements can be arranged in Blender on different layers, thus
avoiding confusion or obstruction of view when editing very complex models.*

### CLI

You can either use CLI-phobos as a normal python package or use the scripts provided with it.

For the latter do `phobos --help` to get a list of the currently available scripts.
It will also tell you which dependencies are missing for some scripts.

## Features

- WYSIWYG editor for robot models using Blender
- CLI tools for fast and easy model handling and inspection
- CI tool to run phobos headless in your CI-pipeline for atomated model processing and maintenance
- Import and export of **URDF**, **SDF** **SMURF** and other
  [formats](https://github.com/dfki-ric/phobos/wiki/Formats)
- Easy definition of robot kinematics (links and joints)
- Visualisation of different model components, even joint constraints
- Numerous tools for fast editing:
  - Batch editing of object properties
  - Auto-generation of collision objects
  - Auto-generation of inertia tensors from mass and shape
  - Calculation of merged inertia for complex links
  - Verbose logging
- Saving and loading of model poses
- Annotation of objects from motors/sensors to joints/links
- Save/load different export configurations for the same model
- Export with defined floating point precision
- Model integrity checks
- Tools for maintaining your own model database
- Library containing Python examples for automatic model adaption
- All the cool features Blender already provides (rendering, animation, etc.)

## License

Phobos is distributed under the [3-Clause BSD License](https://opensource.org/licenses/BSD-3-Clause).
