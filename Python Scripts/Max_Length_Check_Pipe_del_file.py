# this is used for calculating each column max length for pipe '|' delimeted file.
# to run it 
# python3 Max_Length_Check_Pipe_del_file.py File_to_be_checked.txt

import sys

def compute_max_column_lengths(file_path):
    max_lengths = []

    with open(file_path, 'r', encoding='utf-8') as f:
        for line_num, line in enumerate(f, 1):
            columns = line.rstrip('\n').split('|')
            while len(max_lengths) < len(columns):
                max_lengths.append(0)
            for i, col in enumerate(columns):
                max_lengths[i] = max(max_lengths[i], len(col))
            if line_num % 1_000_000 == 0:
                print(f"Processed {line_num:,} lines...")

    return max_lengths

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python max_column_lengths.py <file_path>")
        sys.exit(1)

    file_path = sys.argv[1]
    result = compute_max_column_lengths(file_path)
    print("Max length per column:", result)
