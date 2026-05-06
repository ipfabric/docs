FROM python:3.12-bookworm

WORKDIR /app

COPY poetry.lock pyproject.toml /app/

COPY . .

RUN apt-get update

EXPOSE 8000

RUN python3 -m pip install poetry

RUN poetry install --only=docs

ENTRYPOINT ["poetry", "run", "mkdocs", "serve", "-a", "0.0.0.0:8000"]