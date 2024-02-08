"""Read a JSON file or string and create an Excel file with the structure of that JSON."""

# Import required libraries
import pandas as pd
import json
import argparse
import os

# This is where the magic happens 🤓
def parse_json(json_obj, path):
    """Parse a JSON object and store the path to each element in a list."""
    if isinstance(json_obj, dict):
        for k, v in json_obj.items():
            new_path = path + [(k, 'dict' if isinstance(v, dict) else 'list' if isinstance(v, list) else type(v).__name__)]
            data.append(new_path)
            parse_json(v, new_path)
    elif isinstance(json_obj, list):
        for i, v in enumerate(json_obj):
            new_path = path + [(str(i), 'dict' if isinstance(v, dict) else 'list' if isinstance(v, list) else type(v).__name__)]
            data.append(new_path)
            parse_json(v, new_path)
    else:
        return


# Prepare the command line arguments
parser = argparse.ArgumentParser(description='Process a JSON file or string.')
parser.add_argument('-f', '--file', help='The path to a JSON file.')
parser.add_argument('-s', '--string', help='A JSON string.')
args = parser.parse_args()

# Path to each element in the JSON
data = []

# Read the JSON file or string
if args.file:
    if os.path.isfile(args.file):
        with open(args.file, 'r') as f:
            json_obj = json.load(f)
elif args.string:
    json_obj = json.loads(args.string)
else:
    print("Please provide a JSON file or string.")
    exit(1)


# Parse the JSON --> actually envoke the function
parse_json(json_obj, [("Root", "dict")])

# Add the root object in the first row
data.insert(0, [("Root", "dict")])

# Flatten data and convert to DataFrame --> easier to create the Excel file
data = [[item for sublist in row for item in sublist] for row in data]
df = pd.DataFrame(data)
df.to_excel("json-parser.xlsx", index=False, header=False)