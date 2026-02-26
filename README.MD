📄 API de Validação de CPF e CNPJ com Autenticação

API REST desenvolvida em Python + Flask para validação de documentos fiscais brasileiros (CPF e CNPJ), com autenticação de usuários e controle de acesso via sessão.

O projeto expõe regras reais de validação através de endpoints HTTP, permitindo integração com sistemas externos como:

aplicações web

sistemas de cadastro

ERPs

formulários digitais

🚀 Funcionalidades
🔐 Autenticação de Usuário

Cadastro de usuário

Login

Controle de sessão

📑 Validação de Documentos

A API realiza validação completa de:

✔️ CPF
✔️ CNPJ

Incluindo:

Sanitização de entrada

Remoção de máscara

Cálculo de dígitos verificadores

Bloqueio de sequências inválidas

A validação segue o padrão oficial baseado no algoritmo Módulo 11.

🌐 Endpoints
👤 Usuário
Cadastro
POST /user/register

Body:

{
  "username": "usuario",
  "password": "senha"
}
Login
POST /user/login

Body:

{
  "username": "usuario",
  "password": "senha"
}
📄 Validação
Validar CPF
POST /validate/cpf

Body:

{
  "cpf": "12345678909"
}

Resposta:

{
  "valid": true
}
Validar CNPJ
POST /validate/cnpj

Body:

{
  "cnpj": "11222333000181"
}

Resposta:

{
  "valid": true
}
🧠 Regras Aplicadas

A API valida documentos com base em:

Estrutura numérica correta

Rejeição de padrões inválidos (ex: 11111111111)

Cálculo dos dígitos verificadores

Isso garante validação real e não apenas verificação de formato.

🏗️ Arquitetura

O projeto segue separação de responsabilidades:

Routes → Interface HTTP

Services / Validators → Regra de negócio

Auth → Controle de sessão

🛠️ Tecnologias Utilizadas

Python

Flask

Flask Sessions

Regex

Algoritmo Módulo 11

▶️ Como Executar

Clone o repositório:

git clone https://github.com/Dev2TT/Validador-CPF-CNPJ.git
cd Validador-CPF-CNPJ

Instale as dependências:

pip install -r requirements.txt

Execute:

python app.py

A API estará disponível em:

http://localhost:5000
🧪 Testes

Você pode testar os endpoints utilizando:

Postman

Insomnia

Curl

📌 Possíveis Evoluções

Testes automatizados

JWT Authentication

Suporte a CNPJ alfanumérico (novo padrão Receita Federal)

Deploy em nuvem

👨‍💻 Autor

Desenvolvido por Victtor Oliveira