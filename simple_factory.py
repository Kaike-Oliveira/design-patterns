# Factory é responsável pela criação de objetos

from abc import ABC, abstractmethod


class Veiculo(ABC):
    @abstractmethod
    def buscar_cliente(self) -> None:
        pass


class CarroLuxo(Veiculo):
    def buscar_cliente(self) -> None:
        print('Carro de luxo buscando cliente...')


class CarroPopular(Veiculo):
    def buscar_cliente(self) -> None:
        print('Carro popular buscando cliente...')


class VeiculoFactory:
    @staticmethod
    def get_veiculo(tipo: str) -> Veiculo:
        carro = None
        if tipo == 'luxo':
            carro = CarroLuxo()
        elif tipo == 'popular':
            carro = CarroPopular()
        else:
            assert ('Veiculo inexistente')

        return carro


if __name__ == '__main__':
    from random import choice

    carros_disponiveis = ['luxo', 'popular']

    for i in range(10):
        carro = VeiculoFactory.get_veiculo(choice(carros_disponiveis))
        carro.buscar_cliente()
