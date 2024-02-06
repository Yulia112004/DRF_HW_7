FROM python:3.11

WORKDIR /code

COPY ./pyproject.toml /code/pyproject.toml

RUN poetry install

COPY . .

CMD python manage.py runserver