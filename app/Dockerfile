FROM python:3.6
RUN pip install -requirements.txt

COPY ./src /app
COPY ./requirements.txt /app

WORKDIR /app

RUN pip install -requirements.txt

EXPOSE 8000

CMD ["uvicorn", "app.app:app", "--host", ":0.0.0.0", "--port", "15400" ,"--reload"]
