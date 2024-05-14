
# ByteBiteBurgers

Lanchonete com auto atendimento

<details>
  <summary>Repositórios</summary>

Aplicação
https://github.com/postech-g38/ByteBiteBurgers

Lambda
https://github.com/postech-g38/lambda-metrics

Infra Kubernetes com Terraform
https://github.com/postech-g38/terraform-eks

Infra banco de dados gerenciáveis com Terraform
https://github.com/postech-g38/terraform-rds

</details>


### Dependencies
- [ ] Docker
- [ ] Python 3.11
- [ ] direnv


## Commands

### Install Virtual Environment
```bash
pip install virtualenv
```

### Create Virtualenv
```bash
virtualenv venv
```

Veja se o terminal entrou no envrionmento (Vai aparecer o venv no canto esquerdo do terminal) \
[Veja nos docs como entrar no env pelo terminal](https://docs.python.org/pt-br/dev/library/venv.html)

### Install All Python Dependncies
```bash
pip install -r requirements/common.txt
```

### Install Test Dependencies
```bash
pip install -r requirements/common.txt
```

### Running App for Development
```bash
uvicorn src.app:app --reload --port 8000
```

### Quit APP
```
double CTRL + C
```

### Swagger
```bash
http://localhost:8000/docs
```

### Build Databse Tables and EDR
```bash
python manage_database.py
```
Aqui temos 3 funçoes, create, drop e load. Basta troca a funçao embaixo do __name__

### Running Tests
```bash
pytest -s -v
```


### Running Docker
```bash
docker compose -f docker-compose.yml up --build
```

### Running Load Test
```bash
locust -H http://localhost:8000 -f tests/load/locustfile.py
```

open URL:
```bash
http://localhost:8089/
```
Add the number of user and spawn rate and click start Swarming button to start the load test

## DISCLAIMER

- Devemos ter um banco postgres local instalado na maquina, podemos usar o docker compose pra isso tambem ou podemos usar o SQL Lite que funciona emmemoria
