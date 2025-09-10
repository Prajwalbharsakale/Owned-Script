
# Max Length Check Scripts

This repository contains two Python scripts designed to compute the maximum length of each column in a pipe (`|`) delimited text file.

## Folder Structure
```
Max Length Check/
├── Max_Length_Check_Pipe_del_file.py
├── Max_length_check_pipe_del_file.py
```

---

## 1. Max_Length_Check_Pipe_del_file.py

### Description
This script calculates the maximum length of each column in a pipe-delimited file using UTF-8 encoding.

### Usage
```bash
python3 Max_Length_Check_Pipe_del_file.py File_to_be_checked.txt
```

### Functionality
- Reads the file line by line.
- Splits each line by the pipe (`|`) delimiter.
- Tracks the maximum length of each column.
- Prints progress every 1,000,000 lines.

---

## 2. Max_length_check_pipe_del_file.py

### Description
This script performs the same column length calculation but supports multiple encodings (Latin1 and CP1252).

### Usage
```bash
python3 Max_length_check_pipe_del_file.py File_to_be_checked.txt
```

### Functionality
- Attempts to open the file using Latin1 or CP1252 encoding.
- Reads the file line by line.
- Splits each line by the pipe (`|`) delimiter.
- Tracks the maximum length of each column.
- Prints progress every 1,000,000 lines.
- Displays the encoding used to read the file.

---

## Output
Both scripts output the maximum length of each column in the format:
```
Max length per column: [length1, length2, ..., lengthN]
```

