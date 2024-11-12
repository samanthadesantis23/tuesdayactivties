class Person:
    def __init__(self, name: str):
        self.name = name  # Store the full name

    def return_first_name(self):
        # Split the name by space and return the first part (first name)
        return self.name.split()[0]

    def return_last_name(self):
        # Split the name by space and return the second part (last name)
        return self.name.split()[1]

# Example usage
if __name__ == "__main__":
    peter = Person("Peter Pythons")
    print(peter.return_first_name())  # Expected output: Peter
    print(peter.return_last_name())   # Expected output: Pythons

    paula = Person("Paula Pythonnen")
    print(paula.return_first_name())  # Expected output: Paula
    print(paula.return_last_name())   # Expected output: Pythonnen
