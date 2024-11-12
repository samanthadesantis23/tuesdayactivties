# Class Checklist
class Checklist:
    def __init__(self, header, entries):
        self.header = header  # String: header of the checklist
        self.entries = entries  # List: list of entries in the checklist

# Class Customer
class Customer:
    def __init__(self, id, balance, discount):
        self.id = id  # String: customer id
        self.balance = balance  # Float: customer's balance
        self.discount = discount  # Integer: discount percentage for the customer

# Class Cable
class Cable:
    def __init__(self, model, length, max_speed, bidirectional):
        self.model = model  # String: model of the cable
        self.length = length  # Float: length of the cable in meters
        self.max_speed = max_speed  # Integer: maximum speed of the cable in Mbps
        self.bidirectional = bidirectional  # Boolean: whether the cable is bidirectional


# Creating instances of the classes

# Checklist
checklist = Checklist("Weekend Chores", ["Buy groceries", "Clean the house", "Finish the project"])

# Customer
customer = Customer("C12345", 1500.75, 10)

# Cable
cable = Cable("Xtreme Pro", 30.5, 1000, True)

# Printing the details

print(f"Checklist: {checklist.header}")
print(f"Entries: {checklist.entries}")

print(f"Customer ID: {customer.id}")
print(f"Balance: ${customer.balance}")
print(f"Discount: {customer.discount}%")

print(f"Cable Model: {cable.model}")
print(f"Cable Length: {cable.length} meters")
print(f"Max Speed: {cable.max_speed} Mbps")
print(f"Bidirectional: {cable.bidirectional}")
