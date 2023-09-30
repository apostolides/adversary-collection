FROM python:latest

RUN pip install --no-cache-dir "fastapi[all]"
RUN pip install typing-extensions --upgrade

WORKDIR /server
ADD . .

CMD ["uvicorn", "server:app", "--host", "0.0.0.0", "--port", "8000"]

