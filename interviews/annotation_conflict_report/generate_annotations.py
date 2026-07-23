"""Generate sample annotations for the annotation report generation problem."""

import random


random.seed(42)

LABELS = ["tumor", "normal", "artifact"]


def generate_annotations(
    num_records=1000,
    num_images=300,
    num_reviewers=12,
    conflict_probability=0.20,
):
    records = []

    # Base label for every image
    base_label = {f"img_{i}": random.choice(LABELS) for i in range(num_images)}

    conflicting_images = {
        f"img_{i}"
        for i in random.sample(
            range(num_images),
            int(num_images * conflict_probability),
        )
    }

    for _ in range(num_records):
        image_id = f"img_{random.randrange(num_images)}"
        reviewer_id = f"dr_{random.randrange(num_reviewers)}"

        if image_id in conflicting_images:
            label = random.choice(LABELS)
        else:
            label = base_label[image_id]

        records.append(
            {
                "image_id": image_id,
                "reviewer_id": reviewer_id,
                "label": label,
            }
        )

    return records
