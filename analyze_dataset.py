from datasets import load_dataset
from collections import Counter

print("=" * 60)
print("AGRISHIELD - PLANTVILLAGE DATASET ANALYSIS")
print("=" * 60)

print("\nLoading dataset...")
ds = load_dataset("mohanty/PlantVillage", "default")

all_paths = []
split_paths = {}

for split in ["train", "test"]:
    paths = list(ds[split]["text"])
    split_paths[split] = paths
    all_paths.extend(paths)

    print(f"\n{split.upper()} RECORDS: {len(paths)}")
    print(f"{split.upper()} UNIQUE PATHS: {len(set(paths))}")

# ---------------------------------------------------------
# 1. Overall duplicates
# ---------------------------------------------------------

unique_paths = set(all_paths)

print("\n" + "=" * 60)
print("DUPLICATE ANALYSIS")
print("=" * 60)

print("Total records       :", len(all_paths))
print("Unique image paths  :", len(unique_paths))
print("Duplicate records   :", len(all_paths) - len(unique_paths))

# ---------------------------------------------------------
# 2. Train/Test overlap
# ---------------------------------------------------------

train_set = set(split_paths["train"])
test_set = set(split_paths["test"])

overlap = train_set.intersection(test_set)

print("\n" + "=" * 60)
print("TRAIN / TEST OVERLAP")
print("=" * 60)

print("Train unique images :", len(train_set))
print("Test unique images  :", len(test_set))
print("Exact path overlap  :", len(overlap))

if len(overlap) == 0:
    print("GOOD: No exact path overlap.")
else:
    print("WARNING: Duplicate paths exist in train and test!")

# ---------------------------------------------------------
# 3. Class counts using unique paths
# ---------------------------------------------------------

class_paths = {}

for path in unique_paths:

    parts = path.replace("\\", "/").split("/")

    if len(parts) >= 4:
        class_name = parts[2]

        if class_name not in class_paths:
            class_paths[class_name] = set()

        class_paths[class_name].add(path)

print("\n" + "=" * 60)
print("UNIQUE IMAGE COUNT BY CLASS")
print("=" * 60)

for class_name, paths in sorted(class_paths.items()):
    print(f"{class_name:<55} {len(paths)}")

# ---------------------------------------------------------
# 4. Class imbalance
# ---------------------------------------------------------

counts = [len(paths) for paths in class_paths.values()]

print("\n" + "=" * 60)
print("CLASS BALANCE")
print("=" * 60)

print("Number of classes :", len(counts))
print("Smallest class    :", min(counts))
print("Largest class     :", max(counts))
print("Imbalance ratio   :", round(max(counts) / min(counts), 2))

smallest = sorted(
    [(len(paths), name) for name, paths in class_paths.items()]
)

largest = sorted(
    [(len(paths), name) for name, paths in class_paths.items()],
    reverse=True
)

print("\nSMALLEST 5 CLASSES:")
for count, name in smallest[:5]:
    print(f"{count:6}  {name}")

print("\nLARGEST 5 CLASSES:")
for count, name in largest[:5]:
    print(f"{count:6}  {name}")

print("\n" + "=" * 60)
print("ANALYSIS COMPLETE")
print("=" * 60)