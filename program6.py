arra = []
n = 10

for i in range(n):
    element = input(f"Enter the element {i + 1}: ")
    arra.append(element)

reversed_array = []

for i in range(len(arra) - 1, -1, -1):
    reversed_array.append(arra[i])

print("Original array:", arra)
print("Reversed array:", reversed_array)