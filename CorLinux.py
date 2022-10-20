class CorLinux:

    def vermelho(): 
        vermelho = '\033[31m'
        return vermelho
    
    def verde():
        verde = '\033[32m'
        return verde

    def azul():    
        azul = '\033[34m'
        return azul

    def ciano():    
        ciano = '\033[36m'
        return ciano
    
    def magenta():   
        magenta = '\033[35m'
        return magenta
    
    def amarelo():    
        amarelo = '\033[33m'
        return amarelo

    def restaura_cor(): 
        original = '\033[0;0m'
        print('{}'.format(original))