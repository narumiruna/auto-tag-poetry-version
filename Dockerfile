FROM python:3.10-alpine

RUN pip install poetry PyGithub

COPY main.py main.py

CMD [ "python3", "main.py" ]
