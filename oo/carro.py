""" Você deve criar uma classe carro que vai possuir
dois atributos compostos por outras duas classes
1) Motor
2) Direção

O Motor terá a responsabilidade de controlar a velocidade.
Ele oferece os seguintes atributos:
1) Atributo de dado: velocidade
2) Método acelerar, que deverá incrementar a velocidade em uma unidade
3) Método frear, que deverá decrementar a velocidade em duas unidades

A direção terá a reponsabilidade de controlar a direção. Ela oferece
os seguintes atributos:
1) Valor da direção com os valores possíveis: Norte, Sul, Leste, Oeste
2) Método girar a direita
3) Método girar a esquerda
  N
O   L
  S
    Exemplo:
    >>> motor = Motor()
    >>> motor.velocidade
    0
    >>> motor.acelerar()
    >>> motor.velocidade
    1
    >>> motor.acelerar()
    >>> motor.velocidade
    2
    >>> motor.acelerar()
    >>> motor.velocidade
    3
    >>> motor.frear()
    >>> motor.velocidade
    1
    >>> motor.frear()
    >>> motor.velocidade
    0
    >>> direcao = Direcao()
    >>> direcao.valor
    'Norte'
    >>> direcao.girar('Direita')
    >>> direcao.valor
    'Leste'
    >>> direcao.girar('Direita')
    >>> direcao.valor
    'Sul'
    >>> direcao.girar('Direita')
    >>> direcao.valor
    'Oeste'
    >>> direcao.girar('Direita')
    >>> direcao.valor
    'Norte'
    >>> direcao.girar('Esquerda')
    >>> direcao.valor
    'Oeste'
    >>> direcao.girar('Esquerda')
    >>> direcao.valor
    'Sul'
    >>> direcao.girar('Esquerda')
    >>> direcao.valor
    'Leste'
    >>> direcao.girar('Esquerda')
    >>> direcao.valor
    'Norte'
    >>> carro = Carro(direcao,motor)
    >>> carro.calcular_velocidade()
    0
    >>> carro.acelerar()
    >>> carro.calcular_velocidade()
    1
    >>> carro.acelerar()
    >>> carro.calcular_velocidade()
    2
    >>> carro.frear()
    >>> carro.calcular_velocidade()
    0
    >>> carro.calcular_direcao()
    'Norte'
    >>> carro.girar('Direita')
    >>> carro.calcular_direcao()
    'Leste'
    >>> carro.girar('Esquerda')
    >>> carro.calcular_direcao()
    'Norte'
    >>> carro.girar('Esquerda')
    >>> carro.calcular_direcao()
    'Oeste'

"""

class Motor:
    def __init__(self):
        self.velocidade = 0

    def acelerar(self):
        self.velocidade += 1

    def frear(self):
        if self.velocidade <= 1:
            self.velocidade = 0
        else:
            self.velocidade -= 2

class Direcao:

    def __init__(self):
        self.valor = 'Norte'

    def girar(self, direcao): #Converte direção em número
        if self.valor == 'Norte':
            self.valor = 0
        elif self.valor == 'Leste':
            self.valor = 1
        elif self.valor == 'Sul':
            self.valor = 2
        elif self.valor == 'Oeste':
            self.valor = 3
        else:
            self.valor = 'Direção inválida'

        #Uma solução mais elegante para tratar a direção
        #Proposta pelo professor Renzo seria criar dois dicionários
        #Um com as direções apontando o sentido horário
        #E outro com as direções apontando sentido anti-horário
        #Vou manter o programa do jeito que está por que foi essa solução
        #Que eu mesmo desenvolvi e está satisfatória
        if direcao == 'Direita':
            self.valor += 1
        else:
            self.valor -= 1

        if self.valor % 4 == 0:
            self.valor = 'Norte'
        elif self.valor % 4 == 1:
            self.valor = 'Leste'
        elif self.valor % 4 == 2:
            self.valor = 'Sul'
        elif self.valor % 4 == 3:
            self.valor = 'Oeste'

class Carro:

    def __init__(self, direcao, motor):
        self.motor = motor
        self.direcao = direcao

    def calcular_velocidade(self):
        return self.motor.velocidade

    def girar(self, direcao):
        self.direcao.girar(direcao)

    def acelerar(self):
        self.motor.acelerar()

    def frear(self):
        self.motor.frear()

    def calcular_direcao(self):
        return self.direcao.valor
