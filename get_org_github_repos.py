import requests

def get_org_repos(org_name, token):
    headers = {
        'Authorization': f'token {token}',
    }
    url = f'https://api.github.com/orgs/{org_name}/repos?per_page=100&type=all'
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        repos = response.json()
        for repo in repos:
            print(repo['name'])
    else:
        print(f"Error: {response.status_code}. Could not fetch repos.")

if __name__ == '__main__':
    org_name = input("Please enter the GitHub organization name: ")
    token = input("Please enter your Personal Access Token (PAT): ")
    
    get_org_repos(org_name, token)