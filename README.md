API criada em Django Rest Framework para uma clínica médica controlar pacientes cadastrados, agendamentos, históricos e imagens.

# Configurações do Projeto

## Requisitos

1. Ative o ambiente virtual:
```sh
.\venv\Scripts\activate # No Windows
source venv/bin/activate # No macOS/Linux
```

2. Instale as dependências do projeto:
```sh
pip install -r requirements.txt
```

3. Execute as migrações do banco de dados:
```sh
python manage.py migrate
```

4. Inicie o servidor:
```sh
python manage.py runserver
```

## Dependências
As seguintes dependências são necessárias para o projeto:
- Django
- Django REST Framework
- Pillow

Essas dependências estão listadas no arquivo 'requirements.txt' 
