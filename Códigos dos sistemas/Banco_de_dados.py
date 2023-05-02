import mysql.connector

#Código que realiza conexão ao banco de dados e suas respectivas funções

conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='bot_telebot',
)
cursor = conexao.cursor()

# tabelas: provas, tarefas

def add_prova(nome, data, nota):
    comando_add_prova = f'INSERT INTO provas (name_prova, data_prova, notas_prova ) VALUES ("{nome}", {data},"{nota}")'
    cursor.execute(comando_add_prova)
    conexao.commit()
    cursor.close()
    conexao.close()

def add_tarefa(nome, data, descricao):
    comando_add_prova = f'INSERT INTO tarefas (name_tarefa, data_tarefa, descricao_tarefa ) VALUES ("{nome}", {data},"{descricao}")'
    cursor.execute(comando_add_prova)
    conexao.commit()
    cursor.close()
    conexao.close()

def add_compromomisso(nome, data, descricao):
    comando_add_prova = f'INSERT INTO compromissos (name_compromisso, data_compromisso, descricao_compromisso ) VALUES ("{nome}", {data},"{descricao}")'
    cursor.execute(comando_add_prova)
    conexao.commit()
    cursor.close()
    conexao.close()

def read_compromissos_data():
    comando = f'SELECT data_compromisso FROM compromissos'
    resultado = conexao.cursor()
    cursor.execute(comando)
    cursor.close()
    return resultado

def add_anotacao(titulo, descricao):
    comando_add_prova = f'INSERT INTO anotacoes (name_anotacao, descricao_anotacao ) VALUES ("{titulo}", "{descricao}")'
    cursor.execute(comando_add_prova)
    conexao.commit()
    cursor.close()
    conexao.close()

def read_bd(tabela):
    comando = f'SELECT * FROM {tabela}'
    cursor.execute(comando)
    resultado = cursor.fetchall()
    cursor.close()
    conexao.close()
    return resultado

def delete_bd(tabela, id):
    comando = f'DELETE FROM {tabela} WHERE name_prova = "{id}"'
    cursor.execute(comando)
    conexao.commit()
    cursor.close()
    conexao.close()

def update_bd(tabela, novo_valor, id):
    comando = f'UPDATE {tabela} SET valor = {novo_valor} WHERE nome_produto = "{id}"'
    cursor.execute(comando)
    conexao.commit()
    cursor.close()
    conexao.close()



