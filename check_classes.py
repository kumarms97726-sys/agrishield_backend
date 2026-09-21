from datasets import load_dataset
from collections import Counter

print("Loading PlantVillage...")

ds = load_dataset("mohanty/PlantVillage", "default")

classes = Counter()

for split in ["train", "test"]:
    print(f"Reading {split}...")

    for path in ds[split]["text"]:
        parts = path.replace("\\", "/").split("/")

        # Example:
        # raw/color/Raspberry___healthy/image.JPG
        if len(parts) >= 4:
            class_name = parts[2]
            classes[class_name] += 1

print("\n================================")
print("PLANTVILLAGE DATASET REPORT")
print("================================")

print("Total records:", sum(classes.values()))
print("Number of classes:", len(classes))

print("\nClasses:")
print("--------------------------------")

for name, count in sorted(classes.items()):
    print(f"{name:<55} {count}")

print("--------------------------------")
print("Done.")