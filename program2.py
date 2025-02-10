arra = []
n = 5

for i in range(n):
    element = input(f"Enter the element {i + 1}: ")
    element = int(element)  
    arra.append(element)

ele50 = []

for element in arra:
    if element > 50:
        ele50.append(element)
if ele50:
    print("Elements more tham 50:", ele50)
else:
    print("No elements more then 50 found.")
