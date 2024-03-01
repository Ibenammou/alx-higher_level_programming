#!/usr/bin/python3
"""
Takes in a letter, sends a POST request to http://0.0.0.0:50000/search_user
with the letter as a parameter
"""

import requests
import sys


if __name__ == '__main__':
    # Set q to an empty string if no argument is given
    q = sys.argv[1] if len(sys.argv) > 1 else ""

    # Define the payload with the letter as a parameter
    payload = {'q': q}

    # Send a POST request with the payload
    response = requests.post("http://0.0.0.0:5000/search_user", data=payload)

    try:
        # Try to parse the response as JSON
        json_response = response.json()
        # check if the JSON is properly formatted and not empty
        if 'id' in json_response and 'name' in json_response:
            print(f"[{json_response.get('id')}] {json_response.get('name')}")
        else:
            print("No result")

    except ValueError:
        # Handle invalid JSON format
        print("Not a valid JSON")
