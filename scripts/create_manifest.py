from datasets import load_dataset
import csv
import os

OUTPUT = "data/raw/plantvillage_manifest.csv"

print("=" * 60)
print("AgriShield - PlantVillage Manifest")
print("=" * 60)

print("\nLoading PlantVillage...")

ds = load_dataset("mohanty/PlantVillage", "default")

rows = []

for split in ["train", "test"]:

    print(f"Processing {split}...")

    for path in ds[split]["text"]:

        path = path.replace("\\", "/")

        parts = path.split("/")

        if len(parts) < 4:
            continue

        class_name = parts[2]
        filename = parts[-1]

        rows.append({
            "source": "PlantVillage",
            "original_split": split,
            "class_name": class_name,
            "relative_path": path,
            "filename": filename
        })


os.makedirs("data/raw", exist_ok=True)

with open(OUTPUT, "w", newline="", encoding="utf-8") as f:

    writer = csv.DictWriter(
        f,
        fieldnames=[
            "source",
            "original_split",
            "class_name",
            "relative_path",
            "filename"
        ]
    )

    writer.writeheader()
    writer.writerows(rows)

print("\nManifest created:")
print(OUTPUT)

print("Total rows:", len(rows))

print("\nFirst 5 entries:")

for row in rows[:5]:
    print(row)

print("\nDone.")
