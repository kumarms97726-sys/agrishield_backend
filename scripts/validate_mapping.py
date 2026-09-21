from pathlib import Path
import csv

PLANTDOC_DIR = Path("data/raw/plantdoc")
MAPPING_FILE = Path("scripts/plantdoc_mapping.csv")

mapping = {}

with open(MAPPING_FILE, "r", encoding="utf-8-sig") as f:
    reader = csv.DictReader(f)
    for row in reader:
        mapping[row["plantdoc_class"]] = row["agrishield_class"]

folders = sorted(
    p.name for p in PLANTDOC_DIR.iterdir()
    if p.is_dir()
)

print("=" * 60)
print("AGRISHIELD - PLANTDOC MAPPING VALIDATION")
print("=" * 60)

print("PlantDoc folders:", len(folders))
print("Mapped folders:", len(mapping))

missing = [folder for folder in folders if folder not in mapping]

if missing:
    print("\nMISSING MAPPINGS:")
    for name in missing:
        print("  -", name)
else:
    print("\nEvery PlantDoc class has a mapping.")

print("\nAgriShield destination classes:",
      len(set(mapping.values())))

if not missing:
    print("\nMAPPING VALIDATION PASSED")
else:
    print("\nMAPPING NEEDS FIXING")