class MenuItem:
    def __init__(self, name: str, price: float, category: str):
        self.name = name
        self.price = price
        self.category = category

    def __str__(self) -> str:
        return f"{self.name} : {self.price} EGP"

MENU_ITEMS = [
    MenuItem("meat", 280, "Main"),
    MenuItem("chicken", 185, "Main"),
    MenuItem("rice", 30, "Main"),
    MenuItem("pasta", 80, "Main"),
    MenuItem("fish", 200, "Main"),
    MenuItem("water", 15, "Extra"),
    MenuItem("tea", 8, "Extra"),
    MenuItem("soda", 20, "Extra"),
    MenuItem("juice", 25, "Extra"),
]

class Table:
    def __init__(self, number: int) -> None: 
        self.number = number
        self._total: float = 0.0
        self.order: list[tuple[str, float]] = []
        self.vip: bool = False

    @property
    def total(self) -> float:
        if self.vip:
            return round(self._total * 0.9, 2)
        return self._total
    
    def add_to_total(self, amount: float) -> None:
        if amount < 0:
            raise ValueError("Amount cannot be negative")
        self._total += amount
 
    def add(self, name: str, price: float) -> None:
        self.order.append((name, price))
        self.add_to_total(price)

    def __str__(self) -> str:
        order_str = ' '.join([f'{name} : {price}' for name,price in self.order])
        return f"\nTable: {self.number}\nOrder: {order_str}\nTotal: {self.total}"
    
    def check(self) -> str:
        if not self.order:
            return "Error: No items in order to checkout!"
        receipt = f"--------\n{str(self)}\ncheck successfully"
        self.order = []
        self._total = 0.0
        self.vip = False
        return receipt
        
class Hall:
    def __init__(self, number: int):
        self.number = number
        self.tables: list[Table] = [Table(i) for i in range(1, 6)]