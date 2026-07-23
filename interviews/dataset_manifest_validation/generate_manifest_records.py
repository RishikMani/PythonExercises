import random


random.seed(42)

SPLITS = ["train", "validation", "test"]


def generate_records(
    num_records: int = 1000,
    num_patients: int = 300,
    duplicate_images: int = 40,
    multi_split_patients: int = 25,
):
    records = []

    # Track all image ids so we can intentionally duplicate some later
    image_ids = []

    # Patients that are allowed to violate the "one split only" rule
    violating_patients = {
        f"patient_{i}"
        for i in random.sample(range(num_patients), multi_split_patients)
    }

    # Every normal patient gets assigned exactly one split
    patient_home_split = {
        f"patient_{i}": random.choice(SPLITS) for i in range(num_patients)
    }

    for i in range(num_records):
        patient_id = f"patient_{random.randrange(num_patients)}"

        if patient_id in violating_patients:
            split = random.choice(SPLITS)
        else:
            split = patient_home_split[patient_id]

        image_id = f"img_{i}"
        image_ids.append(image_id)

        records.append(
            {
                "image_id": image_id,
                "patient_id": patient_id,
                "split": split,
            }
        )

    # Inject duplicate image ids
    indices_to_modify = random.sample(range(num_records), duplicate_images)

    for idx in indices_to_modify:
        existing_image = random.choice(image_ids)
        records[idx]["image_id"] = existing_image

    return records
