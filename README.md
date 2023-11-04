# auto-tag-version

```yaml
name: Auto Tag Version

on:
  push:

jobs:
  tag:
    permissions:
        contents: write
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: narumiruna/auto-tag-version@main
        with:
          github_token: ${{ secrets.GITHUB_TOKEN }}
          github_repository: ${{ github.repository }}
```
