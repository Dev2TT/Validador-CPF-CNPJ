# API de Validação de CPF e CNPJ

API REST desenvolvida em **Python (Flask)** para validação de documentos brasileiros (CPF e CNPJ), com autenticação de usuários e exposição de regras de negócio via HTTP.

O projeto demonstra a aplicação de lógica de domínio real em um serviço backend consumível por outras aplicações.

---

## Principais Responsabilidades

- Autenticação de usuários (login e sessão)
- Validação de CPF
- Validação de CNPJ
- Sanitização de entrada
- Verificação de dígitos validadores (Módulo 11)
- Rejeição de padrões inválidos

---

## Arquitetura

A API foi estruturada com separação de responsabilidades:

- **Rotas** → Interface HTTP
- **Serviços de validação** → Regra de negócio
- **Autenticação** → Controle de acesso

Esse modelo permite que a lógica de validação seja reutilizada independentemente da camada de transporte.

---

## Endpoints

### Autenticação

POST `/user/register`  
POST `/user/login`

---

### Validação

POST `/validate/cpf`

```json id="61zzld"
{
  "cpf": "12345678909"
}

POST /validate/cnpj

{
  "cnpj": "11222333000181"
}
Stack

Python

Flask

Execução
git clone https://github.com/Dev2TT/Validador-CPF-CNPJ.git
cd Validador-CPF-CNPJ
pip install -r requirements.txt
python app.py
Objetivo do Projeto

Demonstrar:

Implementação de regras fiscais reais

Exposição de serviços via API REST

Estruturação básica de autenticação

Separação entre lógica de negócio e camada de acesso

Autor

Victtor Oliveira
