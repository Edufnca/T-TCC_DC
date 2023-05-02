
ComandAProva = ['addProva', 'addP', 'addp']
Cumprimentos = ['oi', 'Oi', 'ola', 'Ola', 'olaa', 'oii', 'bo dia']
ComandClima = ['clima', 'Clima', 'temperatura', 'Temperatura', 'temp']
ComandCota = ['Cotação', 'cotação', 'dolar', 'Dolar']
ComandVProvas = ['verP', 'ver Provas', 'verprovas']
ComandGPT = ['chatgpt', 'ChatGPT', 'chatGPT', 'GPT', 'gpt', 'chat gpt']
ComandAComando = ['Acomando', 'adicionar comando', 'AddComando', 'AddComnad']

Dicionario_Comandos = {
    'Comandos Adicionar Prova': ComandAProva,
    'Comandos Ver as Provas': ComandVProvas,
    'Comandos Clima': ComandClima,
    'Comandos Cotação': ComandCota,
    'Cumprimentos Usuário': Cumprimentos,
    'Comandos ChatGPT': ComandGPT,
    'Comandos Adicionar Comandos': ComandAComando,
}


for Comandos in Dicionario_Comandos:
    comandos = Dicionario_Comandos[Comandos]
    print(comandos)