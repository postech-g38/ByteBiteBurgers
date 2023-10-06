FROM python3.11-slim

ENV SERVICE_HOME=/usr/src/application

WORKDIR ${TASK_ROOT}

COPY src/ src/

CMD ["python", "src/main.py"]
