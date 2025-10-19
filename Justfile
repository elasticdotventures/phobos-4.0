set shell := ["bash", "-lc"]

# Build Blender 4.x extension (default)
build: build-extension

# Build Blender extension archive
build-extension:
	python3 build_extension.py

# Clean build artifacts
clean:
	rm -rf build/ dist/ *.egg-info .uv-cache

# Install extension directly to Blender (requires BLENDER_EXTENSIONS_PATH)
install: build-extension
	@if [ -z "${BLENDER_EXTENSIONS_PATH}" ]; then \
		echo "Error: BLENDER_EXTENSIONS_PATH not set. Example:"; \
		echo "  export BLENDER_EXTENSIONS_PATH=\"\$$APPDATA/Blender Foundation/Blender/4.5/extensions/user_default\""; \
		exit 1; \
	fi
	@mkdir -p "${BLENDER_EXTENSIONS_PATH}"
	@echo "Installing to: ${BLENDER_EXTENSIONS_PATH}/phobos_4"
	@unzip -o dist/phobos_4.zip -d "${BLENDER_EXTENSIONS_PATH}"
	@echo "✓ Extension installed successfully!"
