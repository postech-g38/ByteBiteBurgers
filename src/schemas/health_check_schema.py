from pydantic import BaseModel


class HealthCheckResponse(BaseModel):
    status: str = 'alive'
    message: str = 'hello world'