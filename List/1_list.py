numbers = [10, 20, 30, 40]

#list can contain different types
data=["nithin",1,23,True]

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
print(numbers[:3]) # first 3
print(numbers[2:]) # from index 2
print(numbers[:]) # entire list
