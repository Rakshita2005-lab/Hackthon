import requests

def get_repo_files(repo_url, token):
    headers = {"Authorization": f"token {token}"}
    response = requests.get(repo_url, headers=headers)
    return response.json()