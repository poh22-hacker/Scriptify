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
    print("[4] - Ataque DDOS/DOS")
    print("[5] - sair")
    print("[6] - Atualizar")

    subpergunta = input("Qual você escolhe? - ")

    if subpergunta == "1":
        print("Você escolheu: Pishing")
        os.system('clear')
        os.system('pkg install git')
        os.system('pkg update && apt upgrade -y')
        os.system('pkg install tur-repo')
        os.system('pkg install zphisher')
        os.system('zphisher')

    elif subpergunta == "2":
        print("Você escolheu: Analista de Vulnerabilidade")
        os.system('clear')
        os.system('pkg install git')
        os.system('git clone https://github.com/nmap/nmap.git')
        os.system('cd nmap')
        os.system('pkg install nmap')

    elif subpergunta == "3":
        print("Você escolheu: Ataque Wireless")
        os.system('clear')
        os.system('pkg install git')
        os.system('pkg install aircrack-ng')

    elif subpergunta == "4":
        print("Você escolheu: Ataque DDOS/DOS")
        os.system('clear')
        os.system('pkg install git')
        os.system('git clone https://github.com/gamkers/GAMKERS-DDOS.git')
        os.system('cd GAMKERS-DDOS')
        os.system('python2 GAMKERS-DDOS.py')

    elif subpergunta == "5":
        print("Você escolheu sair.")
        os.system('clear')

    elif subpergunta == "6":
        print("Atualizando")
        os.system('clear')
        os.system('cd')
        os.system('rm -rf Scriptfy')
        os.system('https://github.com/poh22-hacker/Scriptify.git')

    else:
        print("Opção inválida!")

elif pergunta == sair: 
    print("Volte sempre!")
else:
    print("Opção inválida!")
