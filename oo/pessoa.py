class Pessoa:
    """ quando criamos um atributo diretamente dentro de uma classe, fora do método __init__, este é chamado de
    'atributo default' ou 'atributo de classe'. esse tipo de atribuição é um valor padrão para todos os objetos deste
    tipo de classe, tal padrão é utilizado para evitar a atribuição de memória para este atributo para cada um dos
    objetos criados a partir desta classe Pessoa, assim uma unica alocação é feita para o atributo olhos e este
    pertence por padrão a todos os objetos da classe. Como exemplo temos o caso abaixo do atributo olhos, que possui
    valor padrão 2 para todos objetos criados a partir da classe Pessoa.
    """
    olhos = 2

    def __init__(self, *filhos, nome=None, idade=35):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá, meu nome é {self.nome}'

    """decorators (espécie de métodos de classe): funciona como uma função simples atrelada a classe pessoa, por isso 
    independe do objeto, dessa forma não é necessário receber nenhum atributo.
     """

    @staticmethod
    def metodo_estatico():
        return 42

    @classmethod
    def nome_e_atributos_de_classe(cls):
        return f'{cls} - olhos {cls.olhos}'


class Homem(Pessoa):
    def cumprimentar(self):
        # recebe o retorno do método cumprimentar da classe Pessoa (especificamente dela)
        #cumprimentar_da_classe = Pessoa.cumprimentar(self)

        # recebe o retorno do método cumprimentar da classe Pai (Da quel essa classe herda)
        cumprimentar_da_classe = super().cumprimentar()
        return f'{cumprimentar_da_classe}. Aperto de mão'


class Mutante(Pessoa):
    # sobrescrevendo um atributo da classe Pai, ao criar um atributo com o mesmo nome na classe filho
    olhos = 3


if __name__ == '__main__':
    random = Mutante(nome='Random', idade=20)
    luciano = Homem(random, nome='Luciano')
    print(Pessoa.cumprimentar(luciano))
    print(id(luciano))
    print(luciano.cumprimentar())
    print(luciano.nome)
    print(luciano.idade)
    print(luciano.filhos)

    for filho in luciano.filhos:
        print(filho.nome)
        print(filho.idade)

    # podemos adicionar um novo atributo (fora do escopo init a um objeto)
    luciano.sobrenome = 'Ramalho'
    print(luciano.sobrenome)

    # podemos remover um atributo de um dado objeto
    del luciano.filhos

    """ Apesar de ser possível sua utilização, criar ou deletar um atributo durante tempo de execução não costuma ser 
    uma boa prática, o ideal é que os atributos estejam dentro do __init__. Porém tal fucionalidade pode ser util, 
    quando por exemplo, queremos utilizar um valor em formato específico para uma dada requisição específica, e não 
    para toda a aplicação como um todo.
    """

    """ Os unicos atributos que fazem parte do __dict_ de um objeto são aqueles contidos em __init__, ou um atributo de 
    classe que seja alterado para tal objeto, caso contrário o mesmo não será retornado no dicionário de atributos do 
    objeto
    """
    # consultar os atributos de um objeto
    luciano.olhos = 1
    print(luciano.__dict__)
    print(random.__dict__)

    """No caso de atributos de classe, este pode ser acessado diretamente a partir da  classe, diferentemente dos 
    atributos contidos em __init__. Note também que o id do atributo olhos todos os objetos da classe Pessoa é o mesmo.
    """
    print('Valor atributo olhos: {}, id: {}'.format(Pessoa.olhos, id(Pessoa.olhos)))
    print('Valor atributo olhos: {}, id: {}'.format(luciano.olhos, id(luciano.olhos)))
    print('Valor atributo olhos: {}, id: {}'.format(random.olhos, id(luciano.olhos)))

    """Assim como no caso de atributos de classe, os decorators também pode ser acessador a partir da própria
    classe.
    """
    print('Valor retornado pelo método estático: {}'.format(Pessoa.metodo_estatico()))
    print('Valor retornado pelo método estático: {}'.format(luciano.metodo_estatico()))

    print('Nome da classe e atributo olhos: {}'.format(Pessoa.nome_e_atributos_de_classe()))
    print('Nome da classe e atributo olhos: {}'.format(luciano.nome_e_atributos_de_classe()))

    # Objeto pessoa pertence a classe Pessoa, mas não pertence a classe Homem
    pessoa = Pessoa('Anonimo')
    print('Objeto pessoa faz parte da classe Pessoa: {}'.format(isinstance(pessoa, Pessoa)))
    print('Objeto pessoa faz parte da classe Homem: {}'.format(isinstance(pessoa, Homem)))

    # Objeto random pertence tanto a classe Homem, quanto Pessoa devido a herança
    print('Objeto random faz parte da classe Pessoa: {}'.format(isinstance(random, Pessoa)))
    print('Objeto random faz parte da classe Homem: {}'.format(isinstance(random, Homem)))

    print(random.olhos)

    print(luciano.cumprimentar())
    print(random.cumprimentar())