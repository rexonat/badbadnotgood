FROM mcr.microsoft.com/playwright/python:v1.44.0

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "login_download_upload.py"]
