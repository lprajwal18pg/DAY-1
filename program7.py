arra1 = []
arra2 = []
n = 10

print("Enter elements for Array 1:")
for i in range(n):
    element = input(f"Enter element {i + 1}: ")
    arra1.append(element)

print("Enter elements for Array 2:")
for i in range(n):
    element = input(f"Enter element {i + 1}: ")
    arra2.append(element)

arra3 = arra1 + arra2

print("Combined Array 3:")
print(arra3)