from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "Aplicacion en Flask"

if __name__ == '__main__':
    app.run()