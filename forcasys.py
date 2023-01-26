import utils

class PartidaDeJogoDaForca:
    
    
    def __init__(self, palavra: str, revelacao: bool, chances: int, instaLoseAdivPalavra: bool):
        
        self.caracteresProibidos = " _\'\"[]{}^~`´+=!@#$%¨&*();:<>,.?/\\|§"     
        self.palavra = palavra.upper() 
        self.palavraStatus = ["_"] * len(palavra)
        self.letrasInformadas = []
        self.ganho = False
        self.perdido = False
        self.finalizado = False
        self.revelacao = revelacao
        self.instaLoseAdivPalavra = instaLoseAdivPalavra
        self.chances = chances

        if (self.chances == 0):
            self.limite = False
        else:
            self.limite = True


        
        
 
        
    
    @property
    def palavra(self):
        return self._palavra
    
    @palavra.setter
    def palavra(self, pl):
        if (any(i in self.caracteresProibidos for i in pl)):
            raise Exception("Palavra contém caracteres inválidos")
            
        else:
            self._palavra = pl
    
    
    @property
    def palavraStatus(self):
        return self._palavraStatus
    
    @palavraStatus.setter
    def palavraStatus(self, pl):
        self._palavraStatus = pl
        
        if ("-" in self.palavra):
                for i in range(len(self.palavra)):
                    if "-" == self.palavra[i]:
                        self.palavraStatus[i] = "-"
        

    def isLetra(self, string):
        
        if (not utils.isnumber(string)) and (len(string) == 1):
            return True
            
        else:
            return False

    
    
    def adivinharLetra(self, letra):
        letra = letra.upper()
        
        if ( self.isLetra(letra) ):
            if (letra in self.palavra) and (letra not in self.letrasInformadas):
                for i in range(len(self.palavra)):
                    if letra == self.palavra[i]:
                        self.palavraStatus[i] = letra
                        
                self.letrasInformadas.append(letra)

                if ("_" not in self.palavraStatus):
                    self.finalizado = True
                return True

                    
            elif (letra not in self.palavra):
                if self.limite is True:
                    self.diminuirChances()
                raise Exception("Letra informada não está na palavra")
                
            elif (letra in self.letrasInformadas):
                raise Exception("Letra já informada")
            
        else:
            raise Exception("Não é uma letra")
            
            
            
    def adivinharPalavra(self, palavra):
        
        palavra = palavra.upper()
        
        if (palavra == self.palavra):
            self.palavraStatus = [x for x in self.palavra]
            self.ganharOJogo()
            return True

        else:
            if self.instaLoseAdivPalavra:
                self.chances = 0
                self.perderOJogo()

            if (self.limite is True) and (self.chances > 0):
                self.diminuirChances()

            raise Exception("Palavra errada")

    def showDisplay(self):
        return "".join(self.palavraStatus)

    def ganharOJogo(self):
        self.ganho = True
        self.finalizado = True

    def perderOJogo(self):
        self.chances = 0
        self.perdido = True
        self.finalizado = True

    def diminuirChances(self):
        if self.limite is True and self.chances > 0:
            self.chances -= 1
        else:
            raise Exception("Erro inesperado em diminuirChances()")

        if (self.chances == 0):
            self.perderOJogo()

    def aumentarChances(self):
        # In case.

        if self.limite is True:
            self.chances += 1



