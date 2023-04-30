from datetime import date, datetime
import mysql.connector

conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='bot_telebot',
)
cursor = conexao.cursor()
def read_compromissos_data():
    comando = f'SELECT data_compromisso FROM compromissos'
    cursor.execute(comando)
    resultado = cursor.fetchall()
    cursor.close()
    conexao.close()
    return resultado
def notifica_compromisso():
    data_atual = date.today()
    data_compromisso = read_compromissos_data()
    data_tresD = datetime(year=0, month=0, day=3)
    for data_compromisso in data_compromisso:
        data_notifica = data_compromisso - data_tresD
        if data_atual == data_notifica:
            comando = f'SELECT name_compromisso FROM compromissos WHERE data_compromisso = {data_compromisso}'
            cursor.execute(comando)
            compromisso = cursor.fetchall()
            notificacao = f"Olá, falta 3 dias para o {compromisso}"



