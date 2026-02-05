from flask import Flask, render_template, url_for

# Cria a aplicação Flask
app = Flask(__name__)

# Dicionario de produtos
lista_produtos = [
    {"id":1,"nome":"Notebook"},
    {"id":2,"nome":"Celular"},
    {"id":3,"nome":"Tablet"}
]

# Rota é o endereço de onde vai executar
# Rota inicial
# Decorators - Marcadores de função
@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html", title="Home",header="Pagina Flask")

@app.route ("/produtos")
def produtos():
    return render_template("produtos.html", title="Produtos",header="Pagina de lista de produtos",produtos=lista_produtos)

@app.route ("/produtos/<int:produto_id>")
def produtos_id(produto_id):
    return f"API Flask! - Produto ID: {produto_id}"

# Executa o servidor
if __name__ == '__main__':
    app.run(debug=True)
