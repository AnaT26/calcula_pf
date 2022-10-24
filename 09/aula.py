from flask import Flask, render_template, request
import sqlite3
pf = Flask(__name__)
mediaf = 8
conn = sqlite3.connect('aula.db')
c = conn.cursor()


def valida_senha_db(dre, senha):
    c.execute('SELECT * FROM users WHERE dre = dre] AND senha = senha', (dre, senha))
    if c.fetchall():
        return render_template("calculapf.html")
    else:
        return render_template("home.html", erro="login incorreto")
    print(linha)


@pf.route("/")
def hw():
    return render_template("home.html")


'''def valida_senha(nome, senha):
    arquivo = open("aula19\\09\senha.txt", "r+")
    linha = arquivo.readlines()
    teste = nome+"-"+senha+"\n"

    if teste in linha:
        return render_template("calculapf.html")
    else:
        return render_template("home.html", erro="login incorreto")
    print(linha)'''


@pf.route("/login", methods=["POST"])
def login():
    if request.method == "POST":
        dre = request.form["dre"]
        senha = request.form["senha"]
        print(dre, senha)
        return valida_senha_db(dre, senha)
    else:
        print("deu ruim")
        return ("ruim")


def calcula_media(p1, p2):
    if (p1+p2)/2 >= 7:
        mediaf = float((p1+p2)/2)
        return render_template("aprovado.html", media=float((p1+p2)/2))
    elif (p1+p2)/2 < 3:
        mediaf = float((p1+p2)/2)
        return render_template("reprovado.html", media=float((p1+p2)/2))
    else:
        return render_template("final.html", mediaf=float((p1+p2)/2))


@pf.route("/media", methods=["POST"])
def media():
    if request.method == "POST":
        p1 = float(request.form["p1"])
        p2 = float(request.form["p2"])
        return calcula_media(p1, p2)
    else:
        print("deu ruim")
        return ("RUIM")


def calcula_final(mediaf, p3):
    if (mediaf+p3)/2 >= 5:
        return render_template("aprovado.html", media=(mediaf+p3)/2)
    else:
        return render_template("reprovado.html", media=(mediaf+p3)/2)


@pf.route("/final", methods=["POST"])
def final():
    if request.method == "POST":
        p3 = float(request.form["p3"])
        return calcula_final(mediaf, p3)
    else:
        print("deu ruim")
        return ("RUIM")


# forange key
# alterar valida senha para usar banco de dados
pf.run()
