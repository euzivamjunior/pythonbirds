"""
  #Testando motor
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

  # Testando Direção()
  >>> direcao = Direcao()
  >>> direcao.direcao
  'Norte'
  >>> direcao.girar_a_direita()
  >>> direcao.direcao
  'Leste'
  >>> direcao.girar_a_direita()
  >>> direcao.direcao
  'Sul'
  >>> direcao.girar_a_direita()
  >>> direcao.direcao
  'Oeste'
  >>> direcao.girar_a_direita()
  >>> direcao.direcao
  'Norte'
  >>> direcao.girar_a_esquerda()
  >>> direcao.direcao
  'Oeste'
  >>> direcao.girar_a_esquerda()
  >>> direcao.direcao
  'Sul'
   >>> direcao.girar_a_esquerda()
  >>> direcao.direcao
  'Leste'
   >>> direcao.girar_a_esquerda()
  >>> direcao.direcao
  'Norte'

  # Testando Carro
  >>> carro = Carro(direcao, motor)
  >>> carro.calcular_velocidade
  0
  >>> carro.acelerar()
  >>> carro.calcular_velocidade
  1
  >>> carro.acelerar()
  >>> carro.calcular_velocidade
  2
  >>> carro.acelerar()
  >>> carro.calcular_velocidade
  3
  >>> carro.calcular_direcao
  'Norte'
  >>> carro.girar_a_direita()
  >>> carro.calcular_direcao
  'Leste'
  >>> carro.girar_a_esquerda()
  >>> carro.calcular_direcao
  'Norte'
  >>> carro.girar_a_esquerda()
  >>> carro.calcular_direcao
  'Oeste'
"""


class Carro:
    def __init__(self, direcao, motor):
        self.calcular_velocidade = motor.velocidade
        self.calcular_direcao = direcao.direcao

    def acelerar(self):
        motor.acelerar()
        self.calcular_velocidade = motor.velocidade

    def frear(self):
        motor.frear()
        self.calcular_velocidade = motor.velocidade

    def girar_a_direita(self):
        direcao.girar_a_direita()
        self.calcular_direcao = direcao.direcao

    def girar_a_esquerda(self):
        direcao.girar_a_esquerda()
        self.calcular_direcao = direcao.direcao


class Motor:
    def __init__(self, velocidade=0):
        self.velocidade = velocidade

    def acelerar(self):
        self.velocidade += 1

    def frear(self):
        if self.velocidade >= 2:
            self.velocidade -= 2
        else:
            self.velocidade = 0


class Direcao:
    def __init__(self, direcao='Norte'):
        self.direcao = direcao
        self.direita = {'Norte': 'Leste', 'Leste': 'Sul', 'Sul': 'Oeste', 'Oeste': 'Norte'}
        self.esquerda = {'Norte': 'Oeste', 'Oeste': 'Sul', 'Sul': 'Leste', 'Leste': 'Norte'}

    def girar_a_direita(self):
        self.direcao = self.direita[self.direcao]

    def girar_a_esquerda(self):
        self.direcao = self.esquerda[self.direcao]
