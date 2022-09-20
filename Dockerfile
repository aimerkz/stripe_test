FROM python:3.10-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt --no-cache-dir
COPY ./ /app
CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]
