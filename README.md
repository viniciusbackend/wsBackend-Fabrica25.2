Api de informações de frutas

Uma API RESTful desenvolvida em Django e Django REST Framework com informações das frutas.

🚀 Instalação

    Clone o repositório:

bash

git clone https://github.com/viniciusbackend/wsBackend-Fabrica25.2

    Crie um ambiente virtual e ative-o:

bash

python -m venv venv
source venv/bin/activate  # Linux/Mac
# ou
venv\Scripts\activate  # Windows

    Instale as dependências:

bash


    Execute as migrações:

bash

python manage.py migrate

    Crie um superusuário:

bash

python manage.py createsuperuser

    Execute o servidor de desenvolvimento:

bash

python manage.py runserver

🛣️ Endpoints da API

[Entidade Fruta]

    GET /api/frutas - Lista todas as frutas

     POST /api/frutas - Cria uma nova fruta de acordo com o nome da fruta e preencha as informações automaticamente

    GET /api/fruta/id - Retorna uma fruta especifica

    PUT /api/fruta/id - Atualiza uma fruta(obs: não será permitido alterar as informações nutricionais da fruta)

    DELETE /api/fruta/id - Exclui uma fruta