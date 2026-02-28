import click
from pathlib import Path
from auto_doco.github_client import GitHubClient
from auto_doco.collector import ReadmeCollector
from auto_doco.settings import GITHUB_API_TOKEN


@click.command()
@click.option("--org", required=True)
@click.option("--token", default=GITHUB_API_TOKEN)
@click.option("--output", default="docs")
def run(org, token, output):
    client = GitHubClient(token)
    print(f"GitHub Client created...")
    collector = ReadmeCollector(client)
    print("Readme content collector initialised...")
    collector.collect(org, Path(output))
    print(f"Readme content collected successfully. Check at /{output}")


if __name__ == "__main__":
    run()
