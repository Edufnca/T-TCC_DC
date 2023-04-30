from datetime import date, datetime
import mysql.connector

conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='bot_telebot',
)
cursor = conexao.cursor()
def read_provas_data():
    comando = f'SELECT data_prova FROM provas'
    cursor.execute(comando)
    resultado = cursor.fetchall()
    cursor.close()
    conexao.close()
    return resultado
def notifica_provas():
    data_atual = date.today()
    data_prova = read_provas_data()
    data_tresD = datetime(year=0, month=0, day=3)
    for data_prova in data_prova:
        data_notifica = data_prova - data_tresD
        if data_atual == data_notifica:
            comando = f'SELECT name_prova FROM provas WHERE data_prova = {data_prova}'
            cursor.execute(comando)
            prova = cursor.fetchall()
            notificacao = f"Olá, falta 3 dias para a {prova}"