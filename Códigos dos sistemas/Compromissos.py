from datetime import date, datetime, timedelta
from Banco_de_dados import *
from Dicionario import *
import random
def notifica_compromisso():
    data_atual = datetime.now().date()
    data_notificacao = data_atual + timedelta(days=3)
    read = read_bd('data', 'compromisso')
    for compromisso in read():
        data_compromisso = compromisso[0].date()
        if data_atual == data_notificacao.date():
            comando = f'SELECT name_compromisso FROM compromissos WHERE data_compromisso = {data_notificacao}'
            cursor.execute(comando)
            compromisso = cursor.fetchall()
            mensagem = random.choice(mensagem_alerta_compromisso)
            notificacao = f"{mensagem} {compromisso}"
            return notificacao
    conexao.close()



