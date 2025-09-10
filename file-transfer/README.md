# Panther File Transfer Script

This Folder contains a secure and dynamic Bash script to transfer files from a production environment to a development environment using `scp`.

## 📁 Folder Structure
```
file-transfer/
├── README.md
├── transfer_files.sh
├── input/
│   ├── prod_files.txt
│   └── dev_files.txt
├── output/
│   └── transfer_log.txt (generated after script runs)
```

## 1. transfer_files.sh
### 📝 Description
This script automates the secure transfer of files from a production environment to a development environment using scp. It reads source and destination file paths from input files and logs the transfer process.

### ▶️ Usage
```bash
REMOTE_USER=your_username REMOTE_HOST=your_host bash transfer_files.sh
```

### ⚙️ Functionality
- Reads file paths from prod_files.txt and dev_files.txt.
- Transfers each file from prod to dev using scp.
- Logs each transfer in transfer_log.txt.
- Uses environment variables for remote credentials (REMOTE_USER, REMOTE_HOST).
- Displays file listing before transfer using ls -ltr.

---
### 📥 Input Example
prod_files.txt
```
/path/to/prod/file1.txt
/path/to/prod/file2.txt
```
dev_files.txt
```
/path/to/dev/file1.txt
/path/to/dev/file2.txt
```

### 📤 Output Example
transfer_log.txt
Transfer Log - Wed Sep 10 10:00:00 UTC 2025
File Transfer: from /path/to/prod/file1.txt to /path/to/dev/file1.txt
File Transfer: from /path/to/prod/file2.txt to /path/to/dev/file2.txt

#### ⚠️ Error Handling
If a file path is invalid, scp will silently fail (stderr redirected).
Script continues processing remaining files.
Listing with ls -ltr helps verify file existence.

---
### ✅ Benefits 
- Secure and dynamic file transfer.
- Avoids hardcoding sensitive data.
- Easy to configure and extend.
- Useful for ETL and environment sync operations.
