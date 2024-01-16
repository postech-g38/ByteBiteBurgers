
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


## Instalação do eksctl

O eksctl é uma ferramenta de linha de comando para criar, gerenciar e operar clusters do Amazon Elastic Kubernetes Service (Amazon EKS). Este guia fornece instruções passo a passo para instalar o eksctl em seu ambiente.

Pré-requisitos
Certifique-se de ter os seguintes pré-requisitos instalados em seu sistema antes de começar:

AWS CLI
kubectl
Git

## Instalação do eksctl
Linux ou macOS

```bash
# Instale o eksctl usando o comando curl
curl --silent --location "https://github.com/weaveworks/eksctl/releases/latest/download/eksctl_$(uname -s)_amd64.tar.gz" | tar xz -C /tmp

# Mova o binário para um diretório no seu PATH
sudo mv /tmp/eksctl /usr/local/bin

# Teste a instalação
eksctl version
```
Windows
Abra o PowerShell como administrador.

Execute o seguinte comando para baixar e instalar o eksctl:

```bash
# Certifique-se de substituir <version> pela versão mais recente disponível
curl.exe -o eksctl.exe https://github.com/weaveworks/eksctl/releases/latest/download/eksctl_Windows_amd64.exe

# Mova o binário para um diretório no seu PATH
Move-Item .\eksctl.exe C:\diretorio\do\seu\PATH\eksctl.exe

# Teste a instalação
eksctl version
```
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
## Teste de Stress - K6

A fim de comprovar a escalabilidade e a disponibilidade com o aumento de volume de requisições na aplicação construimos um cenário de teste de stress. 

- O cenário consiste em 20 usuarios virtuais (vu's), realizando 40 requisições por usuario durante 60 segundos ( 20 vu's * 40 interactions = 800 requests em 60 segundos)

A ideia deste teste consiste em comprovar a escalabilidade e disponibilidade com o escalonamento do numero de Pod com uma quantidade minima de erro de requisições

- Para executar o teste execute o seguinte comando:

```bash
k6 run stress_test.js
```
--