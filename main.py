from flask import Flask

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return "Olá, bem-vindo à minha aplicação Flask!"

if _name_ == '__main__':
    app.run(debug=True)