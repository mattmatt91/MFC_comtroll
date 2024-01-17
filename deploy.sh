#!/bin/bash

# SSH details
SSH_USER="gmu"
SSH_SERVER="192.168.2.10"
DEST_DIR="/home/gmu/Desktop/gmu/" # Updated directory path
SSH_KEY="C:/Users/PC/Desktop/private_key.ppk" # Replace with your actual key path

# Folder to copy
FOLDER1="gascontrol"
ADDITIONAL_FILES=("docker-compose.yaml")

# Copy folder using scp
copy_folder() {
    local folder=$1
    scp -i "$SSH_KEY" -r "$folder" "${SSH_USER}@${SSH_SERVER}:${DEST_DIR}"
}

# Check if remote directory exists and create it if it doesn't
ssh -i "$SSH_KEY" "${SSH_USER}@${SSH_SERVER}" "mkdir -p ${DEST_DIR}"

# Clear and prepare remote directory
# ssh -i "$SSH_KEY" "${SSH_USER}@${SSH_SERVER}" "cd ${DEST_DIR} && rm -rf gascontrol && mkdir gascontrol"

# Copy folder
copy_folder "$FOLDER1"


# Copy additional files
for file in "${ADDITIONAL_FILES[@]}"; do
    scp -i "$SSH_KEY" "$file" "${SSH_USER}@${SSH_SERVER}:${DEST_DIR}"
done

# Run Docker Compose
# ssh -i "$SSH_KEY" "${SSH_USER}@${SSH_SERVER}" "cd ${DEST_DIR} && docker-compose down && docker-compose up --build"