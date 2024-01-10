def linha():
    print('+---------------+----------+----------+----------+----------+----------+----------+')

def printar_dias():
    print('|               | Seg      | Ter      | Qua      | Qui      | Sex      | Sab      |')

def mostrar_horarios(tabela):
    for i in range(0, len(tabela)): # print dos horarios
            japrintou = False
            for j in range(1, 7):
                if tabela[i][j] != 0:
                    if japrintou == False:
                        for k in range(0, 7):
                            if k == 0:
                                print(f'| {tabela[i][k]} |', end='')
                            elif tabela[i][k] != 0:
                                print(f' {tabela[i][k]}  |', end='')
                            else:
                                print(f'          |', end='')
                        japrintou = True
                        print()
                        linha()

def add_materia(tabela, materia):
    mat = materia # salva a materia em string
    printa = True # variavel p nao printar materia repetida
    materia = materia.split()

    if len(materia) > 3:
                for i in range(2, len(materia)):
                    if 'M' in materia[i]:
                        periodo = 'M'
                        dias, horarios = materia[i].split(periodo)
                        for d in dias:
                            for h in horarios:
                                if tabela[int(h)-1][int(d) - 1] == 0:
                                    tabela[int(h)-1][int(d) - 1] = materia[1]
                                elif printa == True:
                                    print(f'!({mat}): você já tem uma matéria nesse horário!')
                                    printa = False
                    
                    elif 'T' in materia[i]:
                        periodo = 'T'
                        dias, horarios = materia[i].split(periodo)
                        for d in dias:
                            for h in horarios:
                                if tabela[int(h) + 5 - 1][int(d) - 1] == 0:
                                    tabela[int(h) + 5 - 1][int(d) - 1] = materia[1]
                                elif printa == True:
                                    print(f'!({mat}): você já tem uma matéria nesse horário!')
                                    printa = False

                    elif 'N' in materia[i]:
                        periodo = 'N'
                        dias, horarios = materia[i].split(periodo)
                        for d in dias:
                            for h in horarios:
                                if tabela[int(h) + 11 - 1][int(d) - 1] == 0:
                                    tabela[int(h) + 11 - 1][int(d) - 1] = materia[1]
                                elif printa == True:
                                    print(f'!({mat}): você já tem uma matéria nesse horário!')
                                    printa = False
    else:
        
        if 'M' in materia[2]:
                periodo = 'M'
                dias, horarios = materia[2].split(periodo)
                for d in dias:
                    for h in horarios:
                        if tabela[int(h)-1][int(d) - 1] == 0:
                            tabela[int(h)-1][int(d) - 1] = materia[1]
                        elif printa == True:
                            print(f'!({mat}): você já tem uma matéria nesse horário!')
                            printa = False
            
        elif 'T' in materia[2]:
            periodo = 'T'
            dias, horarios = materia[2].split(periodo)
            for d in dias:
                for h in horarios:
                    if tabela[int(h) + 5 - 1][int(d) - 1] == 0:
                        tabela[int(h) + 5 - 1][int(d) - 1] = materia[1]
                    elif printa == True:
                        print(f'!({mat}): você já tem uma matéria nesse horário!')
                        printa = False

        elif 'N' in materia[2]:
            periodo = 'N'
            dias, horarios = materia[2].split(periodo)
            for d in dias:
                for h in horarios:
                    if tabela[int(h) + 11 - 1][int(d) - 1] == 0:
                        tabela[int(h) + 11 - 1][int(d) - 1] = materia[1]
                    elif printa == True:
                        print(f'!({mat}): você já tem uma matéria nesse horário!')
                        printa = False

def retirar_materia(tabela, materia):
    mat = materia # salva a materia em string
    printa = True # variavel p nao printar materia repetida
    materia = materia.split()
    
    if len(materia) > 3:
                for i in range(2, len(materia)):
                    if 'M' in materia[i]:
                        periodo = 'M'
                        dias, horarios = materia[i].split(periodo)
                        for d in dias:
                            for h in horarios:
                                if tabela[int(h)-1][int(d) - 1] == materia[1]:
                                    tabela[int(h)-1][int(d) - 1] = 0
                                elif printa == True:
                                    print(f'!({mat})')
                                    printa = False
                    
                    elif 'T' in materia[i]:
                        periodo = 'T'
                        dias, horarios = materia[i].split(periodo)
                        for d in dias:
                            for h in horarios:
                                if tabela[int(h) + 5 - 1][int(d) - 1] == materia[1]:
                                    tabela[int(h) + 5 - 1][int(d) - 1] = 0
                                elif printa == True:
                                    print(f'!({mat})')
                                    printa = False

                    elif 'N' in materia[i]:
                        periodo = 'N'
                        dias, horarios = materia[i].split(periodo)
                        for d in dias:
                            for h in horarios:
                                if tabela[int(h) + 11 - 1][int(d) - 1] == materia[1]:
                                    tabela[int(h) + 11 - 1][int(d) - 1] = 0
                                elif printa == True:
                                    print(f'!({mat})')
                                    printa = False

    else:
        
        if 'M' in materia[2]:
                periodo = 'M'
                dias, horarios = materia[2].split(periodo)
                for d in dias:
                    for h in horarios:
                        if tabela[int(h)-1][int(d) - 1] == materia[1]:
                            tabela[int(h)-1][int(d) - 1] = 0
                        elif printa == True:
                            print(f'!({mat})')
                            printa = False
            
        elif 'T' in materia[2]:
            periodo = 'T'
            dias, horarios = materia[2].split(periodo)
            for d in dias:
                for h in horarios:
                    if tabela[int(h) + 5 - 1][int(d) - 1] == materia[1]:
                        tabela[int(h) + 5 - 1][int(d) - 1] = 0
                    elif printa == True:
                        print(f'!({mat})')
                        printa = False

        elif 'N' in materia[2]:
            periodo = 'N'
            dias, horarios = materia[2].split(periodo)
            for d in dias:
                for h in horarios:
                    if tabela[int(h) + 11 - 1][int(d) - 1] == materia[1]:
                        tabela[int(h) + 11 - 1][int(d) - 1] = 0
                    elif printa == True:
                        print(f'!({mat})')
                        printa = False

def gerar_tabela():
    horarios = [['08:00 - 08:55', 0, 0, 0, 0, 0, 0], # M1
        ['08:55 - 09:50', 0, 0, 0, 0, 0, 0], # M2
        ['10:00 - 10:55', 0, 0, 0, 0, 0, 0], # M3
        ['10:55 - 11:50', 0, 0, 0, 0, 0, 0], # M4
        ['12:00 - 12:55', 0, 0, 0, 0, 0, 0], # M5
        ['12:55 - 13:50', 0, 0, 0, 0, 0, 0], # T1
        ['14:00 - 14:55', 0, 0, 0, 0, 0, 0], # T2
        ['14:55 - 15:50', 0, 0, 0, 0, 0, 0], # T3
        ['16:00 - 16:55', 0, 0, 0, 0, 0, 0], # T4
        ['16:55 - 17:50', 0, 0, 0, 0, 0, 0], # T5
        ['18:00 - 18:55', 0, 0, 0, 0, 0, 0], # T6
        ['19:00 - 19:50', 0, 0, 0, 0, 0, 0], # N1
        ['19:50 - 20:40', 0, 0, 0, 0, 0, 0], # N2
        ['20:50 - 21:40', 0, 0, 0, 0, 0, 0], # N3
        ['21:40 - 22:30', 0, 0, 0, 0, 0, 0]] # N4
    
    return horarios

def criar_arquivo(tabela):
    def escrever_linha(arquivo):
        arquivo.write('+---------------+----------+----------+----------+----------+----------+----------+\n')
    nome = input("Digite seu nome: ").lower()

    semestre = input("Digite seu semestre(Nesse formato -> 2024-1): ")

    titulo = nome + '-' + semestre
    arquivo = open(titulo, 'wt+')
    arquivo.write("|               | Seg      | Ter      | Qua      | Qui      | Sex      | Sab      |\n")
    escrever_linha(arquivo)
    for i in range(0, len(tabela)): # print dos horarios
                japrintou = False
                for j in range(1, 7):
                    if tabela[i][j] != 0:
                        if japrintou == False:
                            for k in range(0, 7):
                                if k == 0:
                                    arquivo.write(f'| {tabela[i][k]} |')
                                elif tabela[i][k] != 0:
                                    arquivo.write(f' {tabela[i][k]}  |')
                                else:
                                    arquivo.write(f'          |')
                            japrintou = True
                            arquivo.write('\n')
                            escrever_linha(arquivo)

    arquivo.close()
    print(f'{nome.capitalize}, seus horários do semestre {semestre}')
    print(f'foram salvos no arquivo {titulo}.')