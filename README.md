# ProjectZPO
@startuml
abstract class Server { 
    - n_max_returned_entries: int 
    + __init__(self, name: str, price: float) 
    + abstract all_products(): List[Product] 
    + get_entries(n_letters: int): List[Product] 
}

class MapServer { 
    + __init__(self, products: List[Product], *args, **kwargs)) 
    + all_products(): Dict[Product] 
    + products: Dict[str, Product]
}

class ListServer { 
    + __init__(self, products: List[Product], *args, **kwargs)) 
    + all_products(): List[Product] 
    + products: List[Product]
}

class Client { 
    + __init__(self, server: BaseOrDerivedT) 
    + get_total_price(n_letters: int): float  
    + server: Server
}

class Product { 
    + name: str 
    + price: float 
    + __init__(self, name: str, price: float) 
    + __eq__(self, other: Product) 
    + __hash__(self) 
}

class Exception {
}

class TooManyProductsFoundError {
}

Server <|-- ListServer 
Server <|-- MapServer 
Client o-- Server 
MapServer o-- Product 
ListServer o-- Product
Exception <|-- TooManyProductsFoundError
TooManyProductsFoundError <.. Server : "<< throws >>"

@enduml
