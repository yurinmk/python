class Pilha:
    def __init__(self):
        self.pilha1 = ''
        self.pilha2 = ''
    def testaMaisElementos(self,pilha1,pilha2):
        if len(pilha1) > len(pilha2):
            return True
        else:
            return False

