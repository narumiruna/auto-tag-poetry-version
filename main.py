import os

from github import Github
from poetry.console.application import Application


def main():
    version = Application().poetry.package.pretty_version

    prefix = os.getenv("INPUT_VERSION_PREFIX")

    version_tag = f"{prefix}{version}"

    token = os.getenv("INPUT_GITHUB_TOKEN")
    if token is None:
        return
    g = Github(token)
    repo = g.get_repo(os.environ["github"]["repository"])

    for tag in repo.get_tags():
        if tag.name == version_tag:
            return

    sha = repo.get_commits()[0].sha
    repo.create_git_ref(f"refs/tags/{version_tag}", sha)


if __name__ == "__main__":
    main()
