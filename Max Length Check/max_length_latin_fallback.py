#It will compare the files with latin1..

import sys

# Tries to open the file using a list of encodings until one works
def try_open_with_encodings(file_path, encodings):
    for enc in encodings:
        try:
            f = open(file_path, 'r', encoding=enc)
            return f, enc  # Return the file object and the successful encoding
        except UnicodeDecodeError:
            continue
    raise UnicodeDecodeError("All encoding attempts failed.")

# Computes the maximum length of each column in a pipe-separated file
def compute_max_column_lengths(file_path):
    max_lengths = []
    encodings_to_try = ['latin1', 'cp1252']  # Common encodings to try

    f, used_encoding = try_open_with_encodings(file_path, encodings_to_try)
    print(f"Reading file using encoding: {used_encoding}")

    with f:  # Ensures the file is properly closed after reading
        for line_num, line in enumerate(f, 1):
            columns = line.rstrip('\n').split('|')  # Split line into columns
            while len(max_lengths) < len(columns):  # Extend max_lengths list if needed
                max_lengths.append(0)
            for i, col in enumerate(columns):
                max_lengths[i] = max(max_lengths[i], len(col))  # Track max length per column
            if line_num % 1_000_000 == 0:
                print(f"Processed {line_num:,} lines...")  # Progress update

    return max_lengths

# Entry point of the script
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python max_column_lengths.py <file_path>")
        sys.exit(1)

    file_path = sys.argv[1]
    result = compute_max_column_lengths(file_path)
    print("Max length per column:", result)
