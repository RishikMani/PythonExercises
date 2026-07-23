# Annotation Conflict Report

You're working on an ML platform where multiple pathologists review the same medical images. Each annotation record represents one pathologist's label for one image.

```json
{
    "image_id": "img_001",
    "reviewer_id": "dr_smith",
    "label": "tumor",
}
```

Possible labels are: `tumor`, `normal` and `artifact`.

---
## Task

Implement:

```python
def generate_annotation_report(records: list[dict]) -> dict:
    ...
```

and return:

```json
{
    "conflicting_images": dict[str, set[str]],
    "reviewer_counts": dict[str, int],
    "consensus_images": set[str],
}
```

---
## Requirements

1. **Conflicting images:** An image is considered conflicting if more than one distinct label has been assigned to it.

Example:

```
img_5

tumor
tumor
normal
```

Output:

```json
{
    "img_5": {
        "tumor",
        "normal",
    }
}
```

The value should contain the set of labels observed.

2. **Reviewer counts:** Count how many annotations each reviewer submitted.

Example:

```json
{
    "dr_smith": 132,
    "dr_jones": 87,
}
```

3. **Consensus images:** Return the set of image IDs where there are at least two annotations and all annotations agree on exactly one label.

Example

```
img_1

tumor
tumor
tumor
```
-> consensus

```
img_2

tumor
normal
```
-> no consensus

```
img_3

tumor
```
-> no consensus (needs at least two annotations)

---
## Constraints

- One pass over the records is preferred.
- Use only the Python standard library.
- Dictionaries and sets should be your primary data structures.
- You may assume all input records are valid.
