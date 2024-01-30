FROM python:3.8-slim

WORKDIR /app

COPY requirements.txt /app

RUN python3 -m pip install --upgrade pip && pip3 install -r /app/requirements.txt --no-cache-dir

COPY cook_book/ /app

CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]
