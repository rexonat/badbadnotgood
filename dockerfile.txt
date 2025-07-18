FROM mcr.microsoft.com/playwright/python:v1.43.1

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "login_download_upload.py"]
