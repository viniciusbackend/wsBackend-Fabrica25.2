Api de informações de frutas

Uma API REST desenvolvida em Django e Django REST Framework com informações de Frutas.

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

Autenticação com simple_jwt

    POST /token/ - Caminho para pegar o token de validação
    deve ser passado o username e o password do superuser em formato json
    em seguida deve passar no header do método a ser utilizado na key: Authorization e no value: Bearer tokendeacesso

    POST /token/refresh/ - Caminho para pegar o token de validação refresh(ele tem um tempo maior para expirar)


[Entidade Fruta]

    GET /api/frutas - Lista todas as frutas

    POST /api/frutas - Cria uma nova fruta e de acordo com o nome da fruta é preenchida as todas as informações

    GET /api/fruta/id - Retorna uma fruta especifica

    PUT /api/fruta/id - Atualiza uma fruta(obs: não será permitido alterar as informações nutricionais da fruta)

    DELETE /api/fruta/id - Exclui uma fruta