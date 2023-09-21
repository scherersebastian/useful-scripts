import requests

def get_authenticated_user_repos(token):
    headers = {
        'Authorization': f'token {token}',
    }
    url = 'https://api.github.com/user/repos?per_page=100&affiliation=owner'
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        repos = response.json()
        for repo in repos:
            print(repo['name'])
    else:
        print(f"Error: {response.status_code}. Could not fetch repos.")

if __name__ == '__main__':
    token = input("Please enter your Personal Access Token (PAT): ")
    
    get_authenticated_user_repos(token)