#!/bin/bash

# Load input file paths
prod_file="input/prod_files.txt"
dev_file="input/dev_files.txt"

# Output log file
log_file="output/transfer_log.txt"
mkdir -p output
echo "Transfer Log - $(date)" > "$log_file"

# Replace with actual remote user and host via environment variables
REMOTE_USER="${REMOTE_USER:-user}"
REMOTE_HOST="${REMOTE_HOST:-your.remote.host}"

paste "$prod_file" "$dev_file" | while read -r src_file dest_file; do
    echo "Listing file: $src_file"
    ls -ltr "$src_file"

    echo "Transferring file $src_file to dev as $dest_file"
    scp "$src_file" "${REMOTE_USER}@${REMOTE_HOST}:$dest_file" 2>/dev/null

    echo "File Transfer: from $src_file to $dest_file" | tee -a "$log_file"
done
