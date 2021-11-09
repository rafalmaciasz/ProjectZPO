# !/usr/bin/python
# -*- coding: utf-8 -*-

from typing import Optional, List, TypeVar, Dict
from abc import ABC, abstractmethod
import re


class Product:

    def __init__(self, name: str, price: float) -> None:
        self.name: str = name
        self.price: float = price

    def __eq__(self, other):
        if isinstance(other, Product):
            return self.name == other.name and self.price == other.price
        return False

    def __hash__(self):
        return hash((self.name, self.price))


class TooManyProductsFoundError(Exception):
    pass


class Server(ABC):
    n_max_returned_entries: int = 5

    def __init__(self, *args, **kwargs) -> None:
        super().__init__()

    def get_entries(self, n_letters: int = 1) -> List[Product]:
        name_pat = '^[a-zA-Z]{{{n}}}\\d{{2,4}}$'.format(n=n_letters)
        entries = [product for product in self.all_products() if re.fullmatch(name_pat, product.name)]
        if len(entries) > Server.n_max_returned_entries: raise TooManyProductsFoundError
        return sorted(entries, key=lambda entry: entry.price)

    @abstractmethod
    def all_products(self) -> List[Product]:
        raise NotImplementedError


class ListServer(Server):

    def __init__(self, products: List[Product], *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.products: List[Product] = products

    def all_products(self) -> List[Product]:
        return self.products


class MapServer(Server):

    def __init__(self, products: List[Product], *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.products: Dict[str, Product] = {product.name: product for product in products}

    def all_products(self) -> List[Product]:
        return list(self.products.values())


BaseOrDerivedT = TypeVar('BaseOrDerivedT', bound=Server)


class Client:

    def __init__(self, server: BaseOrDerivedT) -> None:
        self.server: BaseOrDerivedT = server

    def get_total_price(self, n_letters: Optional[int]) -> Optional[float]:
        try:
            total: float = 0.0

            if n_letters is None:
                items = self.server.get_entries()
            else:
                items = self.server.get_entries(n_letters)

            if len(items) == 0:
                return None
            else:
                total = sum([item.price for item in items])
                
                return total

        except TooManyProductsFoundError:
            return None
