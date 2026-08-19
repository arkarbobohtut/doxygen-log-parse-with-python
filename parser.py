import sys
import re
import csv
import os

def parse_log_file(input_filepath, output_filepath):
    if not os.path.exists(input_filepath):
        print(f"Error: File '{input_filepath}' not found.")
        return

    if os.path.getsize(input_filepath) == 0:
        print(f"Warning: The file '{input_filepath}' is empty. Nothing to parse.")
        return

    pattern = re.compile(r"^([^:]+):(\d+):\s*(warning:\s*.*)$")

    parsed_rows = []

    with open(input_filepath, "r", encoding="utf-8") as file:
        for line in file:
            line = line.strip()
            match = pattern.match(line)

            if match:
                file_path = match.group(1)
                line_number = match.group(2)
                message = match.group(3)

                parsed_rows.append([line_number, file_path, message])

    if parsed_rows:
        with open(output_filepath, "w", newline="", encoding="utf-8") as csv_file:
            writer = csv.writer(csv_file)

            writer.writerow(["Line", "File", "Message"])
            writer.writerows(parsed_rows)

        print(f"Successfully parsed {len(parsed_rows)} entries into '{output_filepath}'.")
    else:
        print("No matching log entries were found.")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python3 parse.py <path_to_log_file> <output_csv_file>")
        sys.exit(1)

    log_file_input = sys.argv[1]
    output_file = sys.argv[2]

    parse_log_file(log_file_input, output_file)