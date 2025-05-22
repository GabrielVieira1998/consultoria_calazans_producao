# Deploy Simplificado no PythonAnywhere

Este guia contém apenas os passos essenciais para configurar o projeto Consultoria Calazans no PythonAnywhere.

## 1. Criação da Conta

1. Acesse [PythonAnywhere](https://www.pythonanywhere.com) e crie uma conta gratuita
2. Faça login e acesse o Dashboard

## 2. Configuração do Projeto

### Fazer Upload do Projeto

Opção 1: Via GitHub
1. No dashboard do PythonAnywhere, abra um console Bash
2. Clone o repositório:
   ```bash
   git clone https://github.com/GabrielVieira1998/consultoria_calazans_producao.git
   ```

Opção 2: Upload manual
1. Comprima o projeto em um arquivo ZIP
2. No dashboard do PythonAnywhere, faça upload do arquivo
3. No console Bash, descompacte o arquivo:
   ```bash
   unzip nome_do_arquivo.zip
   ```

### Configurar Ambiente Virtual

1. No console Bash, navegue até a pasta do projeto
2. Crie um ambiente virtual:
   ```bash
   mkvirtualenv --python=python3.9 calazans-venv
   ```
3. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

## 3. Configurar a Aplicação Web

1. No dashboard do PythonAnywhere, vá para a seção "Web"
2. Clique em "Add a new web app"
3. Escolha um domínio (será algo como `seuusername.pythonanywhere.com`)
4. Selecione "Manual configuration" (não "Flask")
5. Selecione a versão Python 3.9

### Configurar o WSGI

1. Na página de configuração da aplicação web, localize o link para o arquivo WSGI
2. Clique no link para editar o arquivo
3. Substitua todo o conteúdo pelo seguinte (ajuste os caminhos conforme necessário):

```python
import sys
import os

# Adicionar o diretório do projeto ao path
path = '/home/seuusername/consultoria_calazans_producao'
if path not in sys.path:
    sys.path.append(path)

# Definir variáveis de ambiente
os.environ['FLASK_APP'] = 'wsgi.py'
os.environ['FLASK_ENV'] = 'production'

# Importar a aplicação
from wsgi import app as application
```

### Configurar o Virtualenv

1. Na página de configuração da aplicação web, na seção "Virtualenv"
2. Informe o caminho para o seu virtualenv: `/home/seuusername/.virtualenvs/calazans-venv`

### Configurar Diretórios Estáticos

1. Na seção "Static files", adicione:
   - URL: `/static/`
   - Directory: `/home/seuusername/consultoria_calazans_producao/app/static/`

## 4. Inicializar o Banco de Dados

1. Abra um console Bash
2. Ative o ambiente virtual:
   ```bash
   workon calazans-venv
   ```
3. Navegue até a pasta do projeto
4. Execute o script de inicialização do banco:
   ```bash
   python -c "from app import create_app; app = create_app(); from app.models.database import init_db; with app.app_context(): init_db()"
   ```

## 5. Reiniciar a Aplicação

1. Volte para a página de configuração da aplicação web
2. Clique no botão grande verde "Reload" para iniciar a aplicação

## 6. Manutenção

### Atualizar o Código

1. Faça as alterações no repositório
2. No console Bash do PythonAnywhere:
   ```bash
   cd ~/consultoria_calazans_producao
   git pull
   ```
3. Recarregue a aplicação web

### Backup do Banco de Dados

1. No console Bash:
   ```bash
   cp ~/consultoria_calazans_producao/instance/calazans.sqlite3 ~/backup_$(date +%Y%m%d).sqlite3
   ```

## 7. Solução de Problemas

- Se a aplicação não iniciar, verifique os logs de erro na seção "Web" > "Logs"
- Para testar localmente a aplicação antes de enviar para produção, execute:
  ```bash
  gunicorn wsgi:app
  ``` 