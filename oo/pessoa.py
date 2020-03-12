class Pessoa:
    olhos = 2

    def __init__(self, *filhos, nome=None, idade=None):
        self.nome = nome
        self.idade = idade
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {id(self)}'


if __name__ == '__main__':
    sarah = Pessoa(nome='Sarah', idade=24)
    laura = Pessoa(nome='Laura', idade=1)
    geraldo = Pessoa(sarah, laura, nome='Geraldo', idade=48)
    print(Pessoa.cumprimentar(geraldo))
    print(id(geraldo))
    print(geraldo.cumprimentar())
    print(geraldo.nome)
    print(geraldo.idade)
    for filho in geraldo.filhos:
        print(filho.nome)
    print()
    print('Será incluído o atributo Sobrenome dinamicamente:')
    geraldo.sobrenome = 'Zamparo' # inclui atributo dinamicamente
    print(f'{geraldo.nome} {geraldo.sobrenome}')
    print(geraldo.__dict__)
    print(sarah.__dict__)
    print(laura.__dict__)
    print('Será excluído o atributo Sobrenome dinamicamente:')
    del geraldo.sobrenome  # excluído atributo dinamicamente
    print(geraldo.__dict__)
    print()
    geraldo.olhos = 3
    print('Foi criado um atributo Olhos especificamente para o Geraldo:')
    print('Classe', ' - Qtde de Olhos: ',Pessoa.olhos, ' - Id dos olhos: ', id(Pessoa.olhos))
    print('Geraldo', ' - Qtde de Olhos: ',geraldo.olhos, ' - Id dos olhos: ', id(geraldo.olhos))
    print('Sarah', ' - Qtde de Olhos: ',sarah.olhos, ' - Id dos olhos: ', id(sarah.olhos))
    print('Laura', ' - Qtde de Olhos: ',laura.olhos, ' - Id dos olhos: ', id(laura.olhos))
    print()
    Pessoa.olhos = 3.5
    print('mudou a qtde de olhos da classe de 2 para 3.5:')
    print('Classe', ' - Qtde de Olhos: ', Pessoa.olhos, ' - Id dos olhos: ', id(Pessoa.olhos))
    print('Geraldo', ' - Qtde de Olhos: ', geraldo.olhos, ' - Id dos olhos: ', id(geraldo.olhos))
    print('Sarah', ' - Qtde de Olhos: ', sarah.olhos, ' - Id dos olhos: ', id(sarah.olhos))
    print('Laura', ' - Qtde de Olhos: ', laura.olhos, ' - Id dos olhos: ', id(laura.olhos))
    print()
    print('mudando todas as qtdes de olhos para 2 e excluída o atributo exclusivo Olhos do Geraldo, ficando padrão:')
    del geraldo.olhos
    Pessoa.olhos = 2
    print('Classe', ' - Qtde de Olhos: ', Pessoa.olhos, ' - Id dos olhos: ', id(Pessoa.olhos))
    print('Geraldo', ' - Qtde de Olhos: ', geraldo.olhos, ' - Id dos olhos: ', id(geraldo.olhos))
    print('Sarah', ' - Qtde de Olhos: ', sarah.olhos, ' - Id dos olhos: ', id(sarah.olhos))
    print('Laura', ' - Qtde de Olhos: ', laura.olhos, ' - Id dos olhos: ', id(laura.olhos))