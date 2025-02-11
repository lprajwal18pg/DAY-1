def rotate(num, k):
   
    k = k % len(num)
    num[:] = num[-k:] + num[:-k]


num = [1, 2, 3, 4, 5, 6, 7]
k = 3
rotate(num, k)
print(num)  