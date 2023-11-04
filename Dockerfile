FROM python:3.10-alpine

RUN pip install poetry PyGithub click

WORKDIR /workspace
COPY main.py main.py

CMD [ "python3", "/workspace/main.py" ]
