from pathlib import Path
from collections import Counter

ROOT = Path("data/raw/plantdoc")

print("=" * 60)
print("AGRISHIELD - PLANTDOC INSPECTION")
print("=" * 60)

if not ROOT.exists():
    print("ERROR: PlantDoc folder not found.")
    raise SystemExit

extensions = {".jpg", ".jpeg", ".png", ".JPG", ".JPEG", ".PNG"}

all_images = []

for file in ROOT.rglob("*"):
    if file.is_file() and file.suffix in extensions:
        all_images.append(file)

print("\nTotal image files:", len(all_images))

folder_counts = Counter()

for image in all_images:
    relative = image.relative_to(ROOT)

    if len(relative.parts) >= 2:
        folder = relative.parts[0]
        folder_counts[folder] += 1

print("\nFolders containing images:")

for folder, count in sorted(folder_counts.items()):
    print(f"{folder:<30} {count}")

print("\nSample files:")

for image in all_images[:20]:
    print(image)

print("\n" + "=" * 60)
print("INSPECTION COMPLETE")
print("=" * 60)
