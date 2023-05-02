Aulas = list()
Salas = list()
Segunda = {
    1: 'Português', 2: 'Biologia', 3: 'Ed.Física', 4: 'IPSSI', 5: 'IPSSI', 6: 'Geografia', 7: 'Filosofia', 8: 'Filosofia'
}
Terca = {
    1: 'Inglês', 2: 'Biologia', 3: 'História', 4: 'Matemática', 5: 'PAM', 6: 'PAM', 7: 'História', 8: '-'
}
Quarta = {
    1: 'Física', 2: 'Matemática', 3: 'Matemática', 4: 'Química', 5: 'Física', 6: 'PW II', 7: 'PW II', 8: 'Matemática'
}
Quinta = {
    1: 'Química', 2: 'Espanhol', 3: 'Português', 4: 'QTS', 5: 'QTS', 6: 'Espanhol', 7: 'Geografia', 8: 'Inglês'
}
Sexta = {
    1: '-', 2: 'Ed.Física', 3: 'TCC', 4: 'TCC', 5: 'TCC', 6: 'Português', 7: 'Português', 8: '-'
}

def mudar_horario_aulaS(dia_semana, aula, nova_aula):
    if dia_semana==1:
        Segunda[aula] = f'{nova_aula}'
    if dia_semana==2:
        Terca[aula] = f'{nova_aula}'
    if dia_semana==3:
        Quarta[aula] = f'{nova_aula}'
    if dia_semana==4:
        Quinta[aula] = f'{nova_aula}'
    if dia_semana==5:
        Sexta[aula] = f'{nova_aula}'

def aula_dia(dia_semana):
    au = 0
    if dia_semana==1:
        au = 0
        for x in Segunda:
            au = au + 1
            if au == 8:
                print(Aulas[0][au] + '\n')
                break
            if au == 1:
                print('\nSegunda')
                print('\n' + Aulas[0][au])
            else:
                print(Aulas[0][au])
    if dia_semana==2:
        au = 0
        for x in Terca:
            au = au + 1
            if au == 8:
                print(Aulas[1][au] + '\n')
                break
            if au == 1:
                print('\nTerça')
                print('\n' + Aulas[1][au])
            else:
                print(Aulas[1][au])
    if dia_semana==3:
        au = 0
        for x in Quarta:
            au = au + 1
            if au == 8:
                print(Aulas[2][au] + '\n')
                break
            if au == 1:
                print('\nQuarta')
                print('\n' + Aulas[2][au])
            else:
                print(Aulas[2][au])
    if dia_semana==4:
        au = 0
        for x in Quinta:
            au = au + 1
            if au == 8:
                print(Aulas[3][au] + '\n')
                break
            if au == 1:
                print('\nQuinta')
                print('\n' + Aulas[3][au])
            else:
                print(Aulas[3][au])
    if dia_semana==5:
        au = 0
        for x in Sexta:
            au = au + 1
            if au == 8:
                print(Aulas[4][au] + '\n')
                break
            if au == 1:
                print('\nSexta')
                print('\n' + Aulas[4][au])
            else:
                print(Aulas[4][au])

def aula_semana():
    au = 0
    for x in Segunda:
        au = au + 1
        if au == 8:
            print(Aulas[0][au]+'\n')
            break
        if au == 1:
            print('\nSegunda')
            print('\n'+Aulas[0][au])
        else:
            print(Aulas[0][au])
    au = 0
    for x in Terca:
        au = au + 1
        if au == 8:
            print(Aulas[1][au]+'\n')
            break
        if au == 1:
            print('\nTerça')
            print('\n'+Aulas[1][au])
        else:
            print(Aulas[1][au])
    au = 0
    for x in Quarta:
        au = au + 1
        if au == 8:
            print(Aulas[2][au]+'\n')
            break
        if au == 1:
            print('\nQuarta')
            print('\n'+Aulas[2][au])
        else:
            print(Aulas[2][au])
    au = 0
    for x in Quinta:
        au = au + 1
        if au == 8:
            print(Aulas[3][au]+'\n')
            break
        if au == 1:
            print('\nQuinta')
            print('\n'+Aulas[3][au])
        else:
            print(Aulas[3][au])
    au = 0
    for x in Sexta:
        au = au + 1
        if au == 8:
            print(Aulas[4][au]+'\n')
            break
        if au == 1:
            print('\nSexta')
            print('\n'+Aulas[4][au])
        else:
            print(Aulas[4][au])

Aulas.append(Segunda)
Aulas.append(Terca)
Aulas.append(Quarta)
Aulas.append(Quinta)
Aulas.append(Sexta)




