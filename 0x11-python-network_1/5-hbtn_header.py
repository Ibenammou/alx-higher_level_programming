#!/usr/bin/python3
"""
Takes in a URL, sends a request to the URL, and displays the value of the
variable X-Request_Id in the response header using the requests package
"""

import requests
import sys


if __name__ == '__main__':
    url = sys.argv[1]

    response = requests.get(url)

    # Retrieve and print the value of the X-Request_Id header
    x_request_id = response.headers.get('X-Request-Id')
    print(x_request_id)
