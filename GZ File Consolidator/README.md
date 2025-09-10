
# GZ File Consolidator Script

This script reads a list of `.gz` compressed files from an input list and consolidates the first 10 lines from each file into a single output file.

---

## 📂 Folder Structure Suggestion
```
GZ File Consolidator/
├── consolidate_gz_files.py
├── file_list.txt
├── consolidated_output.txt
```

---

## 🐍 Script: `consolidate_gz_files.py`

### 🔧 Description
- Reads filenames from `file_list.txt`.
- Opens each `.gz` file and extracts the first 10 lines.
- Writes the extracted lines to `consolidated_output.txt`.
- Adds headers for each file and handles errors gracefully.

### ▶️ Usage
```bash
python3 consolidate_gz_files.py
```

---

## 📥 Input Example: `file_list.txt`
```
logs_20230901.gz
logs_20230902.gz
logs_20230903.gz
```

---

## 📤 Output Example: `consolidated_output.txt`
```
---------------------------------------------------------------------
file1 record :- logs_20230901.gz
-------------------------------------------------------------------
INFO: Starting log...
INFO: Connecting to database...
INFO: Connection successful.
...

---------------------------------------------------------------------
file2 record :- logs_20230902.gz
-------------------------------------------------------------------
INFO: Starting log...
ERROR: Timeout occurred.
...

Error reading logs_20230903.gz: [Errno 2] No such file or directory: 'logs_20230903.gz'
```

---

## ⚠️ Error Handling
- If a file is missing or unreadable, the error is logged in the output file.
- Script continues processing remaining files.

---

## ✅ Benefits
- Quick preview of multiple `.gz` files.
- Useful for log inspection and debugging.

