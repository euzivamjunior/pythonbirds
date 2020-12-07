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
  >>> carro.calcular_velocidade()
  0
  >>> carro.acelerar()
  >>> carro.calcular_velocidade()
  1
  >>> carro.acelerar()
  >>> carro.calcular_velocidade()
  2
  >>> carro.acelerar()
  >>> carro.calcular_velocidade()
  3
  >>> carro.calcular_direcao()
  'Norte'
  >>> carro.girar_a_direita()
  >>> carro.calcular_direcao()
  'Leste'
  >>> carro.girar_a_esquerda()
  >>> carro.calcular_direcao()
  'Norte'
  >>> carro.girar_a_esquerda()
  >>> carro.calcular_direcao()
  'Oeste'
"""

class Carro:
    def __init__(self, direcao, motor):
        self.motor = motor
        self.direcao = direcao

    def calcular_velocidade(self):
        return self.motor.velocidade

    def acelerar(self):
        self.motor.acelerar()

    def frear(self):
        self.motor.frear()

    def calcular_direcao(self):
        return self.direcao.direcao

    def girar_a_direita(self):
        self.direcao.girar_a_direita()

    def girar_a_esquerda(self):
        self.direcao.girar_a_esquerda()


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


if __name__ == '__main__':
    motor_teste = Motor()

    print('\nTestando métodos e atributos Motor')
    print('Valor esperado velocidade: {} | Valor obtido: {}'.format(0, motor_teste.velocidade))
    motor_teste.acelerar()
    print('Valor esperado velocidade: {} | Valor obtido: {}'.format(1, motor_teste.velocidade))
    motor_teste.acelerar()
    print('Valor esperado velocidade: {} | Valor obtido: {}'.format(2, motor_teste.velocidade))
    motor_teste.acelerar()
    print('Valor esperado velocidade: {} | Valor obtido: {}'.format(3, motor_teste.velocidade))
    motor_teste.frear()
    print('Valor esperado velocidade: {} | Valor obtido: {}'.format(1, motor_teste.velocidade))
    motor_teste.frear()
    print('Valor esperado velocidade: {} | Valor obtido: {}'.format(0, motor_teste.velocidade))

    direcao_teste = Direcao()

    print('\nTestando métodos e atributos Direção')
    print('Valor esperado direção: {} | Valor obtido: {}'.format('Norte', direcao_teste.direcao))
    direcao_teste.girar_a_direita()
    print('Valor esperado direção: {} | Valor obtido: {}'.format('Leste', direcao_teste.direcao))
    direcao_teste.girar_a_direita()
    print('Valor esperado direção: {} | Valor obtido: {}'.format('Sul', direcao_teste.direcao))
    direcao_teste.girar_a_direita()
    print('Valor esperado direção: {} | Valor obtido: {}'.format('Oeste', direcao_teste.direcao))
    direcao_teste.girar_a_direita()
    print('Valor esperado direção: {} | Valor obtido: {}'.format('Norte', direcao_teste.direcao))
    direcao_teste.girar_a_esquerda()
    print('Valor esperado direção: {} | Valor obtido: {}'.format('Oeste', direcao_teste.direcao))
    direcao_teste.girar_a_esquerda()
    print('Valor esperado direção: {} | Valor obtido: {}'.format('Sul', direcao_teste.direcao))
    direcao_teste.girar_a_esquerda()
    print('Valor esperado direção: {} | Valor obtido: {}'.format('Leste', direcao_teste.direcao))
    direcao_teste.girar_a_esquerda()
    print('Valor esperado direção: {} | Valor obtido: {}'.format('Norte', direcao_teste.direcao))

    motor = Motor()
    direcao = Direcao()
    carro = Carro(direcao, motor)

    print('\nTestando métodos e atributos Carro')
    carro.acelerar()
    print('Valor esperado velocidade: {} | Valor obtido: {}'.format(1, carro.calcular_velocidade()))
    carro.acelerar()
    print('Valor esperado velocidade: {} | Valor obtido: {}'.format(2, carro.calcular_velocidade()))
    carro.frear()
    print('Valor esperado velocidade: {} | Valor obtido: {}'.format(0, carro.calcular_velocidade()))
    print('Valor esperado direção: {} | Valor obtido: {}'.format('Norte', carro.calcular_direcao()))
    carro.girar_a_direita()
    print('Valor esperado direção: {} | Valor obtido: {}'.format('Leste', carro.calcular_direcao()))
    carro.girar_a_esquerda()
    print('Valor esperado direção: {} | Valor obtido: {}'.format('Norte', carro.calcular_direcao()))
    carro.girar_a_esquerda()
    print('Valor esperado direção: {} | Valor obtido: {}'.format('Oeste', carro.calcular_direcao()))
