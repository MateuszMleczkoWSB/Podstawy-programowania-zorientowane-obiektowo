class Pizza:
    def __init__(self, name, price):
        self.name = name
        self.size = price

    def add_topping(self, topping):
        self.topping = topping

    def show_pizza(self):
        print(f"{self.name}")

class Topping:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class Order:
    def __init__(self, customer):
        self.customer = customer

    def add_pizza(self, pizza):
        self.pizza = pizza

    def show_order(self):
        print(f"")

class Customer:
    def __init__(self, name, surname, address, phone, email):
        self.name = name
        self.surname = surname
        self.address = address
        self.phone = phone
        self.email = email

    def show_customer(self):
        print(f"Name: {self.name}\nSurname: {self.surname}\nAddress: {self.address} \nPhone: {self.phone} \nEmail: {self.email}")

customer = Customer("Adam", "Smith", "Przygodzka 43, Jaworzno", "502780580", "adam.smith2006@gmail.com")
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