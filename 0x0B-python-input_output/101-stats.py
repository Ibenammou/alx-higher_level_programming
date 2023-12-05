#!/usr/bin/python3
"""Define function read stdin"""


import sys
import signal

# Define variables to store metrics
total_file_size = 0
status_code_counts = {}


def print_metrics():
    """Define print_metrics"""

    print(f"Total file size: {total_file_size}")
    for status_code in sorted(status_code_counts):
        print(f"{status_code}: {status_code_counts[status_code]}")


def reset_metrics():
    """Define reset_metrics"""

    global total_file_size
    global status_code_counts
    total_file_size = 0
    status_code_counts = {}


def signal_handler(sig, frame):
    """Define singnal_handler"""

    # Handle the keyboard interruption (CTRL + C)
    print_metrics()
    sys.exit(0)

# Register the CTRL + C signal handler


signal.signal(signal.SIGINT, signal_handler)

line_count = 0
try:
    for line in sys.stdin:
        line = line.strip()
        parts = line.split()
        if len(parts) >= 8:
            status_code = parts[-2]
            file_size = int(parts[-1])

            # Update total file size
            total_file_size += file_size

            # Update status code counts
            status_code_counts[status_code] = status_code_counts.get(status_code, 0) + 1

            line_count += 1

            # If we have processed 10 lines, print metrics and reset
            if line_count % 10 == 0:
                print_metrics()
                reset_metrics()

except KeyboardInterrupt:
    # Handle the keyboard interruption (CTRL + C)
    print_metrics()
