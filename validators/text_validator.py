def remove_non_strings(texts: dict):
    return {k: v for k, v in texts.items() if isinstance(v, str)}
