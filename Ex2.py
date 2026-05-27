class Pizza:
    def __init__(self, name, price):
        self.name = name
        self.price = price
        self.toppings = []

    def add_topping(self, topping):
        self.toppings.append(topping)

    def pizza_price(self):
        toppings_sum = 0
        for topping in self.toppings:
            toppings_sum += topping.price
        total_price = self.price + toppings_sum

        return total_price

    def show_pizza(self):
        print(f"Pizza: {self.name} (Basic price: {self.price} zł)")
        if self.toppings:
            print("Toppings:")
            for topping in self.toppings:
                print(f"- {topping.name}: {topping.price} zł")

        print(f"/// Pizza total: {self.pizza_price()} zł \n")


class Topping:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class Order:
    def __init__(self, customer):
        self.customer = customer
        self.pizzas = []

    def add_pizza(self, pizza):
        self.pizzas.append(pizza)

    def order_price(self):
        total_order_price = 0
        for pizza in self.pizzas:
            total_order_price += pizza.pizza_price()

        return total_order_price

    def show_order(self):
        print("Order summary")
        print(f"/// Customer: {self.customer.name} {self.customer.surname} \n")
        for pizza in self.pizzas:
            pizza.show_pizza()
        print(f"/// Total order price {self.order_price()} zł \n")

class Customer:
    def __init__(self, name, surname, address, phone, email):
        self.name = name
        self.surname = surname
        self.address = address
        self.phone = phone
        self.email = email

    def show_customer(self):
        print(
            f"Name: {self.name}\nSurname: {self.surname}\nAddress: {self.address} \nPhone: {self.phone} \nEmail: {self.email} \n")


# --- Code test ---

customer = Customer("Adam", "Smith", "Przygodzka 43, Jaworzno", "503784580", "adam.smith2006@gmail.com")
customer.show_customer()

cheese = Topping("Cheese", 3)
mushrooms = Topping("Mushrooms", 3)
ham = Topping("Ham", 5)

pizza1 = Pizza("Margarita", 25)
pizza2 = Pizza("Caprisiosa", 31)

pizza1.add_topping(ham)
pizza1.add_topping(mushrooms)
pizza2.add_topping(cheese)

order1 = Order(customer)
order1.add_pizza(pizza1)
order1.add_pizza(pizza2)

order1.show_order()