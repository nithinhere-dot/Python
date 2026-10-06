numbers = [10, 20, 30, 40]

# Access
print(numbers[0])
print(numbers[-1])

# Modify
numbers[0] = 100

# Add
numbers.append(50)

# Insert
numbers.insert(1, 15)

# Remove
numbers.remove(30)

# Last item
last = numbers.pop()

# Length
print(len(numbers))

# Slicing
print(numbers[1:3])