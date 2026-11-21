from typing import Any, Callable, TypeVar, Union

T = TypeVar('T')

def validate_schema(data: Any, schema: dict[str, type]) -> bool:
    """verify dictionary values against specified types."""
    if not isinstance(data, dict):
        return False
    return all(isinstance(data.get(k), v) for k, v in schema.items())

def chain_validators(*funcs: Callable[[T], bool]) -> Callable[[T], bool]:
    """composition of multiple validation predicates."""
    def validator(value: T) -> bool:
        return all(f(value) for f in funcs)
    return validator

def non_empty_string(value: Any) -> bool:
    """check for non-whitespace string existence."""
    return isinstance(value, str) and bool(value.strip())

def range_checker(low: Union[int, float], high: Union[int, float]) -> Callable[[Union[int, float]], bool]:
    """factory for bound checking logic."""
    def check(value: Union[int, float]) -> bool:
        return low <= value <= high
    return check

if __name__ == "__main__":
    is_valid_age = range_checker(0, 120)
    combined = chain_validators(is_valid_age, lambda x: x % 1 == 0)
    print(f"Validation result: {combined(25.0)}")