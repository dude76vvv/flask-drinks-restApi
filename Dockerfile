FROM python:3.11-alpine


WORKDIR /usr/src/rest-drink-app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY ./app ./app

EXPOSE 5000

CMD [ "flask", "run", "--host=0.0.0.0", "--port=5000"]