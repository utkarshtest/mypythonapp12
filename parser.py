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
            repo = os.environ.get('GITHUB_REPOSITORY')
            print(repo)
            pr_number = os.environ.get('GITHUB_PR_NUMBER')
            token = os.environ.get('GITHUB_TOKEN')
            
            comment_url = f"https://api.github.com/repos/{repo}/issues/{pr_number}/comments"
            comment_data = {"body": "Blocked - High Vulnerability Found"}
            headers = {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}
            response = requests.post(comment_url, json=comment_data, headers=headers)
            print(response.content)
           
            # print(response.status_code)
            sys.exit(2)

sys.exit(0)
