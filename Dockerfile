FROM python:3.11

RUN pip install "poetry==1.7.0"

WORKDIR /app
COPY poetry.lock .
COPY pyproject.toml .
RUN poetry config virtualenvs.create false

COPY . .

RUN poetry install

EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
