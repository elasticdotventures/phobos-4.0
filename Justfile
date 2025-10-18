set shell := ["bash", "-lc"]

cache_dir := ".uv-cache"

# Prepare uv-managed environment
sync:
	uv sync --extra dev

# Build wheel artifact into dist/
build-wheel:
	UV_CACHE_DIR={{cache_dir}} uv run python -m build --wheel

# Package add-on zip for legacy installer
zip-addon:
	mkdir -p dist
	rm -f dist/phobos-addon.zip
	zip -r dist/phobos-addon.zip phobos bl_ext blender_manifest.toml

# Build Blender extension archive using blender-extension-builder
build-extension:
	if [ -n "${BLENDER_PATH:-}" ]; then \
		PATH="$$(dirname "$$BLENDER_PATH"):$${PATH}" build-blender-extension -m blender_manifest.toml -d dist; \
	elif command -v blender >/dev/null 2>&1; then \
		build-blender-extension -m blender_manifest.toml -d dist; \
	else \
		echo "Blender executable not found. Set BLENDER_PATH or add blender to PATH." >&2; \
		exit 1; \
	fi
