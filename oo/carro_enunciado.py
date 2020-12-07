"""Você deve criar uma classe carro que vai possuir 2 atributos compostos por outras duas classes:
1 - Motor
2 - Direção

O motor terá a responsabilidade de controlar a velocidade.
Ele oferece os seguintes atributos:
1 - Atributo de dado: velocidade
2 - Método acelerar, que deverá incrementar a velocidade de uma velocidade
3 - Método frear que deverá decrementar a velocidade em duas unidades

A direção terá a aresponsabilidade de controlar a direção. Ela oferece os seguintes atributos:
1 - Valor de direção com valores possíveis: Norte, Sul, Leste, Oeste.
2 - Método girar a direita
2 - Método girar a esquerda

  N
O   L    - Virar a direita significa a mudança na seguinte sequência N-L-S-O-N
  S      - Virar a esquerda: N-O-S-L

  Exemplo:
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
  >>> # Testando Direção()
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
  >>> carro = Carro(direcao, motor)
  >>>carro.calcular_velocidade()
  0
  >>>carro.acelerar()
  >>>carro.calcular_velocidade()
  1
  >>>carro.acelerar()
  >>>carro.calcular_velocidade()
  2
  >>>carro.acelerar()
  >>>carro.calcular_velocidade()
  0
  >>>carro.calcular.direcao()
  'Norte'
  >>>carro.girar_a_direita()
  >>>carro.calcular.direcao()
  'Leste'
  >>>carro.girar_a_esquerda()
  >>>carro.calcular.direcao()
  'Norte'
  >>>carro.girar_a_esquerda()
  >>>carro.calcular.direcao()
  'Oeste'
"""