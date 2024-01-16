
# ByteBiteBurgers

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

- A app sobe mas esta quebrando, temos q terminar de arrumar o endpoint de criar usuario


# PENDÊNCIAS

- Vou remover os arquivos init_database.py e drop_database.py depois. Criei apenas porque não consegui usar o manage_database.py.
- O autoincrement não está funcionando para o campo ID. O ideal seria que o usuário não tenha que passar o ID e o backend (ou ainda melhor o banco) seja o responsável por gerar o ID único.
- Carga inicial de categorias (e talvez Produtos)
- Métodos de checkout.

# Kubernetes - EKS


## Criação do Cluster EKS

- Para criar o cluster EKS, execute o comando:

```bash
eksctl create cluster -f k8s/byte-burguer-eks-cluster.yaml         
```
## Configuração da Política IAM
 - Acesse o Console do AWS e vá para Services > IAM.
 - Crie uma nova política utilizando o JSON abaixo:

```bash
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "ec2:AttachVolume",
        "ec2:CreateSnapshot",
        "ec2:CreateTags",
        "ec2:CreateVolume",
        "ec2:DeleteSnapshot",
        "ec2:DeleteTags",
        "ec2:DeleteVolume",
        "ec2:DescribeInstances",
        "ec2:DescribeSnapshots",
        "ec2:DescribeTags",
        "ec2:DescribeVolumes",
        "ec2:DetachVolume"
      ],
      "Resource": "*"
    }
  ]
}
```
- Pegue o IAM role worker node e associe a policy criada 

```bash
# Get Worker node IAM Role ARN
kubectl -n kube-system describe configmap aws-auth

```
    - Vá até Services > IAM > Roles
    - Busque pela role
    - Clique em Permissions
    - Clique em Attach Policy

 ## Instalação do Amazon EBS CSI Driver

- Instale Amazon EBS CSI Driver

```bash
kubectl apply -k "github.com/kubernetes-sigs/aws-ebs-csi-driver/deploy/kubernetes/overlays/stable/?ref=master"
```
## Instalação do Kubernetes Metric Server

- Instale o Metric Server utilizando o seguinte comando:

```bash
kubectl apply -f https://github.com/kubernetes-sigs/metrics-server/releases/latest/download/components.yaml
```
 - Verifique se o pod's estao em execucao com o comando

 ```bash
 kubectl get deployment metrics-server -n kube-system
```
## Implantação de Pods

- Para implantar os pods, utilize o seguinte comando:

```bash
kubectl apply -f k8s
```
- Verifique a execução dos pods com o comando:

```bash
kubectl get all
```



