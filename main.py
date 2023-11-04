import os

from github import Github
from poetry.console.application import Application


def main():
    version = Application().poetry.package.pretty_version
    print("version:", version)

    prefix = os.getenv("INPUT_VERSION_PREFIX")

    version_tag = f"{prefix}{version}"
    print("version_tag:", version_tag)

    token = os.getenv("INPUT_GITHUB_TOKEN")
    if token is None:
        return

    github_repo = os.getenv("GITHUB_REPOSITORY")

    g = Github(token)
    repo = g.get_repo(github_repo)

    for tag in repo.get_tags():
        if tag.name == version_tag:
            return

    sha = repo.get_commits()[0].sha
    repo.create_git_ref(f"refs/tags/{version_tag}", sha)
    print("created tag:", version_tag)


if __name__ == "__main__":
    main()
