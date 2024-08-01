# Python 3.11 Lightweight Base Image ->  Debian Distro use < apt-get >
FROM --platform=linux/amd64 python:3.11-slim

# Update Packages Manager
RUN apt-get update -y \
    && apt-get upgrade -y \
    && apt autoremove -y
RUN pip install --upgrade pip
RUN apt-get install -y build-essential python3-dev

# App Directory
ENV SERVICE_HOME=/usr/src/app

WORKDIR ${SERVICE_HOME}

# Copy Source Code
COPY src/ src/

COPY migrations.py migrations.py

# Install Dependencies
COPY requirements/common.txt .
RUN pip install \
    -r common.txt \
    --no-cache-dir

# Create User and Group
RUN useradd app_user \
    && groupadd app_group

# User and Group Permissions
RUN chown -R app_user:app_user ${SERVICE_HOME} \
    && chmod -R 755 ${SERVICE_HOME}

USER app_user

EXPOSE 8000

ENTRYPOINT ["uvicorn", "src.app:app", "--host", "0.0.0.0", "--port", "8000"]
