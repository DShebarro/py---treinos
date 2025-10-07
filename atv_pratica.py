def calcular_media(notas): # Calcula a media de uma lista de notas
    if not notas:
        return 0.0
    return sum(notas) / len(notas)

def verificar_situacao(media): # Verifica a situação que o aluno está: Aprovado ou Reprovado
    if media >= 7.0:
        return "APROVADO"
    else:
        return "REPROVADO"
    
def guardar_notas(): # Fluxo principal

    notas_aluno = [] # Cadastro de Notas

    print("Insira as notas do aluno. Digite '0' para finalizar")
    
    # Coleta as notas
    while True:
        notas = float(input("Nota: "))

        # Condição de parada 
        if notas == 0: 
            break

        #Adiciona a nota à lista    
        notas_aluno.append(notas)

    if not notas_aluno:
        print("\nNenhuma nota foi inserida!")
        return
    
    media = calcular_media(notas_aluno)

    situacao = verificar_situacao(media)

    # Relatório Final

    print("\nRelatório Final")
    print("Notas Registradas".format(notas_aluno))
    print("Média: {:.2f}".format(media))
    print("Situação: {}".format(situacao))

# Executação do Sistema
if __name__ == "__main__":
    guardar_notas()