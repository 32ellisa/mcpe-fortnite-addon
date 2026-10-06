import os
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent
OUTPUT = ROOT / "fortnite-inspired-battle-royale.mcaddon"
BEHAVIOR = ROOT / "behavior_pack"
RESOURCE = ROOT / "resource_pack"


def add_folder(zf, folder: Path, prefix: str = ""):
    for child in sorted(folder.iterdir()):
        arcname = f"{prefix}{child.name}"
        if child.is_dir():
            add_folder(zf, child, arcname + "/")
        else:
            zf.write(child, arcname)


def main():
    if not BEHAVIOR.exists() or not RESOURCE.exists():
        raise FileNotFoundError("behavior_pack and resource_pack are required before packaging.")

    with zipfile.ZipFile(OUTPUT, "w", compression=zipfile.ZIP_DEFLATED) as zf:
        add_folder(zf, BEHAVIOR, "behavior_pack/")
        add_folder(zf, RESOURCE, "resource_pack/")

    print(f"Created {OUTPUT.name}")


if __name__ == "__main__":
    main()
