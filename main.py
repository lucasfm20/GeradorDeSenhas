from random import randint


def novaSenha():
    lista = []
    tamanho = int(input("Digite o tamanho da senha:"))
    for i in range (tamanho):
        num=randint(0,9)
        letraMin = chr(randint(97,122))
        letraMai = chr(randint(65,90))
        esc= randint(1,3)
        
        match esc:
            case 1:
                lista.append(num)
            case 2:
                lista.append(letraMin)
            case 3:
                lista.append(letraMai)
    lista = ", ".join(map(str,lista))
    lista = lista.replace(",","")
    print(f"\nNova senha: {lista}\n")


def menu():

    while True:
        print("*"*15)
        print("Menu")
        print("1-Gerar senha")
        print("2-Sair")
        print("*"*15)

        esc = int(input(f"\nDigite uma opcao: "))

        if esc == 1:
            novaSenha()
        elif esc == 2:
            break
        else:
            print("Digite um número válido!")

menu()