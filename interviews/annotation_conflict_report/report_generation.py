import generate_annotations


def generate_annotation_report(records: list[dict]) -> dict:
    conflicting_images: dict[str, set[str]] = {}
    reviewer_counts: dict[str, int] = {}
    consensus_images = {}

    for record in records:
        image_id = record["image_id"]
        reviewer_id = record["reviewer_id"]
        label = record["label"]

        conflicting_images.setdefault(image_id, set()).add(label)
        reviewer_counts[reviewer_id] = reviewer_counts.get(reviewer_id, 0) + 1
        consensus_images.setdefault(image_id, []).append(label)

    conflicting_images = {
        k: v for k, v in conflicting_images.items() if len(v) > 1
    }
    consensus_images = {
        k
        for k, v in consensus_images.items()
        if len(v) > 1 and len(set(v)) == 1
    }

    return {
        "conflicting_images": conflicting_images,
        "reviewer_counts": reviewer_counts,
        "consensus_images": consensus_images,
    }


if __name__ == "__main__":
    records = generate_annotations.generate_annotations()
    report = generate_annotation_report(records)
