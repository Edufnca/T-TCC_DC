from datetime import date, datetime, timedelta
from Dicionario import *
import random
from Banco_de_dados import *

def notifica_provas():
    data_atual = datetime.now().date()
    data_notificacao = data_atual + timedelta(days=3)
    read = read_bd('data', 'prova')
    for prova in read():
        data_compromisso = prova[0].date()
        if data_atual == data_notificacao.date():
            comando = f'SELECT name_prova FROM provas WHERE data_prova = {data_notificacao}'
            cursor.execute(comando)
            prova = cursor.fetchall()
            mensagem = random.choice(mensagem_alerta_prova)
            notificacao = f"{mensagem} {prova}"
            return notificacao
    conexao.close()