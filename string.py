name = "Nithin"
message = "Hello Python"

# Access characters
print(name[0])       # N
print(name[-1])      # n

# Slicing
print(name[0:3])     # Nit

# Common methods
print(name.lower())
print(name.upper())
print(name.strip())
print(name.replace("N", "n"))
print(name.split())

# f-string
age = 22
print(f"My name is {name} and I am {age} years old")