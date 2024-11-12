def smallest_average(person1: dict, person2: dict, person3: dict):
    # Calculate the average for each contestant
    avg1 = (person1['result1'] + person1['result2'] + person1['result3']) / 3
    avg2 = (person2['result1'] + person2['result2'] + person2['result3']) / 3
    avg3 = (person3['result1'] + person3['result2'] + person3['result3']) / 3
    
    # Compare averages and return the dictionary with the smallest average
    if avg1 < avg2 and avg1 < avg3:
        return person1
    elif avg2 < avg1 and avg2 < avg3:
        return person2
    else:
        return person3
        
    # Example contestants
person1 = {"name": "Alice", "result1": 8, "result2": 7, "result3": 6}
person2 = {"name": "Bob", "result1": 6, "result2": 5, "result3": 4}
person3 = {"name": "Charlie", "result1": 9, "result2": 7, "result3": 8}

# Find the contestant with the smallest average
winner = smallest_average(person1, person2, person3)
print(winner)
