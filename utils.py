from typing import Any, Callable, Dict, List, Optional, TypeVar, Union

T = TypeVar('T')

def compose_pipelines(funcs: List[Callable[[Any], Any]]) -> Callable[[Any], Any]:
    """Chain a sequence of functions into a single pipeline operation."""
    def pipeline(data: Any) -> Any:
        for func in funcs:
            data = func(data)
        return data
    return pipeline

def batch_process(items: List[T], size: int) -> List[List[T]]:
    """Partition an iterable into smaller chunks of defined size."""
    return [items[i:i + size] for i in range(0, len(items), size)]

def dict_deep_merge(base: Dict[Any, Any], update: Dict[Any, Any]) -> Dict[Any, Any]:
    """Recursively merge two dictionaries using a nested update approach."""
    result = base.copy()
    for key, value in update.items():
        if isinstance(value, dict) and key in result and isinstance(result[key], dict):
            result[key] = dict_deep_merge(result[key], value)
        else:
            result[key] = value
    return result

class LazyValue:
    """Container for deferred computation of values to optimize resource allocation."""
    def __init__(self, func: Callable[[], T]) -> None:
        self._func = func
        self._value: Optional[T] = None
        self._evaluated = False

    def get(self) -> T:
        if not self._evaluated:
            self._value = self._func()
            self._evaluated = True
        return self._value  # type: ignore