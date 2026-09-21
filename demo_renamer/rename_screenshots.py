import csv
import shutil
from pathlib import Path


def rename_screenshots() -> None:
    """Read mapping.csv and rename screenshot files to output folder."""
    input_dir = Path("input")
    screenshots_dir = input_dir / "screenshots"
    output_dir = Path("output")
    mapping_file = input_dir / "mapping.csv"

    output_dir.mkdir(exist_ok=True)

    with open(mapping_file, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            old_name = row["old_name"].strip()
            new_name = row["new_name"].strip()

            old_path = screenshots_dir / old_name
            new_path = output_dir / new_name

            if old_path.exists():
                shutil.copy2(old_path, new_path)
                print(f"✓ Renamed: {old_name} → {new_name}")
            else:
                print(f"✗ File not found: {old_name}")


if __name__ == "__main__":
    rename_screenshots()
