# Os comandos escritos abaixos são utilizados para 'doctests', uma forma de testar o código a partir da interação a ser
# realizada no console, para utilizá-lo. basta clicar com o botão direito sobre o doctest e então na opção:
# Run 'Doctests in <this_name_file>'
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
  >>> direcao.valor
  'Norte'
  >>> direcao.girar_a_direita()
  >>> direcao.valor
  'Leste'
  >>> direcao.girar_a_direita()
  >>> direcao.valor
  'Sul'
  >>> direcao.girar_a_direita()
  >>> direcao.valor
  'Oeste'
  >>> direcao.girar_a_direita()
  >>> direcao.valor
  'Norte'
  >>> direcao.girar_a_esquerda()
  >>> direcao.valor
  'Oeste'
  >>> direcao.girar_a_esquerda()
  >>> direcao.valor
  'Sul'
   >>> direcao.girar_a_esquerda()
  >>> direcao.valor
  'Leste'
   >>> direcao.girar_a_esquerda()
  >>> direcao.valor
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
        self.direcao = direcao
        self.motor = motor

    def calcular_velocidade(self):
        return self.motor.velocidade

    def acelerar(self):
        self.motor.acelerar()

    def frear(self):
        self.motor.frear()

    def calcular_direcao(self):
        return self.direcao.valor

    def girar_a_esquerda(self):
        self.direcao.girar_a_esquerda()

    def girar_a_direita(self):
        self.direcao.girar_a_direita()



class Motor:
    def __init__(self):
        self.velocidade = 0

    def acelerar(self):
        self.velocidade += 1

    def frear(self):
        self.velocidade -= 2
        # função max abaixo retorna o maior valor dentre os parâmetros especificados, desta forma, caso a velocidade
        # retornada na iteração acima seja 'menor que zero', então o valor atribuido pela iteração abaixo será '0'.
        self.velocidade = max(0, self.velocidade)


# por convenção da PEP8, uma constante (var que não deve ser alterada) é escrita em letra maiúcula
NORTE = 'Norte'
LESTE = 'Leste'
SUL = 'Sul'
OESTE = 'Oeste'


class Direcao:
    rotacao_a_direita_dict = {NORTE: LESTE, LESTE: SUL, SUL: OESTE, OESTE: NORTE}
    rotacao_a_esquerda_dict = {NORTE: OESTE, OESTE: SUL, SUL: LESTE, LESTE: NORTE}

    def __init__(self):
        self.valor = NORTE

    def girar_a_direita(self):
        self.valor = self.rotacao_a_direita_dict[self.valor]

    def girar_a_esquerda(self):
        self.valor = self.rotacao_a_esquerda_dict[self.valor]
