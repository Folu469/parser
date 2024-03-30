from dataclasses import dataclass


@dataclass
class Product:
    sku: int
    name: str
    href: str
    price: float
