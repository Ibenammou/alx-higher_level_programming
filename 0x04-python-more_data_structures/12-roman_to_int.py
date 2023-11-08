#!/bin/bash

# Verify if pycodestyle is installed
if ! command -v pycodestyle &> /dev/null; then
    echo "pycodestyle is not installed. You can install it using 'pip install pycodestyle'"
    exit 1
fi

# Find all Python files in the current directory and its subdirectories
python_files=$(find . -type f -name "*.py")

# Check Python files for PEP 8 compliance using pycodestyle
for file in $python_files; do
    if pycodestyle --first --max-line-length=120 "$file"; then
        echo "PEP 8 compliant: $file"
    else
        echo "PEP 8 violations found in $file. Please fix them."
    fi
done

# Make all Python files executable
for file in $python_files; do
    chmod +x "$file"
done

echo "All Python files have been checked for PEP 8 compliance and made executable."

