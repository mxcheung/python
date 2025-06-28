def apply_tags(resource, tags: list[dict]):
    for tag in tags:
        Tags.of(resource).add(tag["key"], tag["value"])
