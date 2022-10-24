import sqlite3
conn = sqlite3.connect('aula.db')
c = conn.cursor()

c.execute('''
           CREATE TABLE IF NOT EXISTS alunos
           (
           [dre] STRING PRIMARY KEY, 
           [nome]STRING
           )
         ''')
c.execute('''
          CREATE TABLE IF NOT EXISTS users
          (
            [id_users]INTEGER PRIMARY KEY,
            [senha]STRING,
            [dre]STRING,
            CONSTRAINT fk_alusers FOREIGN KEY (dre) REFERENCES alunos (dre)
          )
          
          ''')
conn.commit()