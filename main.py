import click
from github import Github
from poetry.console.application import Application


@click.command()
@click.argument("prefix")
@click.argument("token")
@click.argument("repo")
def main(prefix, token, repo):
    version = Application().poetry.package.pretty_version
    vtag = f"{prefix}{version}"

    repo = Github(token).get_repo(repo)
    for tag in repo.get_tags():
        if tag.name == vtag:
            return

    repo.create_git_ref(
        ref=f"refs/tags/{vtag}",
        sha=repo.get_commits()[0].sha,
    )


if __name__ == "__main__":
    main()
