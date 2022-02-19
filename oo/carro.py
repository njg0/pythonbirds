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
    >>> motor.velocidade()
    2
    >>> motor.acelerar
    >>> motor.velocidade
    3
    >>> motor.frear()
    >>> motor.velocidade()
    1
    >>> motor.frear()
    >>> motor.velocidade()
    0
    >>> direcao = Direcao()
    >>> direcao.valor
    "Norte"
    >>> direcao.girar_a_direita()
    >>> direcao.valor
    "Leste"
    >>> direcao.girar_a_direita()
    >>> direcao.valor
    "Sul"
    >>> direcao.girar_a_direita()
    >>> direcao.valor
    "Oeste"
    >>> direcao.girar_a_direita()
    >>> direcao.valor
    "Norte" #mod direcao = 0
    >>> direcao.girar_a_esquerda()
    >>> direcao.valor
    "Oeste" #mod direcao = 1
    >>> direcao.girar_a_esquerda()
    >>> direcao.valor
    "Sul" #mod direcao = 2
    >>> direcao.girar_a_esquerda()
    >>> direcao.valor
    "Leste" #mod direcao = 3
    >>> direcao.girar_a_esquerda()
    >>> direcao.valor
    "Norte"
    >>> carro = Carro(direcao,motor)
"""
from pessoa import Pessoa

class Motor:
    def __init__(self):
        self.velocidade = 0

    def acelerar(self):
        self.velocidade += 1

    def desacelerar(self):
        if self.velocidade <= 1:
            self.velocidade = 0
        else:
            self.velocidade -= 2

    def velocidade(self):
        return self.velocidade()

class Carro:
    pneus = 5

    def __init__(self, *passageiros, modelo=None, motor, direcao):
        self.modelo = modelo
        self.motor = Motor
        self.direcao = direcao
        self.passageiros = list(Pessoa)


    def check_direcao(self):
        return self.direcao

    def virar_direita(self):
        self.direcao = self.direcao + 1

    def virar_esquerda(self):
        self.direcao = self.direcao - 1

