# -*- coding: utf-8 -*-
from itertools import chain
from atores import ATIVO

VITORIA = 'VITORIA'
DERROTA = 'DERROTA'
EM_ANDAMENTO = 'EM_ANDAMENTO'


class Ponto():
    def __init__(self, x, y, caracter):
        self.caracter = caracter
        self.x = round(x)
        self.y = round(y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y and self.caracter == other.caracter

    def __hash__(self):
        return hash(self.x) ^ hash(self.y)

    def __repr__(self, *args, **kwargs):
        return "Ponto(%s,%s,'%s')" % (self.x, self.y, self.caracter)


class Fase():
    def __init__(self, intervalo_de_colisao=1):
        """
        Método que inicializa uma fase.

        :param intervalo_de_colisao:
        """
        self.intervalo_de_colisao = intervalo_de_colisao
        # por convenção, quando um atributo começa por <_>, isso significa que tal atributo não
        # ser acessado diretamente (ideia de atributo protegido)
        self._passaros = []
        self._porcos = []
        self._obstaculos = []

    def adicionar_obstaculo(self, *obstaculos):
        """
        Adiciona obstáculos em uma fase

        :param obstaculos:
        """
        self._obstaculos.extend(obstaculos)

    def adicionar_porco(self, *porcos):
        """
        Adiciona porcos em uma fase

        :param porcos:
        """
        self._porcos.extend(porcos)

    def adicionar_passaro(self, *passaros):
        """
        Adiciona pássaros em uma fase

        :param passaros:
        """
        self._passaros.extend(passaros)

    def status(self):
        """
        Método que indica com mensagem o status do jogo

        Se o jogo está em andamento (ainda tem porco ativo e pássaro ativo), retorna essa mensagem.

        Se o jogo acabou com derrota (ainda existe porco ativo), retorna essa mensagem

        Se o jogo acabou com vitória (não existe porco ativo), retorna essa mensagem

        :return:
        """
        # método protegido: _metodo(): apenas classe ou subclasse pode usar esse metodo
        # em python isso indica que não deve ser usado fora desse contexto, mas não há
        # nenhum impedimento de fato, pois o método continua do mesmo jeito.
        if not self._possui_porco_ativo():
            return VITORIA
        elif self._possui_passaros_ativos():
            return EM_ANDAMENTO
        else:
            return DERROTA

    def lancar(self, angulo, tempo):
        """
        Método que executa lógica de lançamento.

        Deve escolher o primeiro pássaro não lançado da lista e chamar seu método lançar

        Se não houver esse tipo de pássaro, não deve fazer nada

        :param angulo: ângulo de lançamento
        :param tempo: Tempo de lançamento
        """
        pass

    def calcular_pontos(self, tempo):
        """
        Lógica que retorna os pontos a serem exibidos na tela.

        Cada ator deve ser transformado em um Ponto.

        :param tempo: tempo para o qual devem ser calculados os pontos
        :return: objeto do tipo Ponto
        """
        pontos = [self._transformar_em_ponto(a) for a in self._passaros + self._obstaculos + self._porcos]

        return pontos

    def _transformar_em_ponto(self, ator):
        return Ponto(ator.x, ator.y, ator.caracter())

    def _possui_porco_ativo(self):
        # caso haja 'pelo menos um' porco ativo no jogo, retorna True, caso não, False
        for porco in self._porcos:
            if porco.status == ATIVO:
                return True
        return False

    def _possui_passaros_ativos(self):
        # caso haja 'pelo menos um' passaro ativo no jogo, retorna True, caso não, False
        for passaro in self._passaros:
            if passaro.status == ATIVO:
                return True
        return False
