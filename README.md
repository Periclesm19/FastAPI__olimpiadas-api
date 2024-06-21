# AtletasAPI - Projeto FastAPI com SQLite

## Visão Geral

Este projeto é uma API RESTful construída com FastAPI e SQLite. Ele fornece endpoints para gerenciar atletas, incluindo criação, leitura, atualização e exclusão de registros de atletas.

## Tecnologias Utilizadas

- FastAPI para construção da API
- SQLite como banco de dados
- Alembic para migrações de banco de dados
- Documentação interativa automática da API com Swagger UI

## Requisitos

- Python 3.8+
- pip (gerenciador de pacotes do Python)
- FastAPI
- SQLite
- Virtualenv (opcional, mas recomendado)

## Configuração

### 1. Clone o Repositório

```bash
git clone https://github.com/Periclesm19/fastAPI__api-atletas.git
cd fastAPI__api-atletas
```

## 2. Crie e Ative um Ambiente Virtual

### Linux/MacOS

```bash
python -m venv venv
source venv/bin/activate
```

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

## 3. Instale as Dependências

```bash
pip install requirements.txt
```

## 4. Configurar Variáveis de Ambiente

Crie um arquivo .env na raiz do projeto e defina as seguintes variáveis (se necessário):

```prel
DATABASE_URL=sqlite:///./sqlite.db
```

## 5. Aplicar Migrações do Banco de Dados

```bash
alembic upgrade head
```

## 6. Iniciar o Servidor

```bash
uvicorn app.main:app --reload
```

## Estrutura do Projeto

```bash
├── alembic
│   ├── versions
│   └── env.py
├── app
│   ├── crud
│   │   └── atleta_crud.py
│   ├── models
│   │   └── atleta_model.py
│   ├── routers
│   │   └── atleta_router.py
│   ├── schemas
│   │   └── atleta_schema.py
│   ├── database.py
│   └── main.py
├── .env
├── alembic.ini
├── requirements.txt
└── README.md
```

## 7. Acessar a Documentação da API

Abra seu navegador e acesse http://localhost:8000/docs para ver a documentação interativa do Swagger UI.

## Comandos Úteis
- Ativar ambiente virtual:
   - Linux/MacOS: source venv/bin/activate
   - Windows: venv\Scripts\activate
- Instalar dependências: pip install -r requirements.txt
- Aplicar migrações do banco de dados: alembic upgrade head
- Iniciar o servidor: uvicorn app.main:app --reload
- Acessar a documentação da API: http://localhost:8000/docs

## Autor

Desenvolvido por [Pericles Matos](https://www.linkedin.com/in/periclesm19/)
