#!/usr/bin/python3
"""
Takes in a URL, sends a request to the URL, and displays the body of the
response (decoded in utf-8). Handles urllib.error.HTTPError exceptions.
"""

import urllib.request
import urllib.error
import sys


if __name__ == '__main__':
    url = sys.argv[1]

    try:
        with urllib.request.urlopen(url) as response:
            # Read and print the body of response
            cont = response.read().decode('utf-8')
            print(cont)

    except urllib.error.HTTPError as e:
        # Handle HTTPError and print the error code
        print(f"Error code: {e.code}")
