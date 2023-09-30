1. Clonando o Repositório

Clone o repositório para sua máquina local com o comando abaixo.

    git clone <URL_DO_REPOSITORIO>


2. Configurando o Ambiente Virtual

Vá para o diretório clonado e crie um ambiente virtual Python para isolar as dependências do projeto.

    cd <DIRETORIO_DO_PROJETO>
    python -m venv venv

Ative o ambiente virtual:

    No Windows: .\venv\Scripts\activate
    No MacOS/Linux: source venv/bin/activate


3. Instalando as Dependências

Instale as dependências necessárias do projeto listadas no arquivo requirements.txt.

    pip install -r requirements.txt


4. Configurando Variáveis de Ambiente

Crie um arquivo .env no diretório raiz do projeto para armazenar as configurações sensíveis, como detalhes do banco de dados e SECRET_KEY.

EXEMPLO:

        SECRET_KEY=sua_chave_secreta_de_desenvolvimento
        DEBUG=True 
        DB_NAME=nome_do_seu_banco_de_dados
        DB_USER=nome_do_usuario_do_banco_de_dados
        DB_PASSWORD=senha_do_banco_de_dados
        DB_HOST=localhost
        DB_PORT=5432

Gerando uma nova SECRET_KEY para Desenvolvimento
Você pode gerar uma nova SECRET_KEY usando o Django. Abra um shell Python e execute:
    from django.core.management.utils import get_random_secret_key
    print(get_random_secret_key())


5. Configurando o Banco de Dados

Após configurar as variáveis de ambiente, execute as migrações para configurar o banco de dados.

    python manage.py migrate


6. Rodando o Projeto

Finalmente, para rodar o servidor de desenvolvimento do Django, execute o comando abaixo:

~ python manage.py runserver



Notas Adicionais

    Não exponha seu arquivo .env! Ele está listado no .gitignore para evitar que seja commitado acidentalmente.
