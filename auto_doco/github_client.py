import requests

from auto_doco.settings import GITHUB_API_URL


class GitHubClient:

    def __init__(self, token: str):
        self.headers = {
            "Authorization": f"Bearer {token}",
            "Accept": "application/vnd.github+json"
        }

    def list_public_repos(self, org: str):
        url = f"{GITHUB_API_URL}/users/{org}/repos"
        #url = f"{GITHUB_API_URL}/orgs/{org}/repos"
        repos = []

        params = {
            "type": "public",
            "per_page": 100,
        }

        while url:
            response = requests.get(url, headers=self.headers, params=params)

            if response.status_code != 200:
                raise Exception(
                    f"GitHub API error: {response.status_code} - {response.text}"
                )

            data = response.json()

            # If API returns dict (error), stop
            if not isinstance(data, list):
                raise Exception(f"Unexpected response: {data}")

            repos.extend(data)

            # Check pagination header
            url = response.links.get("next", {}).get("url")

            # After first request, params must be cleared
            params = {}

        return repos

    def get_readme(self, owner: str, repo: str):
        url = f"{GITHUB_API_URL}/repos/{owner}/{repo}/readme"
        response = requests.get(url, headers=self.headers)

        if response.status_code != 200:
            return None

        content = response.json()["content"]
        import base64
        return base64.b64decode(content).decode("utf-8")
