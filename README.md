# ProjectZPO
@startuml
abstract class Server {
    - n_max_returned_entries: int
    + __init__(name: str, price: float)
    + abstract all_products(): List[Product]
    + get_entries(n_letters: int): List[Product]
}

class MapServer {
    + __init__(products: List[Product])
    + all_products(): Dict[Product]
}

class ListServer {
    + __init__(products: List[Product])
    + all_products(): List[Product]
}

class Client {
    + __init__(server)
    + get_total_price(n_letters: int): float
    _ n_letters: int
}

class Product {
    - name: str
    - price: float
    + __init__(name: str, price: float)
    + __eq__(other: Product)
    + __hash__()
}

Server <|-- ListServer
Server <|-- MapServer
Client o-- Server
Server o-- Product
@enduml
