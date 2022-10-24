import sqlite3
conn = sqlite3.connect('aula.db')
c = conn.cursor()

a = input("Digite seu DRE: ")
b = input("Digite seu nome completo: ")
s = input("digite sua senha: ")

c.execute("INSERT INTO alunos VALUES('"+a+"','"+b+"')")
c.execute("INSERT INTO users(senha, dre) VALUES('"+s+"','"+a+"')")


conn.commit()