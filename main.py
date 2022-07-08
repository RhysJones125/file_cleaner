"""Script to obfuscate column values from CSV files while maintaining
relationships between them."""

import pandas as pd
import codecs

# key: a column, value: {key: value, value: obfuscated value}
keys_and_values = {}


def map_function(row, curr_column):
    """Extract all values which need changing and map them into a dictionary to ensure relationships are maintained."""

    # Create empty dictionary for column heading
    if column not in keys_and_values:
        keys_and_values[curr_column] = {}

    # Add column
    if row[curr_column] not in keys_and_values:
        if not pd.isnull(row[curr_column]):
            keys_and_values[curr_column][row[curr_column]] = codecs.encode(str(row[curr_column]), 'rot13')


def obfuscate_values(row, file_name):
    """Swap columns that need changing with new obfuscated values."""
    for key, value in keys_and_values.items():
        if key in row.index:
            if row[key] in value.keys():
                print(f"replacing {row[key]}, with {value[row[key]]}, in {file_name}")
                row[key] = str(value[row[key]])


column_to_change = [
]

files = [
]

for file in files:
    df = pd.read_csv(file)

    for column in column_to_change:
        if column in df.columns:
            df.apply(map_function, axis=1, curr_column=column)

for file in files:
    df = pd.read_csv(file)
    df = df.where(pd.notnull(df), "")

    df.apply(obfuscate_values, axis=1, file_name=file)

    df.to_csv(f"new_{file}")


