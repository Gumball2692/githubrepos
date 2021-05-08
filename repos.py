import requests
import sys


if __name__ == "__main__":
    username = sys.argv[1]
    response= requests.get(f"https://api.github.com/users/{username}/repos")
    repos = response.json()
    for repo in repos:
        repo_name = repo.get("name")
        print(repo_name)
        