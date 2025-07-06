# Sistema de Gerenciamento de Eventos

Uma aplicação Python desenvolvida seguindo os princípios de **Domain-Driven Design (DDD)** e **SOLID**, implementada com Flask e SQLAlchemy para gerenciar eventos, participantes e slots de reserva.

## 📋 Funcionalidades

- ✅ Criação, listagem e exclusão de eventos
- ✅ Gerenciamento de participantes
- ✅ Sistema de slots com status (reservado, pendente, confirmado, cancelado)
- ✅ API REST para integração
- ✅ Arquitetura limpa seguindo DDD

## 🏗️ Arquitetura do Projeto

Este projeto foi desenvolvido seguindo os princípios de **Domain-Driven Design (DDD)** e **SOLID**, organizando o código em camadas bem definidas:

```
src/
├── main.py                          # Ponto de entrada da aplicação
├── domain/                          # Camada de Domínio (regras de negócio)
│   ├── entities/                    # Entidades do domínio
│   │   ├── event.py                 # Entidade Event
│   │   ├── participant.py           # Entidade Participant
│   │   └── slot.py                  # Entidade Slot
│   └── repositories/                # Interfaces dos repositórios
│       ├── event_repository.py
│       ├── participant_repository.py
│       └── slot_repository.py
├── application/                     # Camada de Aplicação (casos de uso)
│   ├── dtos/                        # Data Transfer Objects
│   │   ├── event_dto.py
│   │   ├── participant_dto.py
│   │   └── slot_dto.py
│   └── use_cases/                   # Casos de uso da aplicação
│       ├── create_event.py
│       ├── create_participant.py
│       ├── delete_event.py
│       ├── delete_participant.py
│       ├── list_events.py
│       └── list_participants.py
├── infrastructure/                  # Camada de Infraestrutura
│   ├── database/                    # Configuração do banco de dados
│   │   ├── connection.py            # Conexão com PostgreSQL
│   │   └── init_db.py               # Inicialização do banco
│   ├── models/                      # Modelos SQLAlchemy
│   │   ├── base.py
│   │   ├── event_model.py
│   │   ├── participant_model.py
│   │   └── slot_model.py
│   └── repositories/                # Implementação dos repositórios
│       ├── event_repository_impl.py
│       ├── participant_repository_impl.py
│       └── slot_repository_impl.py
└── presentation/                    # Camada de Apresentação (controllers)
    └── controllers/
        ├── event_controller.py      # Controller de eventos
        └── participant_controller.py # Controller de participantes
```

### 🎯 Princípios Aplicados

#### **Domain-Driven Design (DDD)**
- **Domain Layer**: Contém as entidades e regras de negócio puras
- **Application Layer**: Orquestra os casos de uso e coordena o fluxo da aplicação
- **Infrastructure Layer**: Implementa detalhes técnicos como banco de dados
- **Presentation Layer**: Gerencia a interface com o usuário (API REST)

## 🚀 Como Executar o Projeto

### Pré-requisitos

- Python 3.8+
- PostgreSQL
- Git

### 1. Clone o Repositório

```bash
git clone <url-do-repositorio>
```

### 2. Criar Ambiente Virtual

#### No Linux/Mac:
```bash
# Criar ambiente virtual
python3 -m venv venv

# Ativar ambiente virtual
source venv/bin/activate
```

#### No Windows:
```bash
# Criar ambiente virtual
python -m venv venv

# Ativar ambiente virtual
venv\Scripts\activate
```

### 3. Instalar Dependências

```bash
pip install -r requirements.txt
```

### 4. Configurar Variáveis de Ambiente

1. Copie o arquivo de exemplo:
```bash
cp .env.exemple .env
```

2. Edite o arquivo `.env` com suas configurações de banco de dados:
```bash
DATABASE_URL="postgresql+psycopg2://seu_usuario:sua_senha@localhost:5432/nome_do_banco"
```

### 5. Configurar Banco de Dados

Certifique-se de que o PostgreSQL está rodando e crie um banco de dados:

```sql
CREATE DATABASE event_management;
```

### 6. Executar a Aplicação

```bash
# Navegar para o diretório src
cd src

# Executar a aplicação
python main.py
```

A aplicação estará disponível em: `http://localhost:5000`

## 📡 Endpoints da API

### Eventos

| Método | Endpoint | Descrição |
|--------|----------|-----------|
| GET | `/api/events` | Listar todos os eventos |
| POST | `/api/events` | Criar um novo evento |
| DELETE | `/api/events/{id}` | Deletar um evento |

#### Exemplo de criação de evento:
```json
POST /api/events
{
    "name": "Workshop Python",
    "description": "Workshop sobre desenvolvimento Python",
    "date": "2025-08-15"
}
```

### Participantes

| Método | Endpoint | Descrição |
|--------|----------|-----------|
| GET | `/api/participants` | Listar todos os participantes |
| POST | `/api/participants` | Criar um novo participante |
| DELETE | `/api/participants/{id}` | Deletar um participante |

#### Exemplo de criação de participante:
```json
POST /api/participants
{
    "name": "João Silva",
    "email": "joao@example.com"
}
```

## 🛠️ Tecnologias Utilizadas

- **Python 3.12**
- **Flask** - Framework web
- **SQLAlchemy** - ORM para banco de dados
- **PostgreSQL** - Banco de dados
- **python-dotenv** - Gerenciamento de variáveis de ambiente
- **psycopg2-binary** - Driver PostgreSQL

## 📦 Dependências

Todas as dependências estão listadas no arquivo `requirements.txt`:

```
blinker==1.9.0
click==8.2.1
Flask==3.1.1
greenlet==3.2.3
itsdangerous==2.2.0
Jinja2==3.1.6
MarkupSafe==3.0.2
psycopg2-binary==2.9.10
python-dotenv==1.1.1
SQLAlchemy==2.0.41
typing_extensions==4.14.1
Werkzeug==3.1.3
```

## 🧪 Estrutura de Dados

### Entidades Principais

#### Event (Evento)
```python
@dataclass
class Event:
    id: int
    name: str
    description: str
    date: str
    slots: List[Slot]
```

#### Participant (Participante)
```python
@dataclass
class Participant:
    id: int
    name: str
    email: str
```

#### Slot (Vaga)
```python
@dataclass
class Slot:
    id: int
    event_id: int
    participant_id: int
    status: SlotStatus  # RESERVED, PENDING_CONFIRMATION, CONFIRMED, CANCELED
```
---
