def unique_contacts(ids: list[str]) -> list[str]:
    seen = set()
    result = []
    for item in ids:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result
