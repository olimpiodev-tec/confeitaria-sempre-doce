from flask import Flask, redirect, url_for, render_template, request
import os

app = Flask(__name__)
UPLOAD_FOLDER = os.path.join(os.getcwd(), 'uploads')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route("/")
def inicial():
    return render_template("index.html")


@app.route("/contato")
def contato():
    return render_template("contato.html")


@app.route("/sobre")
def sobre():
    return render_template("sobre.html")


@app.route("/cardapio")
def cardapio():
    return render_template("cardapio.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    elif request.method == "POST":
        usuario = request.form.get("usuario")
        senha = request.form.get("senha")

        if usuario == "bobesponja":
            if senha == "bob123":
                return redirect(url_for('upload'))

        return render_template("login.html")


@app.route("/upload", methods=["GET", "POST"])
def upload():
    if request.method == "GET":
        return render_template("upload.html")
    elif request.method == "POST":
        file = request.files["file"]
        caminho = os.path.join(app.config["UPLOAD_FOLDER"],  file.filename)
        file.save(caminho)

        return render_template("cardapio.html")


if __name__ == '__main__':
    app.run(debug=True)
