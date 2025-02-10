arra = []
n = 10

for i in range(n):
    element = input(f"Enter the element {i + 1}: ")
    element = int(element)  
    arra.append(element)

if len(arra) > 0:
    max_element = arra[0]
    count = 1  

    for element in arra[1:]:  
        if element > max_element:
            max_element = element
            count = 1  
        elif element == max_element:
            count += 1 

    print("The maximum element is:", max_element)
    print("The maximum element is repeated:", count, "times")
else:
    print("The list is empty. No maximum element to find.")