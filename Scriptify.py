import os
import time
infect = "1"
sair = "2"
RED = "\033[31m"  # Vermelho
GREEN = "\033[32m"  # Verde
YELLOW = "\033[33m"  # Amarelo
BLUE = "\033[34m"  # Azul
RESET = "\033[0m"  # Resetar para a cor padrão

os.system('clear')
print(f'''
{GREEN}
 SSSSS  CCCCC  RRRRR   III  PPPP   TTTTT III  FFFFF  Y   Y
S       C      R   R    I   P   P    T    I   F       Y Y
 SSS    C      RRRRR    I   PPPP     T    I   FFF      Y
    S   C      R  R     I   P        T    I   F        Y
 SSSS    CCCCC R   R   III  P        T   III  F        Y
{RESET}
''')
print(f"{YELLOW}[1] - Tools!!!{RESET}")  
print(f"{YELLOW}[2] - Sair{RESET}")

pergunta = input(f"{BLUE}Qual você escolhe? - {RESET}")

if pergunta == infect:  
    print("OBS: se alguma ferramenta demorar mais de 50 segundos, use Ctrl + C")
    time.sleep(5)
    os.system('clear')  
    print(f'''
    {GREEN}
 SSSSS  CCCCC  RRRRR   III  PPPP   TTTTT III  FFFFF  Y   Y
S       C      R   R    I   P   P    T    I   F       Y Y
 SSS    C      RRRRR    I   PPPP     T    I   FFF      Y
    S   C      R  R     I   P        T    I   F        Y
 SSSS    CCCCC R   R   III  P        T   III  F        Y
{RESET}
''')
    print(f"{RED} ---Use com Moderação---{RESET}")
    print(f"{YELLOW}[1] - Pishing{RESET}")
    print(f"{YELLOW}[2] - Analista de Vulnerabilidade{RESET}")
    print(f"{YELLOW}[3] - Ataque Wireless{RESET}")
    print(f"{YELLOW}[4] - Ataque DDOS/DOS{RESET}")
    print(f"{YELLOW}[5] - sair{RESET}")
    print(f"{YELLOW}[6] - Atualizar{RESET}")

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
        os.system('clear')
        print(f"{RED}copie e cole os seguintes comandos:{RESET}")
        print(f'''{YELLOW}
        cd
        rm -rf Scriptify
        git clone https://github.com/poh22-hacker/Scriptify
        cd Scriptify
        python3 Scriptify.py
        {RESET}''')
        

    else:
        print("Opção inválida!")

elif pergunta == sair: 
    print("Volte sempre!")
else:
    print("Opção inválida!")
