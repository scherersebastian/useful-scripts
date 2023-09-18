import requests
import json

def close_issues_with_label(repo_owner, repo_name, label, token):
    url = f"https://api.github.com/repos/{repo_owner}/{repo_name}/issues"
    headers = {
        'Authorization': f'token {token}',
        'Accept': 'application/vnd.github.v3+json',
    }
    params = {
        'state': 'open', 
        'labels': label,
    }

    response = requests.get(url, headers=headers, params=params)
    
    if response.status_code != 200:
        print(f"Failed to get issues. HTTP Status Code: {response.status_code}")
        return
    
    issues = response.json()
    
    for issue in issues:
        issue_number = issue['number']
        close_url = f"https://api.github.com/repos/{repo_owner}/{repo_name}/issues/{issue_number}"
        data = {
            'state': 'closed'
        }

        response = requests.patch(close_url, headers=headers, json=data)
        
        if response.status_code == 200:
            print(f"Successfully closed issue #{issue_number}")
        else:
            print(f"Failed to close issue #{issue_number}. HTTP Status Code: {response.status_code}")

if __name__ == "__main__":
    repo_owner = input("Enter the repo owner's username: ")
    repo_name = input("Enter the repo name: ")
    label = input("Enter the label: ")
    token = input("Enter your GitHub Personal Access Token: ")

    close_issues_with_label(repo_owner, repo_name, label, token)
