from colorama import Fore, Style
from termcolor import colored

# Colorama
class Colorama:
    def vermelho():
        print('{}Entrando na configuracao{}'.format(Fore.RED, Style.RESET_ALL))
  
# Termcolor
class Termcolor():
    def vermelho():
        print(colored('Hello, World!', 'red', attrs=['reverse', 'blink']))


# Para as bibliotecas funcionarem no cmd, precisa rodar o cod:
# reg add HKEY_CURRENT_USER\Console /v VirtualTerminalLevel /t REG_DWORD /d 0x00000001 /f