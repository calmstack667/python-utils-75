import sys

def validate_input(data):
    if not isinstance(data, dict):
        raise ValueError('payload must be a dictionary')
    if 'id' not in data or not isinstance(data['id'], int):
        raise KeyError('missing or invalid integer id')
    return True

def process_stream(data_stream):
    for entry in data_stream:
        try:
            if validate_input(entry):
                print(f'processing task {entry["id"]}')
                # functional transformation of data
                result = {k: v for k, v in entry.items() if v is not None}
                yield result
        except (ValueError, KeyError) as e:
            print(f'skipping malformed entry: {e}', file=sys.stderr)

if __name__ == '__main__':
    raw_data = [{'id': 1, 'task': 'init'}, {'id': 'x'}, {'id': 2, 'task': 'exec'}]
    results = list(process_stream(raw_data))
    print(f'processed {len(results)} items successfully')