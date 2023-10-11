# Python 3.11 Lightweight Base Image
FROM python:3.11.4-alpine3.18
# use apk to install packages

# App Directory
ENV SERVICE_HOME=/app

WORKDIR ${SERVICE_HOME}

# Copy Source Code
COPY src/ src/

# Install Dependencies
COPY requirements/common.txt .
RUN pip install \
    -r common.txt \
    --no-cache-dir

RUN adduser -D app_user \
    && chown -R app_user:app_user /app \
    && chown -R 755 /app

USER app_user

EXPOSE 8000

# ./src/main.py
ENTRYPOINT ["python", "src/main.py"]
