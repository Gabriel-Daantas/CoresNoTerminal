from CorLinux import CorLinux
from CorWindows import Colorama
from CorWindows import Termcolor

if __name__ == '__main__':
    
    # LINUX
    print('{}Vermelho'.format(CorLinux.vermelho()))
    print('{}amarelo'.format(CorLinux.amarelo()))
    print('{}verde'.format(CorLinux.verde()))
    print('{}azul'.format(CorLinux.azul()))
    print('{}ciano'.format(CorLinux.ciano()))
    print('{}magenta'.format(CorLinux.magenta()))
    CorLinux.restaura_cor()


    # WINDOWS
    print('{}Cor'.format(Colorama.vermelho()))
    print('{}Cor'.format(Termcolor.vermelho()))
