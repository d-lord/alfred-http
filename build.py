import json
import csv
import os
import sys

# Converts a JSON document (human editable) to CSV (less so) using Alfred's input format for list filters:
# https://www.alfredapp.com/help/workflows/inputs/list-filter/

INPUT_FILENAME = 'input_for_humans.json'
OUTPUT_FILENAME = 'output_for_alfred.csv'

try:
    with open(INPUT_FILENAME) as in_file:
        data = json.load(in_file)
except FileNotFoundError:
    print(f"{INPUT_FILENAME} is missing. This script expects to find it and generate {OUTPUT_FILENAME}.", sys.stderr)
with open(OUTPUT_FILENAME, 'w') as out_file:
    writer = csv.writer(out_file, csv.QUOTE_ALL)
    for item in data['items']:
        # title, subtitle, arg (URL)
        title = f"{item['status_code']} - {item['reason_phrase']}"
        subtitle = f"{item['one_liner']}"
        arg = f"{item['defined_in']}"
        writer.writerow((title, subtitle, arg))
print(f"OK. Drag {OUTPUT_FILENAME} into Alfred, inside the workflow -> the list input block -> \"Drop CSV file above\".")
print(f"Full path: {os.path.realpath(out_file.name)}")
