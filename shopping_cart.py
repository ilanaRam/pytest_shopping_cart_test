
from typing import List

class ShoppingCart: 
    """
        this is a format of writing, + adding a hint for the type
        instead of: 
        self.items = []
        we write
        self.items: List[str] = []
    """
    def __init__(self,max_size: int) -> None:                
        self.max_size = max_size
        self.items: List[str] = []        

    def add(self, item: str):        
        if self.size() == self.max_size: 
            raise OverflowError("Cannot add more items to cart")           
        
        self.items.append(item)        
        print(f"added new item ({item}), to a cart")

    def size(self) -> int:
        return len(self.items)

    def get_items(self) -> List[str]:
        return self.items
    
    def get_total_price(self, price_map):
        """
        The cart itself doesnt know the prices, so it needs third party map of prices from outside
        """
        total_price = 0
        for item in self.items:            
            total_price  += price_map.get(item)
        print(f"The total price is: {total_price}")
        return total_price
