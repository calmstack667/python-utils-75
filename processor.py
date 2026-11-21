import sys
from typing import Any, Callable, Dict, List

class DataSchema:
    def __init__(self, rules: Dict[str, Callable[[Any], bool]]):
        self.rules = rules

    def validate(self, payload: Dict[str, Any]) -> bool:
        return all(key in payload and func(payload[key]) for key, func in self.rules.items())

def process_stream(data_stream: List[Dict[str, Any]]):
    schema = DataSchema({
        'id': lambda x: isinstance(x, int) and x > 0,
        'value': lambda x: isinstance(x, (int, float)),
        'status': lambda x: x in ['active', 'idle']
    })

    results = []
    for entry in data_stream:
        try:
            if not schema.validate(entry):
                raise ValueError(f"Invalid data packet: {entry}")
            
            processed = entry['value'] * 1.05
            results.append({'id': entry['id'], 'result': processed})
        except (ValueError, KeyError) as e:
            print(f"Skipping packet due to: {e}", file=sys.stderr)
            continue
            
    return results

if __name__ == "__main__":
    raw_data = [
        {'id': 1, 'value': 100, 'status': 'active'},
        {'id': 2, 'value': 'bad', 'status': 'idle'},
        {'id': 3, 'value': 200, 'status': 'active'}
    ]
    print(process_stream(raw_data))