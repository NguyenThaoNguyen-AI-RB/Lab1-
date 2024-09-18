class Store:
    def __init__(self, name, store_type, capacity):
        self.name = name
        self.store_type = store_type
        self.capacity = capacity
        self.items = {}
    def from_size(self, name, type, size):
        return f"{self(name, type, size // 2)}"
    def add_item(self, item_name):
        if sum(self.items.values()) < self.capacity:
            if item_name in self.items:
                self.items[item_name] += 1
            else:
                self.items[item_name] = 1
            return f"{item_name} added to the store"
        return "Not enough capacity in the store"
    def remove_item(self, item_name, amount):
        if item_name in self.items and self.items[item_name] >= amount:
            self.items[item_name] -= amount
            if self.items[item_name] == 0:
                del self.items[item_name]
            return f"{amount} {item_name} removed from the store"
        return f"Cannot remove {amount} {item_name}"
    def __repr__(self):
        return f"{self.name} of type {self.store_type} with capacity {self.capacity}"

first_store = Store("First store", "Fruit and Veg", 20)
second_store = Store.from_size("Second store", "Clothes", 500)
print(first_store)  
print(second_store)  
print(first_store.add_item("potato"))  
print(second_store.add_item("jeans"))  
print(first_store.remove_item("tomatoes", 1))  
print(second_store.remove_item("jeans", 1)) 