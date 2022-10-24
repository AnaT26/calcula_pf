import sqlite3
conn = sqlite3.connect('aula.db')
c = conn.cursor()

j = c.execute("SELECT * FROM alunos").fetchall()
k = c.execute("SELECT * FROM users").fetchall()
conn.commit
print(j, k)