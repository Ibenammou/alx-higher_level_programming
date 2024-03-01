#!/usr/bin/python3
"""
Takes in a URL, sends a request to the URL, and displays the body of the
response. If the HTTP status code is greater than or equal to 400, it prints
Error code: followed by the value of the HTTP status code
"""

import requests
import sys


if __name__ == '__main__':
    url = sys.argv[1]

    response = requests.get(url)

    # Print the body of the response
    # print(response.text)

    # Check if HTTP status code is greater than or equal to 400
    if response.status_code >= 400:
        print(f"Error code: {response.status_code}")
    else:
        # Print the body of the response
        print(response.text)
