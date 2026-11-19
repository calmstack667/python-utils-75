# python-utils-75

A robust collection of high-performance utility functions designed to streamline repetitive Python development tasks. This library focuses on simplifying data manipulation, file system operations, and execution timing with minimal dependencies.

## Features

*   **File System Helpers:** Simplified recursive file discovery and bulk renaming utilities that handle complex path structures with ease.
*   **Precision Timing:** A lightweight decorator suite to profile function execution speed and memory consumption without polluting business logic.
*   **Data Normalization:** Robust tools for sanitizing JSON-like structures and converting nested dictionary keys between snake_case and camelCase.
*   **Concurrency Wrapper:** Thread-safe abstractions for parallelizing I/O-bound tasks using a simple callback-based interface.

## Installation

Install the package via pip:

```bash
pip install python-utils-75
```

Alternatively, install from source:

```bash
git clone https://github.com/Developer/python-utils-75.git
cd python-utils-75
pip install .
```

## Usage

Easily profile your functions using the built-in timer decorator to identify bottlenecks in your code:

```python
from pyutils75.decorators import time_execution

@time_execution
def process_data(dataset):
    # Simulate heavy lifting
    return [x * 2 for x in dataset]

results = process_data(range(1000000))
# Output: [process_data] executed in 0.042 seconds
```

For advanced usage, refer to the documentation in the `/docs` folder for detailed implementation guides on data normalization and threading utilities.

## License

![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)

Distributed under the MIT License. See `LICENSE` for more information.