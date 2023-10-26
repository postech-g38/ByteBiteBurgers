from locust import HttpUser, task, between


class Healthcheck(HttpUser):
    wait_time = between(1, 3)  # Wait between 1 and 3 seconds

    @task
    def health_check(self):
        self.client.get('/health_check')
    
    @task(2)
    def list_user_by_id(self):
        self.client.get('/v1/usuario/1')

    @task
    def list_all_users(self):
        self.client.get('/v1/usuario/')

    @task
    def create_user(self):
        self.client.post('/v1/usuario/', json={
            "nome": "name",
            "senha": "12345",
            "cpf": "03477306040",
            "tipo": "cliente"
            })
    @task
    def list_all_orders(self):
        self.client.get('/v1/pedido/')
    
    @task
    def create_order(self):
        self.client.post('/v1/pedido/checkout', json={
            "data_mudanca_status": "2023-10-26T19:05:17.541Z",
            "valor": 0,
            "status_pedido": "string",
            "status_pagamento": "string"
        })
    