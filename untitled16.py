class LunchCard:
    def __init__(self, balance: float):
        # Initialize the balance when creating the card
        self.balance = balance

    def __str__(self):
        # Return the balance as a formatted string with one decimal place
        return f"The balance is {self.balance:.1f} euros"

    def eat_lunch(self):
        # Subtract the cost of a regular lunch (2.60 euros) if balance allows
        if self.balance >= 2.60:
            self.balance -= 2.60
        else:
            self.balance = self.balance  # Balance does not change if not enough money

    def eat_special(self):
        # Subtract the cost of a special lunch (4.60 euros) if balance allows
        if self.balance >= 4.60:
            self.balance -= 4.60
        else:
            self.balance = self.balance  # Balance does not change if not enough money

    def deposit_money(self, amount: float):
        # Increase the balance by the given amount, raise exception for negative deposit
        if amount < 0:
            raise ValueError("You cannot deposit an amount of money less than zero")
        self.balance += amount


# Main function to test the LunchCard class as described
def main():
    # Create lunch cards for Peter and Grace
    peters_card = LunchCard(20)
    graces_card = LunchCard(30)
    
    # Peter eats a special
    peters_card.eat_special()
    
    # Grace eats a regular lunch
    graces_card.eat_lunch()
    
    # Print the balance on each card
    print(f"Peter: {peters_card}")
    print(f"Grace: {graces_card}")
    
    # Peter deposits 20 euros
    peters_card.deposit_money(20)
    
    # Grace eats the special
    graces_card.eat_special()
    
    # Print the balance on each card again
    print(f"Peter: {peters_card}")
    print(f"Grace: {graces_card}")
    
    # Peter eats a regular lunch twice
    peters_card.eat_lunch()
    peters_card.eat_lunch()
    
    # Grace deposits 50 euros
    graces_card.deposit_money(50)
    
    # Print the balance on each card for the final time
    print(f"Peter: {peters_card}")
    print(f"Grace: {graces_card}")

# Running the main function to test everything
if __name__ == "__main__":
    main()
