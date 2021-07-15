# Jarvis
Discord Bot
<p xmlns:dct="http://purl.org/dc/terms/" xmlns:cc="http://creativecommons.org/ns#" class="license-text">
  <a rel="cc:attributionURL" property="dct:title" href="https://www.github.com/6135/Jarvis">Jarvis</a> by <span property="cc:attributionName">Gui Costa</span> is licensed under 
  <a rel="license" href="https://creativecommons.org/licenses/by-nc/4.0">CC BY-NC 4.0
    <img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1" />
    <img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1" />
    <img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/nc.svg?ref=chooser-v1" />
  </a>
</p>


### Pre-requisitos

* [Python 3.9.0](https://www.python.org/downloads/)
* [Git](https://git-scm.com/downloads)

### Instalação

1. Abrir o terminal na pasta onde vai ser guardado o projeto

e.g.:
```SH
cd ~/Documentos/Projects/Jarvis
```

2. Clonar o projeto do github

```SH
git clone https://github.com/6135/Jarvis
```

3. Entrar na pasta do projeto


4. Criar o ambiente do projeto (venv)

**Atenção: A versão de Python com a qual criar o ambiente do projeto deve ser igual para todos (v3.9.0)**

Para verificar se a versão de Python instalada é a indicada:

Linux:
```SH
python3.9 -V
```

Windows:
```SH
python -V
```

Se o comando anterior não devolver `Python 3.9.0`, há que mudar a versão antes de criar o ambiente.

Se a versão do Python estiver correta, segue a criação do ambiente (na pasta do projeto):

Linux:
```SH
python3.9 -m venv env
```

Windows:
```SH
py -3 -m venv env
```

5. Ativar o ambiente no terminal

Linux:
```SH
source env/bin/activate
```

Windows:
```SH
env\Scripts\activate
```

Em Windows às vezes há problemas neste passo. Se der ErrorSecurityPolicy, ou algo do género, tentar isto na mesma shell:
```SH
Set-ExecutionPolicy Unrestricted -Force
env\Scripts\activate
```

A extensão padrão de Python do VSCode tem a opção de ativar automaticamente o ambiente em novos terminais. Para ativar a funcionalidade, há que abrir a **Palete de Comandos (F1)**,  **Python: Selecionar Interpretador** e escolher a opção cuja localização comece com `./env` ou `.\env`.

6. Atualizar as dependências iniciais do ambiente

```SH
pip install --upgrade pip setuptools
```

7. Instalar as dependências do projeto

```SH
pip install -r requirements.txt
```

8. Criar um ficheiro .env dentro da pasta dia_aberto (a mesma que tem o settings.py), com as informações sensíveis, como credenciais de acesso à base de dados

O ficheiro .env deve ter o mesmo género de formato do ficheiro já criado "example.env".

As informações de acesso à base de dados do servidor do Gui devem-lhe ser solicitadas.

Para ligar a uma base de dados MySQL local, por exemplo, o .env pode ser:

```
DATABASE_URL=mysql://user:password@localhost:3306/db
SECRET_KEY=q1^j3mv#y9-n&^*j)-rd3@lqqu@jv49p_99$mefzljeuz#fra3
EMAIL_HOST_USER=email@gmail.com
EMAIL_HOST_PASSWORD=password
```

9. Gerar uma nova SECRET_KEY aleatória

## Comandos fundamentais

#### Ativar o ambiente virtual no terminal

Linux:
```SH
source env/bin/activate
```

Windows:
```SH
env\Scripts\activate
```

#### Desativar o ambiente virtual no terminal

```SH
deactivate
```

#### Iniciar o servidor localmente

```SH
python manage.py runserver
```

#### Instalar nova dependência

```SH
pip install nome_da_dependência && pip freeze > requirements.txt
```

#### Instalar lista de dependências necessárias

```SH
pip install -r requirements.txt
```

## Dependências

| Dependência              | Descrição / (Dependência Pai)         |
| ------------------------ | ------------------------------------- |
| pip                      | Gestor de Pacotes (Python)            |
| setuptools               | Ferramentas (Python)                  |
| discord.py               | Discord Framework                     |



## Usefull documentation

| Dependência                                               |
| ----------------------------------------------------------|
| https://pypi.org/project/discord.py/                      |
| https://medium.com/better-programming/coding-a-discord-bot-with-python-64da9d6cade7 |
