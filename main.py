class Cart():
    def __init__(self):
        self.items = {}
        
    def add(self, name, quantity, price):
        if name in self.items:
            self.items[name].quantity += quantity
        else:
            new_item = Item(name, quantity, price)

            self.items[name] = new_item
            
    def show(self):
        print("=~" * 15)
        print("SHOPPING CART:")

        for key, val in self.items.items():
            total = val.quantity * val.price
            print(f"{key.title()} x{val.quantity}: ${'{:.2f}'.format(total)}")

        print("=~" * 15)
        
    def delete(self, item_to_delete):
        del self.items[item_to_delete]
    
# My actual products (banana, apple)
class Item():
    def __init__(self, name, quantity, price):
        self.name = name
        self.quantity = quantity
        self.price = price

# Main class, that handles user input and works with the other classes
class Shop():
    def __init__(self):
        self.cart = Cart()
    
    def main(self):
        while True:
            user_choice = input("Choose an Option (add/view/delete/quit): ").lower()

            if user_choice == 'add':
                name = input("Product Name: ").lower()
                quantity = int(input("Product Quantity: "))
                price = float(input("Product Price: "))

                self.cart.add(name, quantity, price)
            elif user_choice == 'view':
                self.cart.show()
            elif user_choice == 'delete':
                name = input("What product do you want to delete? ").lower()

                self.cart.delete(name)
            elif user_choice == 'quit':
                self.cart.show()
                break
            else:
                print("Invalid input, please try again.")