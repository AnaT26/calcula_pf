import sqlite3
conn = sqlite3.connect('aula.db')
c = conn.cursor()

a = input("diga quem roda: ")

c.execute("DELETE from alunos where nome = '"+a+"'")
conn.commit()