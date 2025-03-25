class Item:
    def __init__(self, item_id: int, name: str, description: str, price: float):
        if not isinstance(item_id, int) or item_id <= 0:
            raise ValueError("Item ID must be a positive integer.")
        if not name.strip():
            raise ValueError("Name cannot be empty.")
        if price < 0:
            raise ValueError("Price cannot be negative.")
        
        self.item_id = item_id
        self.name = name
        self.description = description
        self.price = price
    
    def __str__(self):
        return f"ID: {self.item_id}, Name: {self.name}, Description: {self.description}, Price: ${self.price:.2f}"

class ItemManager:
    def __init__(self):
        self.items = {}
    
    def create_item(self):
        try:
            item_id = int(input("Enter item ID: "))
            if item_id in self.items:
                raise ValueError("Item ID already exists.")
            name = input("Enter item name: ")
            description = input("Enter item description: ")
            price = float(input("Enter item price: "))
            
            item = Item(item_id, name, description, price)
            self.items[item_id] = item
            print("Item added successfully.")
        except ValueError as e:
            print(f"Error: {e}")
    
    def read_items(self):
        if not self.items:
            print("No items available.")
        else:
            for item in self.items.values():
                print(item)
    
    def update_item(self):
        try:
            item_id = int(input("Enter item ID to update: "))
            if item_id not in self.items:
                raise ValueError("Item ID not found.")
            
            item = self.items[item_id]
            name = input("Enter new name (leave blank to keep current): ")
            description = input("Enter new description (leave blank to keep current): ")
            price_input = input("Enter new price (leave blank to keep current): ")
            
            if name:
                item.name = name
            if description:
                item.description = description
            if price_input:
                price = float(price_input)
                if price < 0:
                    raise ValueError("Price cannot be negative.")
                item.price = price
            
            print("Item updated successfully.")
        except ValueError as e:
            print(f"Error: {e}")
    
    def delete_item(self):
        try:
            item_id = int(input("Enter item ID to delete: "))
            if item_id not in self.items:
                raise ValueError("Item ID not found.")
            del self.items[item_id]
            print("Item deleted successfully.")
        except ValueError as e:
            print(f"Error: {e}")

    def menu(self):
        while True:
            print("\nItem Management System")
            print("1. Add Item")
            print("2. View Items")
            print("3. Update Item")
            print("4. Delete Item")
            print("5. Exit")
            
            choice = input("Enter your choice: ")
            
            if choice == "1":
                self.create_item()
            elif choice == "2":
                self.read_items()
            elif choice == "3":
                self.update_item()
            elif choice == "4":
                self.delete_item()
            elif choice == "5":
                print("Exiting application.")
                break
            else:
                print("Invalid choice. Please try again.")
