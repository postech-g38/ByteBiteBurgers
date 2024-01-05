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
    def list_all_orders(self):
        self.client.get('/v1/pedido/')
    
    @task
    def create_order(self):
        self.client.post('/v1/pedido/checkout', json={
        "produtos": [
            {
                "produto_id": 3,
                "quantidade": 2
            }
        ]})
    @task
    def get_product_by_category(self):
        self.client.get('http://localhost:8000/v1/produto/categoria/?categoria=Sobremesa')

    