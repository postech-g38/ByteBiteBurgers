# Olá, professor 👋

## Entrega da fase 04 ⬇️
<details> 
  <summary>Abrir</summary>

  ➡️ Fase 04: 
  
  [![Assista ao Vídeo no YouTube](https://img.shields.io/badge/Assista%20ao%20V%C3%ADdeo-no%20YouTube-red?style=for-the-badge&logo=youtube)](https://www.youtube.com/watch?v=mldtRj6B6lc)

  📃 Informações de cobertura dos microsserviços:

  ByteBiteBurgersUsers: https://github.com/postech-g38/ByteBiteBurgersUsers [![Coverage](https://sonarcloud.io/api/project_badges/measure?project=postech-g38_ByteBiteBurgersUsers&metric=coverage)](https://sonarcloud.io/summary/new_code?id=postech-g38_ByteBiteBurgersUsers)  
  ByteBiteBurgersOrders: https://github.com/postech-g38/ByteBiteBurgersOrders [![Coverage](https://sonarcloud.io/api/project_badges/measure?project=postech-g38_ByteBiteBurgersOrders&metric=coverage)](https://sonarcloud.io/summary/new_code?id=postech-g38_ByteBiteBurgersOrders)  
  ByteBiteBurgersPayment: https://github.com/postech-g38/ByteBiteBurgersPayment [![Coverage](https://sonarcloud.io/api/project_badges/measure?project=postech-g38_ByteBiteBurgersPayment&metric=coverage)](https://sonarcloud.io/summary/new_code?id=postech-g38_ByteBiteBurgersPayment)  
  
<details>
  <summary>Repositórios</summary>

  #### Microsserviços
  
  - Usuário: https://github.com/postech-g38/ByteBiteBurgersUsers
  - Pedido: https://github.com/postech-g38/ByteBiteBurgersOrders 
  - Pagamento: https://github.com/postech-g38/ByteBiteBurgersPayment 
     
</details>

<details>
  <summary>Evidência da proteção da branch main (em todos os repositórios)</summary>
  Ela não aceita pull direto, e também requer análise do Sonar  
  
  ![image](https://github.com/postech-g38/ByteBiteBurgers/assets/51934321/793904d5-c2a0-4fcc-bcd6-dc2bfad7ebdb)
  
</details>

<details>
  <summary>Desenho de Arquitetura</summary>

  ![Desenho de Arquitetura](https://github.com/postech-g38/ByteBiteBurgers/assets/38192556/de738fec-aaf0-4128-952e-8874872b4a6f)

</details>

</details>
  
## Entrega da fase 03 ⬇️

<details> 
  <summary>Abrir</summary>

  ➡️ Fase 03: 
  
[![Assista ao Vídeo no YouTube](https://img.shields.io/badge/Assista%20ao%20V%C3%ADdeo-no%20YouTube-red?style=for-the-badge&logo=youtube)](https://www.youtube.com/watch?v=FEfz40NYuA0)


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

<details>
  <summary>Desenho de Arquitetura</summary>

  ![Desenho de Arquitetura](https://github.com/postech-g38/ByteBiteBurgers/assets/51934321/b8f3c32e-80b5-46f4-99fc-3abaf3e256cd)

</details>

<details>
  <summary>Estrutura do banco de dados</summary>
  
![Desenho do banco](https://github.com/postech-g38/ByteBiteBurgers/assets/51934321/d63154d1-3686-4f56-a778-4ed6454cdb23)

</details>
</details>

## Entrega da fase 02 ⬇️

<details> 
  <summary>Abrir</summary>

➡️ Fase 02: 

[![Assista ao Vídeo no YouTube](https://img.shields.io/badge/Assista%20ao%20V%C3%ADdeo-no%20YouTube-red?style=for-the-badge&logo=youtube)](https://www.youtube.com/watch?v=tMUzzM8YnzE)




<details>
  <summary>Desenho de Arquitetura</summary>

  ![Desenho de Arquitetura](https://github.com/postech-g38/ByteBiteBurgers/assets/51934321/b8f3c32e-80b5-46f4-99fc-3abaf3e256cd)


  
</details>

<details>
  <summary>Os requisitos do negócio (problema)</summary>

Automatizar o processo de pedidos em estabelecimentos, proporcionando uma experiência eficiente para os clientes, criando um fluxo de trabalho, desde a realização do pedido até a entrega do produto. Por fim, facilitar o gerenciamento de pedidos, pagamentos, usuários e produtos disponíveis.

## Requisitos Funcionais

1. **Gerenciamento de Pedidos:**
   - Permitir que os clientes façam pedidos através dos totens.
   - Criar uma fila de pedidos para otimizar a entrega.
   - Permitir a atualização do status do pedido e consulta em tempo real.

2. **Notificações:**


teste
   - Notificar o usuário quando o pedido estiver concluído.

3. **Processamento de Pagamentos:**
   - Aceitar métodos de pagamento diretamente no totem.
   - Processar e alterar o pedido automaticamente.

4. **Gerenciamento de Produtos:**
   - Permitir a consulta, edição e deleção dos produtos no sistema.

5. **Gerenciamento de Usuários:**
   - Permitir a consulta, edição e deleção dos usuários do sistema.

## Requisitos Não Funcionais

1. **Desempenho:**
   - Lidar com picos de tráfego e indisponibilidade de máquinas.
   - Escalar conforme necessário sem perder dados.

2. **Escalabilidade:**
   - Permitir que o sistema cresça sem a necessidade de recriar o projeto.

## Riscos de Negócio

- **Sistemas Terceiros:**
  - O pagamento é processado em um sistema terceiro, que pode estar indisponível no momento, afetando a operação.
 
</details>
 

<details>
  <summary>Os requisitos de infraestrutura: </summary>
 ## Nuvem Utilizada

Amazon Web Services (AWS)

## Recursos Utilizados no Projeto

O projeto foi iniciado com a ferramenta `eksctl`, que auxilia e facilita o processo de criação de clusters na AWS. Foram utilizados os seguintes serviços da AWS para compor o projeto nesta entrega:

- **Amazon EKS (Elastic Kubernetes Service):**
  - Utilizado para gerenciar clusters Kubernetes.

- **Amazon EC2 (Elastic Compute Cloud):**
  - Utilizado para fornecer instâncias virtuais escaláveis para o projeto.

- **Amazon EBS (Elastic Block Store):**
  - Utilizado para fornecer volumes de armazenamento persistentes para as instâncias EC2.
</details>

<details>
  <summary>Link do Swagger no projeto ou link para download da collection do Postman (JSON).</summary>

- **Swagger:**
  - Link para a documentação Swagger que sobe com a aplicação: [http://localhost:8000/docs](http://localhost:8000/docs)

- **Postman:**
  - Collection do Postman: [ByteBiteBurgers](https://www.postman.com/gold-robot-4346/workspace/g38-pos-tech-fiap/collection/30696994-63b32e4a-a75e-4298-a551-d8cfeb17253b?action=share&creator=30696994&active-environment=30696994-08c7d317-27c4-47af-b65f-8e6d5ca36b23)
  - 
</details>
</details>

## Informações complementares


Para auxiliar na sua trajetória de conhecimento da ByteBiteBugers, criamos esse pequeno roteiro para baixar e executar o sistema.

Após instalar o Docker e o Git, abra um terminal de prompt e execute o passo-a-passo a seguir.

1. Baixar os fontes:

```
git clone https://github.com/postech-g38/ByteBiteBurgers.git
```

2. Criar o container Docker.

```
docker-compose build
```

3. Iniciar o container.

```
Fase 3: Distribuição da Aplicação - Pós Tech - Fiap -4SOAT```

4. Abra o seu navegador e acesse o endereço abaixo.
```
http://localhost:8000/docs
```


## Outros comandos úteis

- Para resetar o banco, execute o comando abaixo, em seguida, execute os passos 2 e 3 para subir novamente o projeto.

```
docker-compose drop postgres
```


## Outros comandos úteis

- Para resetar o banco, execute o comando abaixo, em seguida, execute os passos 2 e 3 para subir novamente o projeto.


Add the number of user and spawn rate and click start Swarming button to start the load test

## DISCLAIMER

- Devemos ter um banco postgres local instalado na maquina, podemos usar o docker compose pra isso tambem ou podemos usar o SQL Lite que funciona emmemoria

# Kubernetes - EKS

## Link Video
https://www.youtube.com/watch?v=tMUzzM8YnzE

## Instalação do eksctl

O eksctl é uma ferramenta de linha de comando para criar, gerenciar e operar clusters do Amazon Elastic Kubernetes Service (Amazon EKS). Este guia fornece instruções passo a passo para instalar o eksctl em seu ambiente.

Pré-requisitos
Certifique-se de ter os seguintes pré-requisitos instalados em seu sistema antes de começar:

[AWS CLI](https://aws.amazon.com/pt/cli/)

[kubectl](https://kubernetes.io/pt-br/docs/reference/kubectl/)

[Git](https://git-scm.com/book/pt-br/v2/Come%C3%A7ando-Instalando-o-Git)


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

teste
