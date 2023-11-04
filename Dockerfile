FROM python:3.10-alpine

RUN pip install poetry PyGithub

WORKDIR /workspace
COPY main.py main.py

CMD [ "python3", "/workspace/main.py" ]
