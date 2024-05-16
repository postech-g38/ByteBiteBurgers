db = connect("localhost:27017/mongo");

db.usuarios.insertMany([
    {
        nome: "Cliente Pedro",
        senha: "senha123",
        cpf: "24945805016",
        tipo: "cliente",
        criado_em: new Date(),
        atualizado_em: null,
        email: "pedro@email.com"
    },
    {
        nome: "Admin Joao",
        senha: "senha123",
        cpf: "40986296074",
        tipo: "admin",
        criado_em: new Date(),
        atualizado_em: null,
        email: "joao@email.com"
    }
]);
    