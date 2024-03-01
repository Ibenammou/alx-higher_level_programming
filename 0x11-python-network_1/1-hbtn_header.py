#!/usr/bin/python3
"""
Takes a URL, sends a request to the URL, and displays the value of the
X-Request-Id variable found in the header of the request
"""

import urllib.request
import sys


if __name__ == '__main__':
    url = sys.argv[1]

    with urllib.request.urlopen(url) as response:
        # Retrieve and print the value of the X-Request-Id header
        x_request_id = response.info().get('X-Request-Id')
        print(x_request_id)
