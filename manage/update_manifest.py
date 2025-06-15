"""Update the manifest file."""
# https://github.com/hacs/integration/blob/main/manage/update_manifest.py
import json
import os
import sys
from pathlib import Path


def update_manifest():
    """Update the manifest file."""
    version = "0.0.0"
    for index, value in enumerate(sys.argv):
        if value in ["--version", "-V"]:
            version = sys.argv[index + 1]

    # Get the root directory of the project
    root_dir = Path(__file__).parent.parent
    manifest_path = root_dir / "custom_components" / "ocpp" / "manifest.json"

    if not manifest_path.exists():
        print(f"Error: manifest.json not found at {manifest_path}")
        sys.exit(1)

    with open(manifest_path) as manifestfile:
        manifest = json.load(manifestfile)

    manifest["version"] = version

    with open(manifest_path, "w") as manifestfile:
        manifestfile.write(json.dumps(manifest, indent=4, sort_keys=True))


update_manifest()
