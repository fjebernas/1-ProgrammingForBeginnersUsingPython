
class Customer:
    def __init__(self, name, beverage, food, total):
        self.name = name
        self.beverage = beverage
        self.food = food
        self.total = total
    
    greeting = "Welcome to the Coffee Place!"

c_1 = Customer("Samirah","Iced caffe latte", "Cinnamon roll", 225)
c_2 = Customer("Jerry", "Caramel macchiato", "Glazed doughnut", 230)

print(Customer.greeting)
print(c_1.beverage)
print(c_2.food)