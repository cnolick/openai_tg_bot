FROM python:3.8-slim-buster
WORKDIR /app
ADD requirements.txt .
ADD src/* .

RUN pip install --upgrade pip \
    && pip install -r requirements.txt

CMD ["python", "main.py"]


