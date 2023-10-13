
# ByteByteBurguers

Lanchonete com auto atendimento

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

### Build Databse Tables and EDR
```bash
python tests/manage_database.py
```
Aqui temos 3 funçoes, create, destroy e load. Basta troca a funçao embaixo do __name__

### Running Tests
```bash
pytests -s -vvv
```


## DISCLAIMER

- Devemos ter um banco postgres local instalado na maquina, podemos usar o docker compose pra isso tambem ou podemos usar o SQL Lite que funciona emmemoria

- A app sobe mas esta quebrando, temos q terminar de arrumar o endpoint de criar usuario

## Carga Inicial

### Categorias

categorias = [
    {
        "id": 1,
        "nome": "Lanche"
    }, {
        "id": 2,
        "nome": "Acompanhamento"
    }, {
        "id": 3,
        "nome": "Bebida"
    }, {
        "id": 4,
        "nome": "Sobremesa"
    }
]

### Produtos

produtos = [
    {
        "id": 1,
        "nome": "X-Burger",
        "categoria": "Lanche"
    }, {
        "id": 2,
        "nome": "X-Egg-Burger",
        "categoria": "Lanche"
    }, {
        "id": 3,
        "nome": "Batata Média",
        "categoria": "Acompanhamento"
    }, {
        "id": 4,
        "nome": "Batata Grande",
        "categoria": "Acompanhamento"
    }, {
        "id": 5,
        "nome": "Refrigerante",
        "categoria": "Bebida"
    }, {
        "id": 6,
        "nome": "Suco",
        "categoria": "Bebida"
    }, {
        "id": 7,
        "nome": "Sorvete",
        "categoria": "Sobremesa"
    }, {
        "id": 8,
        "nome": "Cookies",
        "categoria": "Sobremesa"
    }
]