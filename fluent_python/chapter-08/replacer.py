from collections.abc import Iterable

FROM_TO = tuple[str, str]


def zip_replace(text: str, changes: Iterable[FROM_TO]) -> str:
    for from_ , to in changes:
        text = text.replace(from_, to)
    return text