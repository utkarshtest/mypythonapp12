import sys
import os
import requests

def check_high(line):
    return line.strip() == "HIGH"

print("hlol")
with open('out.txt', 'r') as f:
    for line in f.readlines():
        if check_high(line):
            print("High Vulnerability Found, Blocking PR")
            # Add a comment to the pull request
            repo = os.environ.get('GITHUB_REPOSITORY')
            pr_number = os.environ.get('GITHUB_PR_NUMBER')
            token = os.environ.get('GITHUB_TOKEN')

            comment_url = f"https://api.github.com/repos/{repo}/issues/{pr_number}/comments"
            comment_data = {"body": "Blocked - High Vulnerability Found"}
            headers = {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}

            response = requests.post(comment_url, json=comment_data, headers=headers)

            # Set the pull request status to failure
            status_url = f"https://api.github.com/repos/{repo}/statuses/{os.environ.get('GITHUB_SHA')}"
            status_data = {"state": "failure", "context": "security-check", "description": "Blocked due to high vulnerability"}

            response = requests.post(status_url, json=status_data, headers=headers)
            sys.exit(2)

sys.exit(0)
