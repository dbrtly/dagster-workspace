#!/bin/bash

function print_file_contents() {
    local file_path="$1"
    local file_name="${file_path##*/}"
    local file_contents=$(cat "$file_path")

    echo "|____$file_name <$file_contents>"
}

# Set the data directory
data_dir="data"

# Recursively find all files in the data directory
find "$data_dir" -type f | while read file; do
  # Print the file path relative to the data directory
  relative_path=$(echo "$file" | sed "s|$data_dir/||")
  printf "%s\n" "$relative_path"

  # Print the file contents
  printf "|____%s\n" "$(cat "$file")"
done
