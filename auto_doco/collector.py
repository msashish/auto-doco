from pathlib import Path


class ReadmeCollector:

    def __init__(self, github_client):
        self.github = github_client

    def collect(self, org: str, output_dir: Path):
        repos = self.github.list_public_repos(org)
        print(f"Total repo count: {str(len(repos))}")

        repos_dir = output_dir / "repos"
        repos_dir.mkdir(parents=True, exist_ok=True)

        index_lines = ["# Organization Repositories\n"]

        print("Collection in-progress. This may take a while...")

        for repo in repos:
            name = repo["name"]
            readme = self.github.get_readme(org, name)

            if not readme:
                continue

            file_path = repos_dir / f"{name}.md"

            with open(file_path, "w") as f:
                f.write(f"# {name}\n\n")
                f.write(f"[View on GitHub]({repo['html_url']})\n\n")
                f.write("---\n\n")
                f.write(readme)

            index_lines.append(f"- [{name}](repos/{name}.md)")
            print(f"Collected for repo {name}")

        with open(output_dir / "repos.md", "w") as f:
            f.write("\n".join(index_lines))
