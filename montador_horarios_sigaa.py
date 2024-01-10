from funcoes import *

mensagem = """1- Exibir sua grade
2- Sair
3- Adicionar matéria
4- Retirar matéria
5- Salvar grade
Sua opção: """
tabela = gerar_tabela()

while True:
    linha()
    materia = int(input(mensagem))
    linha()
    print('')
    match materia:
        case 1:
            linha()
            printar_dias()
            linha()
            mostrar_horarios(tabela)
        case 2:
            break
        case 3:
            codigo = input("Digite o código da matéria(Ex.: CIC0090 35M12): ")
            codigo = '+ ' + codigo
            add_materia(tabela, codigo) # adiciona a materia solicitada nos horarios específicos
        case 4:
            codigo = input("Digite o código da matéria(Ex.: CIC0090 35M12): ")
            codigo = '- ' + codigo
            retirar_materia(tabela, codigo) # retira a matéria solicitada dos horários
        case 5:
            criar_arquivo(tabela)

    print('')