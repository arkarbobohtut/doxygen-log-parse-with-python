# Log Parser Script (`parse.py`)

A simple Python script that parses C/C++ compiler or linter warning log files and exports them into a clean CSV format.

## Features

- **Regex Parsing:** Extracts the file path, line number, and full warning message from log entries.
- **Dynamic Output Naming:** Output CSV is saved in the same location and base name as the log file (e.g., `warnings.log` becomes `warnings.csv`).
- **Standard Library Only:** Uses built-in Python modules (`sys`, `re`, `csv`, `os`) so no extra package installation (`pip`) is needed.
- **Safety Checks:** Automatically checks if the input log file exists or if it's empty before attempting to parse.

## Prerequisites

- Python 3.x installed on your machine.

## How to Use

1. Save `parse.py` in your working directory.
2. Run the script from your terminal by passing the path to your log file:

```bash
python3 parse.py warnings.log