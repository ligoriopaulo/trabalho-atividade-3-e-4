total_pessoas = 0
idades = 0
pessoas_velhas = ""
maior_idade = -1
while True:
    nome = input("digite seu nome:")
    while True:
        try:
            idade = int(input("digite sua idade: "))
            break
        except ValueError:
            print("por favor digite uma idade valida: ")
    total_pessoas += 1
    idade = idade
    if idade > maior_idade:
        maior_idade = idade
        pessoas_velhas = nome
        continuar = input("deseja continuar? (sim/nao)")
        while continuar not in ['sim' , 'nao']:
            continuar = input("Resposta invalida. Deseja continuar? (sim/nao)")
            if continuar == 'sim': 
                break
            print("\n===== Resumo do cadastro =====")
            print(f"total de pessoas cadastradas{total_pessoas}")
            print(f"media de idade do grupo: {idades / total_pessoas:.2f}anos")
            print(f"pessoa mais velha: {pessoas_velhas} com {maior_idade}anos")