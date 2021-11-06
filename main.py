# !/usr/bin/python
# -*- coding: utf-8 -*-

from typing import Optional, List, TypeVar, Dict
from abc import ABC, abstractmethod


class Product:
    # FIXME: klasa powinna posiadać metodę inicjalizacyjną przyjmującą argumenty wyrażające nazwę produktu (typu str) i jego cenę (typu float) -- w takiej kolejności -- i ustawiającą atrybuty `name` (typu str) oraz `price` (typu float)

    def __init__(self, name: str, price: float):
        self.name: str = name
        self.price: float = price

    def __eq__(self, other):
        if isinstance(other, Product):
            return self.name == other.name and self.price == other.price  # FIXME: zwróć odpowiednią wartość
        return False

    def __hash__(self):
        return hash((self.name, self.price))


class Error(Exception):
    pass

class TooManyProductsFoundError(Error):
    # Reprezentuje wyjątek związany ze znalezieniem zbyt dużej liczby produktów.
    pass


# FIXME: Każada z poniższych klas serwerów powinna posiadać:
#   (1) metodę inicjalizacyjną przyjmującą listę obiektów typu `Product` i ustawiającą atrybut `products` zgodnie z typem reprezentacji produktów na danym serwerze,
#   (2) możliwość odwołania się do atrybutu klasowego `n_max_returned_entries` (typu int) wyrażający maksymalną dopuszczalną liczbę wyników wyszukiwania,
#   (3) możliwość odwołania się do metody `get_entries(self, n_letters)` zwracającą listę produktów spełniających kryterium wyszukiwania

class Server(ABC):
    n_max_returned_entries = 5
    def __init__(self, *args, **kwargs):
        super().__init__()

    def get_entries(self, n_letters: int = 1) -> List[Product]:
        name_pat = '^[a-zA-Z]{{{0}}}\\d{{3,3}}$'.format(n_letters)
        entries = [product for product in self.all_products(n_letters) if ]

    @abstractmethod
    def all_products(self, n_letters: int = 1) -> List[Product]:
        raise NotImplementedError


BaseOrDerivedT = TypeVar('BaseOrDerivedT', bound=Server)

class ListServer(Server):
    def __init__(self, products: List[Product], *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.products: List[Product] = products

    def all_products(self, n_letters: int = 1) -> List[Product]:
        return self.products


class MapServer(Server):
    def __init__(self, products: List[Product], *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.products: Dict[str, Product] = {product.name: product.price for product in products}

    def all_products(self, n_letters: int = 1) -> List[Product]:
        return list(self.products.values())


class Client:
    # FIXME: klasa powinna posiadać metodę inicjalizacyjną przyjmującą obiekt reprezentujący serwer

    def get_total_price(self, n_letters: Optional[int]) -> Optional[float]:
        raise NotImplementedError()

