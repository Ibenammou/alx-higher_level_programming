#!/usr/bin/python3
"""
Takes in a URL and an email, sends a POST request to the passed URL with
the email as a parameter, and displays the body of the response
(decoded in utf-8)
"""

import urllib.parse
import urllib.request
import sys


if __name__ == '__main__':
    url = sys.argv[1]
    email = sys.argv[2]

    # Encode the email parameter for the POST request
    data = urllib.parse.urlencode({'email': email}).encode('utf-8')

    with urllib.request.urlopen(url, data=data) as response:
        # Read and print the body of the response
        cont = response.read().decode('utf-8')
        print(cont)
