import os
from src.settings import ApplicationSettings

def check_env_vars():
    print("APPLICATION_NAME:", os.getenv("APPLICATION_NAME"))
    print("APPLICATION_HOST:", os.getenv("APPLICATION_HOST"))
    print("APPLICATION_PORT:", os.getenv("APPLICATION_PORT"))
    print("ENVIRONMENT:", os.getenv("ENVIRONMENT"))
    print("WORKERS:", os.getenv("ENVIRONMENT"))
    print("TIMEOUT_GRACEFUL_SHUTDOWN:", os.getenv("ENVIRONMENT"))


    check_env_vars()