FROM python:alpine

WORKDIR /app
ADD main.py /app/main.py

ENTRYPOINT ["python",  "/app/main.py", "--text"]
