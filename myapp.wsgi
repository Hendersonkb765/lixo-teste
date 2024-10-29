import sys
import os

# Adicione o caminho do seu projeto ao sys.path
sys.path.insert(0, '/var/www/lixo-teste')

# Ative o ambiente virtual (ajuste o caminho conforme necessário)
activate_this = '/var/www/lixo-teste/venv/bin/activate_this.py'
exec(open(activate_this).read(), dict(__file__=activate_this))

# Defina variáveis de ambiente, se necessário (como o FLASK_ENV)
os.environ['FLASK_ENV'] = 'development'  # Ou 'development', se for o caso

# Importe a aplicação Flask
from app import app as application  # Ajuste 'app' para o nome do seu módulo Flask
