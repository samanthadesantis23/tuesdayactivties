def row_sums(my_matrix: list):
    for row in my_matrix:
        row_sum = sum(row)  # Calculate the sum of the current row
        row.append(row_sum)  # Append the sum to the end of the row
        
# Example matrix (3x3 matrix)
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Call row_sums function
row_sums(matrix)

# Print the modified matrix
for row in matrix:
    print(row)