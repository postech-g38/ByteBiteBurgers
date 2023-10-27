# Olá, professor!

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
docker-compose up
```

4. Abra o seu navegador e acesse o endereço abaixo.

```
http://localhost:8000/docs
```


## Outros comandos úteis

- Para resetar o banco, execute o comando abaixo, em seguida, execute os passos 2 e 3 para subir novamente o projeto.

```
docker-compose drop postgres
```