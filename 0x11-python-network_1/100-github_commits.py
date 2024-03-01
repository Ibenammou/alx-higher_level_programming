#!/usr/bin/python3
"""
Lists 10 commits (from the most recent to oldest)
of a repository on GitHub
"""

import requests
from sys import argv


if __name__ == '__main__':
    # get repository name and owner name from command-line arguments
    repo_name, owner_name = argv[1], argv[2]
    # GitHub API endpoint for listing commits
    url = f"https://api.github.com/repos/{owner_name}/{repo_name}/commits"
    # send a GET request to the GitHub API
    response = requests.get(url)
    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the JSON response
        commits = response.json()

        # Print the details of the 10 most recent commits
        for commit in commits[:10]:
            sha = commit.get('sha')
            commit_info = commit.get('commit', {}).get('author', {})
            author_name = commit_info.get('name', 'Unknown')
            print(f"{sha}: {author_name}")

    else:
        # Display an error message for unsuccessful requests
        print(f"Error: Unable to fetch commits. State Code: \
              {response.staus_code}")
