Nome: Luan Moura, Tiago Rocha.
RA: 22407039, 22454546. 

Projeto de Programação para WEB parte 01


O sistema foi desenvolvido com Python e Django, utilizando SQLite como banco de dados.  
O principal objetivo é auxiliar no gerenciamento de eventos acadêmicos, como seminários, palestras e monitorias.

O sistema possibilita que diferentes tipos de usuários (alunos, professores e organizadores) realizem cadastro, login, criação de eventos, inscrições e emissão de certificados de participação.



Funcionalidades e Caso de Uso(Pode ser visto via PDF).

Escopo do Sistema
    1. Cadastro de usuários;
    2. Cadastro de eventos;
    3. Inscrição de Usuários;
    4. Emissão de Certificados;
    5. Autenticação de usuários.


Requisitos Funcionais
RF01:
    O sistema deve permitir o cadastro de usuários com nome, telefone, instituição, login, senha
    e perfil.
RF02:
    O sistema deve permitir o login de usuários cadastrados.
RF03:
    O sistema deve permitir que organizadores cadastrem eventos com informações como tipo,
    data, horário, local
RF04:
    O sistema deve permitir que alunos e professores se inscrevam em eventos disponíveis.
RF05:
    O sistema deve emitir certificado de participação para o usuário que concluiu o evento.


Requisitos Não Funcionais
RNF01:
    O sistema deve ser desenvolvido em Python usando Django e SQLite.
RNF02:
    O sistema deve ter uma interface clara, organizada e responsiva para o usuário.
RNF03:
    O sistema deve garantir a segurança de dados dos usuários.
RNF04:
    O sistema deve ser compatível com os principais navegadores da web, como Chrome,
    Opera e Safari.


Casos de Uso
    Cadastro de Usuário:
        Ator principal: Aluno, Professor, Organizador
        Descrição: Permite que o usuário crie uma conta informando seus dados pessoais e perfil.
        Fluxo principal:
            01. O usuário acessa a tela de cadastro.
            02. Informa nome, telefone, instituição, login, senha e perfil.
            03. O sistema valida os dados e salva no banco.
            04. Exibe mensagem de sucesso.
            Fluxo alternativo:
                Login já existe: Mensagem de erro.

    Login:
        Ator principal: Usuário cadastrado
        Descrição: Permite que o usuário acesse o sistema com seu login e senha.
        Fluxo principal:
            01. O usuário informa login e senha.
            02. O sistema verifica no banco.
            03. Se válidos, redireciona para o painel principal.
            Fluxo alternativo:
                Se inválidos: Mensagem de erro.

Cadastro de Evento:
    Ator principal: Organizador
    Descrição: Permite criar e cadastrar novos eventos.
    Fluxo principal:
        01. O organizador acessa a opção “Cadastrar Evento”.
        02. Informa tipo, título, data, horário, local e capacidade.
        03. O sistema salva no banco.
        Fluxo alternativo:
            Campos não preenchidos: Mensagem de erro.

Inscrição em Evento:
    Ator principal: Aluno / Professor
    Descrição: Permite que o usuário se inscreva em um evento disponível.
    Fluxo principal:
        01. O usuário visualiza lista de eventos.
        02. Seleciona um evento e clica em “Inscrever-se”.
        03. O sistema cria a inscrição e exibe confirmação.
        Fluxo alternativo:
            Evento cheio: Mensagem de erro.

Emissão de Certificados:
    Ator principal: Organizador
    Descrição: Permite gerar certificados para os participantes inscritos.
    Fluxo principal:
    01. O organizador acessa o evento e visualiza lista de inscritos.
    02. Clica em “Emitir certificado”.
    03. O sistema gera o certificado com código único.
    04. O certificado é salvo e pode ser baixado pelo participante.


Tecnologias Utilizadas

- Linguagem: Python; 
- Framework: Django; 
- Banco de Dados: SQLite;  
- Front-end: HTML, CSS e Bootstrap;   
- IDE: Visual Studio Code. 


Executar Projeto

01.Clonar repositório
    git clone https://github.com/Mluanxl/programacao_web_projeto.git

02.Criar Ambiente Virtual 
    python -m venv venv
    venv\Scripts\activate

03.Instalar Django
    pip install django

04.Criar Migrate 
    python manage.py makemigrations
    python manage.py migrate

05.Rodar Server
    python manage.py runserver
        http://127.0.0.1:8000/


Protótipo. 
    Local
        templates/index.html
    
    ou

    Local
        PDF/Protótipo.pdf


Diagrama Lógico de Banco de Dados / Código. 
    Código
        Local
            banco_de_dados.sql

    Código SQLite
        Local
            models.py ( usuario / evento ).

    Diagrama
        PDF/Diagrama Lógico.pdf
        



