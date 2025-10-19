# GitHub Actions Workflows

This directory contains automated CI/CD workflows for the Phobos 4.x extension.

## Workflows

### 1. Build Extension (`build-extension.yml`)

**Triggers:**
- Push to `main` branch
- Push of version tags (`v*`)
- Pull requests to `main`
- Manual workflow dispatch

**What it does:**
- Builds the `phobos_4.zip` extension
- Uploads build artifacts (30-day retention)
- Creates GitHub releases for version tags
- Generates release notes and checksums

**Artifacts:**
- `phobos-4-extension` - The built extension zip file
- `build-info` - Build metadata and information

### 2. Test Build (`test-build.yml`)

**Triggers:**
- Pull requests to `main`
- Manual workflow dispatch

**What it does:**
- Tests the build process across multiple platforms
- Validates extension structure
- Ensures Python compatibility

**Test Matrix:**
- **OS**: Ubuntu, Windows, macOS
- **Python**: 3.10, 3.11, 3.12

**Artifacts:**
- Test builds for each OS/Python combination (7-day retention)

### 3. Release (`release.yml`)

**Triggers:**
- Push of semantic version tags (`v*.*.*`)

**What it does:**
- Builds the extension from tagged commit
- Generates comprehensive release notes
- Creates SHA256 checksums
- Publishes GitHub release with assets
- Marks pre-releases (alpha/beta/rc) appropriately

**Release Assets:**
- `phobos_4.zip` - The extension package
- `phobos_4.zip.sha256` - Checksum file

## Creating a Release

### Manual Release Process

1. **Update version** (if needed in any version files)

2. **Create and push a tag:**
   ```bash
   git tag -a v1.0.0 -m "Release version 1.0.0"
   git push origin v1.0.0
   ```

3. **Wait for workflow:**
   - GitHub Actions will automatically build and create the release
   - Check the Actions tab for progress

4. **Release is ready!**
   - Navigate to Releases to see the new release
   - Download links and release notes are automatically generated

### Version Tag Format

Use semantic versioning:
- `v1.0.0` - Major release
- `v1.1.0` - Minor release (new features)
- `v1.0.1` - Patch release (bug fixes)
- `v1.0.0-alpha.1` - Pre-release (marked as pre-release)
- `v1.0.0-beta.1` - Beta release (marked as pre-release)
- `v1.0.0-rc.1` - Release candidate (marked as pre-release)

### Pre-releases

Tags containing `alpha`, `beta`, or `rc` are automatically marked as pre-releases on GitHub.

## Workflow Permissions

The workflows require the following permissions:
- `contents: write` - For creating releases and uploading assets

These are automatically granted through `GITHUB_TOKEN`.

## Local Testing

To test the build process locally:

```bash
# Build the extension
python build_extension.py

# Verify the output
ls -lh dist/phobos_4.zip
```

## Troubleshooting

### Build Fails

1. Check Python version (requires 3.10+)
2. Ensure `build_extension.py` is executable
3. Check for missing dependencies in requirements

### Release Not Created

1. Verify tag format matches `v*.*.*`
2. Check GitHub Actions logs
3. Ensure `GITHUB_TOKEN` has write permissions

### Artifacts Not Available

1. Check retention period (30 days for builds, 7 days for tests)
2. Verify workflow completed successfully
3. Check artifact upload step in workflow logs

## Security

- All workflows use pinned action versions for security
- `GITHUB_TOKEN` is scoped to minimum required permissions
- No external secrets required for building/releasing

## Maintenance

When updating workflows:
1. Test changes in a fork first
2. Use `workflow_dispatch` to trigger manually
3. Monitor the Actions tab for any issues
4. Update this README if workflow behavior changes
