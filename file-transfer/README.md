# Panther File Transfer Script

This Folder contains a secure and dynamic Bash script to transfer files from a production environment to a development environment using `scp`.

## 📁 Folder Structure

file-transfer/
├── README.md
├── CODE.md
├── transfer_files.sh
├── input/
│   ├── prod_files.txt
│   └── dev_files.txt
├── output/
│   └── transfer_log.txt (generated after script runs)

## 🔧 Usage
Set your remote credentials using environment variables:

```bash
REMOTE_USER=your_username REMOTE_HOST=your_host bash transfer_files.sh
