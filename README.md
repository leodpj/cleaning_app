# 🧹 Cleaning App - Backend (Django)

Este projeto é o backend do aplicativo para **profissionais de limpeza**, permitindo gerenciar clientes, agendamentos, orçamentos e controle financeiro.  
Foi desenvolvido com **Django + Django REST Framework**, pronto para integrar com frontend em React/React Native ou Flutter.

---

## 🚀 Funcionalidades

- Autenticação (login, registro, perfil)
- Gestão de clientes
- Agendamento de serviços
- Criação e envio de orçamentos
- Controle financeiro (receitas, despesas, relatórios)
- Notificações e mensagens
- Configuração de perfil e serviços oferecidos

---

## 🛠️ Tecnologias

- [Python 3.11+](https://www.python.org/)
- [Django 5.x](https://www.djangoproject.com/)
- [Django REST Framework](https://www.django-rest-framework.org/)
- Banco de dados: PostgreSQL / MySQL / SQLite (para dev)

---

## 📂 Estrutura de Pastas

cleaning_app/
│── manage.py
│── cleaning_app/ # Configurações principais
│ ├── settings.py
│ ├── urls.py
│ └── wsgi.py
│
├── users/ # Autenticação & perfil
├── clients/ # Clientes
├── services/ # Agendamentos
├── finance/ # Financeiro
├── quotes/ # Orçamentos
└── communication/ # Mensagens & notificações

yaml
Copy code

---

## ⚙️ Instalação e Configuração

### 1. Clonar repositório
```bash
git clone https://github.com/seu-usuario/cleaning-app-backend.git
cd cleaning-app-backend
2. Criar e ativar ambiente virtual
bash
Copy code
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
3. Instalar dependências
bash
Copy code
pip install -r requirements.txt
4. Configurar variáveis de ambiente
Crie um arquivo .env na raiz com:

ini
Copy code
SECRET_KEY=sua_secret_key
DEBUG=True
DATABASE_URL=sqlite:///db.sqlite3
5. Rodar migrações
bash
Copy code
python manage.py migrate
6. Criar superusuário
bash
Copy code
python manage.py createsuperuser
7. Rodar servidor
bash
Copy code
python manage.py runserver
🧪 Testes
bash
Copy code
python manage.py test
📌 Roadmap
 Deploy com Docker

 Integração com Firebase para notificações

 Integração com gateway de pagamento

 Área do cliente (futuro marketplace)

📄 Licença

Este projeto está sob a licença MIT.