class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class Cart:
    def __init__(self):
        self.items = {}

    def add_product(self, product, quantity):
        if product.name in self.items:
            self.items[product.name]['quantity'] += quantity
        else:
            self.items[product.name] = {'product': product, 'quantity': quantity}

    def compute_total(self):
        total = 0
        for item in self.items.values():
            total += item['product'].price * item['quantity']
        return total

    def compute_discount(self, total):
        # Assuming a flat discount of 10% for this example
        discount = total * 0.10
        return discount

    def compute_vat(self, total):
        vat = total * 0.075  # 7.5% VAT
        return vat

    def generate_invoice(self):
        total = self.compute_total()
        discount = self.compute_discount(total)
        vat = self.compute_vat(total)
        final_total = total - discount + vat

        print("\n--- Invoice ---")
        for item in self.items.values():
            product = item['product']
            quantity = item['quantity']
            print(f"{product.name} (x{quantity}): ${product.price:.2f} each - Total: ${product.price * quantity:.2f}")

        print(f"\nSubtotal: ${total:.2f}")
        print(f"Discount: -${discount:.2f}")
        print(f"VAT (7.5%): +${vat:.2f}")
        print(f"Total Amount Due: ${final_total:.2f}")

def main():
    cart = Cart()
    
    while True:
        product_name = input("Enter product name (or 'done' to finish): ")
        if product_name.lower() == 'done':
            break
        product_price = float(input(f"Enter price for {product_name}: $"))
        product_quantity = int(input(f"Enter quantity for {product_name}: "))
        
        product = Product(product_name, product_price)
        cart.add_product(product, product_quantity)

    cart.generate_invoice()

if __name__ == "__main__":
    main()