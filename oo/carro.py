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
"""
from pessoa import Pessoa

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
    pneus = 5

    def __init__(self):
        self.motor = Motor
        self.direcao = Direcao

    def virar_direita(self):
        self.direcao = self.direcao + 1

    def virar_esquerda(self):
        self.direcao = self.direcao - 1
