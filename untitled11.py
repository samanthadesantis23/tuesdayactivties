class DecreasingCounter:
    def __init__(self, initial_value: int):
        self.initial_value = initial_value  # Save the original value
        self.value = initial_value  # Set the current value to the initial value

    def print_value(self):
        print("value:", self.value)

    def decrease(self):
        # Decrease the value only if it is greater than 0
        if self.value > 0:
            self.value -= 1

    def set_to_zero(self):
        # Set the counter's value to 0
        self.value = 0

    def reset_original_value(self):
        # Reset the counter to the original value
        self.value = self.initial_value

counter = DecreasingCounter(10)
counter.print_value()  # Expected: value: 10
counter.decrease()
counter.print_value()  # Expected: value: 9
counter.decrease()
counter.print_value()  # Expected: value: 8

counter = DecreasingCounter(2)
counter.print_value()  # Expected: value: 2
counter.decrease()
counter.print_value()  # Expected: value: 1
counter.decrease()
counter.print_value()  # Expected: value: 0
counter.decrease()
counter.print_value()  # Expected: value: 0 (no further decrease)


counter = DecreasingCounter(100)
counter.print_value()  # Expected: value: 100
counter.set_to_zero()
counter.print_value()  # Expected: value: 0

counter = DecreasingCounter(55)
counter.decrease()
counter.decrease()
counter.decrease()
counter.decrease()
counter.print_value()  # Expected: value: 51 (55 - 4)
counter.reset_original_value()
counter.print_value()  # Expected: value: 55 (reset to original)
