import os

infect = "1"
sair = "2"

print('''
 SSSSS  CCCCC  RRRRR   III  PPPP   TTTTT III  FFFFF  Y   Y
S       C      R   R    I   P   P    T    I   F       Y Y
 SSS    C      RRRRR    I   PPPP     T    I   FFF      Y
    S   C      R  R     I   P        T    I   F        Y
 SSSS    CCCCC R   R   III  P        T   III  F        Y
''')
print("[1] - Tools!!!")  
print("[2] - Sair")

pergunta = input("Qual você escolhe? - ")

if pergunta == infect:  
    print("Dark Link")
    os.system('clear')  
    print('''
 SSSSS  CCCCC  RRRRR   III  PPPP   TTTTT III  FFFFF  Y   Y
S       C      R   R    I   P   P    T    I   F       Y Y
 SSS    C      RRRRR    I   PPPP     T    I   FFF      Y
    S   C      R  R     I   P        T    I   F        Y
 SSSS    CCCCC R   R   III  P        T   III  F        Y
''')
    print(" ---Use com Moderação---")
    print("[1] - Pishing")
    print("[2] - Analista de Vulnerabilidade")
    print("[3] - Ataque Wireless")
    print("[4] - sair")

    subpergunta = input("Qual você escolhe? - ")

    if subpergunta == "1":
        print("Você escolheu: Pishing")
        os.system('clear')
        os.system('sudo apt install git')
        os.system('sudo apt update && apt upgrade -y')
        os.system('sudo apt install tur-repo')
        os.system('sudoo apt install zphisher')
        os.system('zphisher')

    elif subpergunta == "2":
        print("Você escolheu: Analista de Vulnerabilidade")
        os.system('clear')
        os.system('sudo apt install git')
        os.system('git clone https://github.com/nmap/nmap.git')
        os.system('cd nmap')
        os.system('sudo apt install nmap')

    elif subpergunta == "3":
        print("Você escolheu: Ataque Wireless")
        os.system('clear')
        os.system('sudo apt install git')
        os.system('sudo apt install aircrack-ng')

    elif subpergunta == "4":
        print("Você escolheu sair.")
        os.system('clear')

    else:
        print("Opção inválida!")

elif pergunta == sair: 
    print("Volte sempre!")
else:
    print("Opção inválida!")
