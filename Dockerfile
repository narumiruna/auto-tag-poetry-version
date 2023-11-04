FROM python:3.10-alpine

RUN pip install poetry pygithub

COPY main.py main.py

CMD [ "python3", "main.py" ]
