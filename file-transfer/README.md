# Panther File Transfer Script

This repository contains a secure and dynamic Bash script to transfer files from a production environment to a development environment using `scp`.

## 📁 Folder Structure

- `transfer_files.sh`: Main script to perform file transfers.
- `input/`: Contains `prod_files.txt` and `dev_files.txt` listing source and destination file paths.
- `output/`: Stores logs of file transfers.

## 🔧 Usage
Set your remote credentials using environment variables:

```bash
REMOTE_USER=your_username REMOTE_HOST=your_host bash transfer_files.sh
