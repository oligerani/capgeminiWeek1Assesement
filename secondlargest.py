a = list(map(int, input("Enter numbers  ").split()))

max1 = max2 = float('-inf')

for n in a:
    if n > max1:
        max2 = max1  
        max1 = n     
    elif n > max2 and n != max1:
        max2 = n  

if max2 == float('-inf'):
    print("There is no second largest number.")
else:
    print("Second largest number:", max2)
