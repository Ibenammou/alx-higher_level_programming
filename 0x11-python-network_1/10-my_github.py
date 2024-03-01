#!/usr/bin/python3
"""
Takes GitHub credentials (username and personal access token and uses the
GitHub API to display the user's id.
"""

import requests
from sys import argv


if __name__ == '__main__':
    # Get GitHub username and personal access token from
    # command-line arguments
    username, token = argv[1], argv[2]

    # set up the authentication header using Basic Authentication
    auth = (username, token)
    # GitHub API endpoint for the authenticated user
    url = "https://api.github.com/user"

    # Send a GET request to the GitHub API
    response = requests.get(url, auth=auth)

    # check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the JSON response and display the user's id
        user_data = response.json()
        print(user_data.get('id'))
    else:
        # Display None for unsucessful requests
        print(None)
