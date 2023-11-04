import os

import click
from github import Github
from poetry.console.application import Application


@click.command()
@click.argument("prefix")
@click.argument("token")
@click.argument("repo")
def main(prefix, token, repo):
    version = Application().poetry.package.pretty_version
    print("version:", version)

    version_tag = f"{prefix}{version}"
    print("version_tag:", version_tag)

    if token is None:
        print("GITHUB_TOKEN not set, skipping tag creation")
        return

    print(f"repo: {repo}")

    g = Github(token)
    repo = g.get_repo(repo)

    for tag in repo.get_tags():
        if tag.name == version_tag:
            return

    sha = repo.get_commits()[0].sha
    repo.create_git_ref(f"refs/tags/{version_tag}", sha)
    print("created tag:", version_tag)


if __name__ == "__main__":
    main()
