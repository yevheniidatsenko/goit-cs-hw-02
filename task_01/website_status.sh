#!/bin/bash

# Define the path to the log file within the task_01 directory
LOG_FILE="$(dirname "$0")/task_01/website_status.log"

# Ensure the directory exists and create it if necessary
mkdir -p "$(dirname "$LOG_FILE")"

# Clear the log file before starting and add a timestamp
echo "Website check run at: $(date)" > "$LOG_FILE"

# List of websites to check
websites=(
    "https://google.com"
    "https://facebook.com"
    "https://twitter.com"
)

# Function to check website availability
check_website() {
    local url=$1
    # Use curl to send an HTTP GET request and capture the HTTP status code
    http_code=$(curl -L -s -o /dev/null -w '%{http_code}' "$url")
    
    # Check if the HTTP status code is 200 (OK)
    if [ "$http_code" -eq 200 ]; then
        echo "$url is UP"
        echo "$url is UP" >> "$LOG_FILE"
    else
        echo "$url is DOWN (HTTP code: $http_code)"
        echo "$url is DOWN (HTTP code: $http_code)" >> "$LOG_FILE"
    fi
}

# Iterate over each website in the list
for site in "${websites[@]}"; do
    check_website "$site"
done

# Append a completion timestamp to the log file
echo "Check completed at: $(date)" >> "$LOG_FILE"

# Notify that the results have been logged
echo "Results have been logged to: $LOG_FILE"