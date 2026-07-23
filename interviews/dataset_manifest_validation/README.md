# Dataset Manifest Validation

You're working on the backend of an ML platform that trains pathology models. Each training dataset consists of many image files. Before training starts, the platform validates the dataset manifest to detect inconsistencies. You're given a list of records. Each record is a dictionary with this structure:

```json
{
    "image_id": "img_001",
    "patient_id": "patient_17",
    "split": "train",      # one of: train, validation, test
}
```

---
## Task

Your task is to implement:

```python
def validate_manifest(records: list[dict]) -> dict:
    ...
```

and return a dictionary with the following structure:

```python
{
    "duplicate_images": set[str],
    "patients_in_multiple_splits": dict[str, set[str]],
    "split_counts": dict[str, int],
}
```

## Requirements

1. **Duplicate image IDs:** If the same `image_id` appears more than once anywhere in the manifest, include it in `duplicate_images`. Each duplicate image ID should appear only once in the returned set.
2. **Patients appearing in multiple splits:** Each patient is expected to belong to exactly one split. If a patient appears in more than one split, include them in `patients_in_multiple_splits`. Example:

```json
{
    "patient_5": {"train", "validation"},
    "patient_8": {"train", "test"},
}
```

Patients that appear in only one split should not be included.

3. **Split counts:** Return the total number of records in each split. Example:

```json
{
    "train": 120,
    "validation": 18,
    "test": 25,
}
```

If a split has zero records, it should still appear with a count of `0`. You may assume only the three valid split names exist.

## Input

Example:

```python
records = [
    {"image_id": "img1", "patient_id": "p1", "split": "train"},
    {"image_id": "img2", "patient_id": "p1", "split": "train"},
    {"image_id": "img3", "patient_id": "p2", "split": "validation"},
    {"image_id": "img2", "patient_id": "p3", "split": "test"},
    {"image_id": "img4", "patient_id": "p2", "split": "test"},
]
```

Expected shape of output:

```json
{
    "duplicate_images": {"img2"},
    "patients_in_multiple_splits": {
        "p2": {"validation", "test"},
    },
    "split_counts": {
        "train": 2,
        "validation": 1,
        "test": 2,
    },
}
```

You can assume every record contains all required keys with valid values.
