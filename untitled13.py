class NumberStats:
    def __init__(self):
        self.count = 0  # To count how many numbers have been added
        self.total_sum = 0  # To store the sum of all numbers

    def add_number(self, number: int):
        self.count += 1
        self.total_sum += number

    def count_numbers(self):
        return self.count

    def get_sum(self):
        return self.total_sum

    def average(self):
        if self.count == 0:
            return 0
        return self.total_sum / self.count


# Main program
stats = NumberStats()  # To track all numbers
even_stats = NumberStats()  # To track even numbers
odd_stats = NumberStats()  # To track odd numbers

print("Please type in integer numbers:")

while True:
    number = int(input())  # Get user input
    if number == -1:
        break  # Exit when user types -1
    stats.add_number(number)  # Add to total stats
    if number % 2 == 0:
        even_stats.add_number(number)  # Add to even stats
    else:
        odd_stats.add_number(number)  # Add to odd stats

# Print the results
print("Sum of numbers:", stats.get_sum())
print("Mean of numbers:", stats.average())

print("Sum of even numbers:", even_stats.get_sum())
print("Sum of odd numbers:", odd_stats.get_sum())
