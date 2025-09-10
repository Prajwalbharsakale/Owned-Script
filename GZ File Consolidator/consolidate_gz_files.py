import gzip

# Input file containing the list of .gz filenames (one per line)
input_list_file = 'file_list.txt'  # Update this if your file has a different name

# Output file where consolidated content will be written
output_file = 'consolidated_output.txt'

# Open the input list and output file
with open(input_list_file, 'r') as file_list, open(output_file, 'w') as outfile:
    for idx, line in enumerate(file_list, start=1):
        filename = line.strip()  # Remove any leading/trailing whitespace
        if filename:
            # Write a header for each file's content
            outfile.write(
                f"\n{'-'*70}\n"
                f"File {idx} record: {filename}\n"
                f"{'-'*70}\n"
            )
            try:
                # Open the .gz file in text mode
                with gzip.open(filename, 'rt') as gz_file:
                    # Write the first 10 lines from the .gz file
                    for i, content_line in enumerate(gz_file):
                        if i < 10:
                            outfile.write(content_line)
                        else:
                            break
                outfile.write("\n")  # Add spacing after each file's content
            except Exception as e:
                # Log any errors encountered while reading the file
                outfile.write(f"Error reading {filename}: {e}\n\n")

print(f"✅ Consolidated file '{output_file}' created successfully.")
