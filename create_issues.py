import requests
import json
import re

GITHUB_API_URL = "https://api.github.com"


def create_issue(owner, repo, token, title):
    headers = {
        'Authorization': f'token {token}',
        'Accept': 'application/vnd.github.v3+json',
    }
    url = f"{GITHUB_API_URL}/repos/{owner}/{repo}/issues"
    payload = {
        "title": title,
        "body": ""
    }

    response = requests.post(url, headers=headers, data=json.dumps(payload))
    
    if response.status_code == 201:
        print("Successfully created Issue:", response.json()['url'])
    else:
        print(f"Could not create Issue. Received status code: {response.status_code}")


def main():
    owner = input("Enter GitHub repo owner: ")
    repo = input("Enter GitHub repo name: ")
    token = input("Enter your GitHub personal access token: ")

    transcript = ("The Misfits, the rebels, the troublemakers, the round pegs in the square holes, the ones who see "
                 "things differently. They're not fond of rules and they have no respect for the status quo. You can "
                 "quote them, disagree with them, glorify or vilify them. About the only thing you can't do is ignore "
                 "them because they change things. They push the human race forward. While some may see them as the "
                 "crazy ones, we see genius. Because the people who are crazy enough to think they can change the world, "
                 "are the ones who do.")

    sentences = re.split(r'(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?)\s', transcript)

    for sentence in sentences:
        create_issue(owner, repo, token, sentence)


if __name__ == "__main__":
    main()