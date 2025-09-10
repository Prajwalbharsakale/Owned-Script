
# Max Length Check Scripts

This repository contains two Python scripts designed to compute the maximum length of each column in a pipe (`|`) delimited text file.

## Folder Structure
```
Max Length Check/
├── max_length_latin_fallback.py
├── max_length_utf8.py	
```

---


## 1. max_length_latin_fallback.py

### Description
This script performs the same column length calculation but supports multiple encodings (Latin1 and CP1252).

### Usage
```bash
python3 max_length_latin_fallback.py File_to_be_checked.txt
```

### Functionality
- Attempts to open the file using Latin1 or CP1252 encoding.
- Reads the file line by line.
- Splits each line by the pipe (`|`) delimiter.
- Tracks the maximum length of each column.
- Prints progress every 1,000,000 lines.
- Displays the encoding used to read the file.

---

## 2. max_length_utf8.py	

### Description
This script calculates the maximum length of each column in a pipe-delimited file using UTF-8 encoding.

### Usage
```bash
python3 max_length_utf8.py	 File_to_be_checked.txt
```

### Functionality
- Reads the file line by line.
- Splits each line by the pipe (`|`) delimiter.
- Tracks the maximum length of each column.
- Prints progress every 1,000,000 lines.

---

## Output
Both scripts output the maximum length of each column in the format:
```
Max length per column: [length1, length2, ..., lengthN]
```


=================================================================================================================================================

# Understanding Text Encoding Techniques

Text encoding is the process of converting characters into bytes so they can be stored and transmitted by computers. Different encoding techniques support different sets of characters and are used in various contexts.

---

## 🔤 Common Encoding Techniques

### 1. UTF-8 (Unicode Transformation Format - 8-bit)
- Supports all Unicode characters (over 1 million).
- Variable-length encoding: uses 1 to 4 bytes per character.
- Backward compatible with ASCII.
- Ideal for internationalization.

### 2. Latin1 (ISO-8859-1)
- Supports Western European languages.
- Fixed-length encoding: uses 1 byte per character.
- Limited to 256 characters.
- Does not support characters like “€”, smart quotes, or non-Western scripts.

### 3. CP1252 (Windows-1252)
- Superset of Latin1.
- Also uses 1 byte per character.
- Adds 27 extra characters to Latin1 (e.g., “€”, smart quotes).
- Common in Windows environments.

---

## 🆚 Comparison Table

| Feature            | UTF-8         | Latin1 (ISO-8859-1) | CP1252 (Windows-1252) |
|--------------------|---------------|----------------------|------------------------|
| Byte Length        | 1–4 bytes     | 1 byte               | 1 byte                 |
| Character Support  | Full Unicode  | Western Europe only  | Western Europe + extras|
| Compatibility      | Modern systems| Legacy systems       | Windows systems        |
| Emoji Support      | ✅            | ❌                   | ❌                     |

---

## 💡 Why Use Latin1 and CP1252?
Some files may contain characters that UTF-8 cannot decode properly, especially if created on older or Windows systems. Latin1 and CP1252 are fallback options to handle such cases.

---

## 📄 Use Case in Python Scripts
- Your script attempts to read files using Latin1 and CP1252 when UTF-8 fails.
- This ensures compatibility with legacy and Windows-generated files.


