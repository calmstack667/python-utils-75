import re
from typing import Any, Callable, Dict, List, Union

def validate_schema(data: Any, schema: Dict[str, Any]) -> List[str]:
    """schema-based structure enforcement via key traversal"""
    errors = []
    for key, expected_type in schema.items():
        if key not in data:
            errors.append(f"missing field: {key}")
            continue
        if not isinstance(data[key], expected_type):
            errors.append(f"type mismatch on {key}: expected {expected_type.__name__}")
    return errors

def sanitize_input(value: str, pattern: str = r'[^a-zA-Z0-9_]') -> str:
    """regex-based string sanitization for input cleaning"""
    return re.sub(pattern, '', str(value))

def compose_validators(*funcs: Callable) -> Callable:
    """functional pipeline for sequential data validation"""
    def wrapper(data: Any) -> bool:
        return all(func(data) for func in funcs)
    return wrapper

class DataSentinel:
    """singleton-like sentinel for missing data flags"""
    def __repr__(self):
        return "<SENTINEL_VOID>"

VOID = DataSentinel()

def extract_deep(data: Dict, path: str, default: Any = VOID) -> Any:
    """recursive dot-notation lookup for nested dicts"""
    keys = path.split('.')
    curr = data
    try:
        for key in keys:
            curr = curr[key]
        return curr
    except (KeyError, TypeError):
        return default