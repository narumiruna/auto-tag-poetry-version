FROM python:3.10-alpine

RUN pip install poetry PyGithub click

COPY main.py /main.py

ENTRYPOINT [ "python3", "/main.py" ]
