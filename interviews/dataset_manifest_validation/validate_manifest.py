import generate_manifest_records


def generate_records() -> list:
    """
    Generates a dummy problem record.
    """
    records = generate_manifest_records.generate_records()
    return records


def validate_manifest(records: list[dict]) -> dict:
    """
    Parses and creates a manifest for the records.
    """

    duplicate_images = {}
    patients_in_multiple_splits = {}
    split_counts = {"train": 0, "test": 0, "validation": 0}

    for record in records:
        image_id = record["image_id"]
        duplicate_images[image_id] = duplicate_images.get(image_id, 0) + 1

        patient_id = record["patient_id"]
        split = record["split"]
        patients_in_multiple_splits.setdefault(patient_id, set()).add(split)

        split_counts[split] += 1

    duplicate_images = {k for k, v in duplicate_images.items() if v >= 2}
    patients_in_multiple_splits = {
        k: v for k, v in patients_in_multiple_splits.items() if len(v) >= 2
    }

    return {
        "duplicate_images": duplicate_images,
        "patients_in_multiple_splits": patients_in_multiple_splits,
        "split_counts": split_counts,
    }


if __name__ == "__main__":
    records = generate_records()
    manifest = validate_manifest(records)
