from unittest import TestCase
from oo.carro_minha_solucao import Motor


# as funções de teste devem iniciar com prefixo test, ou teste no português
class CarroTestCase(TestCase):
    def teste_velocidade_inicial(self):
        motor = Motor()
        self.assertEqual(0, motor.velocidade)  # testa se o valor motor.velocidade é igual a 0

    def teste_acelerar(self):
        motor = Motor()
        motor.acelerar()
        self.assertEqual(1, motor.velocidade)
