
arra = []
n = 5


for i in range(n):
    element = input(f"Enter the element {i + 1}: ")
    element = int(element)  
    arra.append(element)


max_ele = max(arra)
max_index = arra.index(max_ele)

eleafmax = len(arra) - (max_index + 1)


print(f"The max ele is: {max_ele}")
if eleafmax == 1:
    print("1 debit")
    max_ele -= 100
elif eleafmax == 2:
    print("2 debit")
    max_ele -= 100
elif eleafmax == 3:
    print("3 debit")
    max_ele -= 100
elif eleafmax > 3:
    print("More than 3 debits")
    max_ele -= 500


print(f"after diduction: {max_ele}")