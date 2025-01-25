def prime_no(n):
    if n<2:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True
    
    
            
    
a=int(input("enter a starting no"))  
b=int(input("enter ending no"))
#n=int(input("enter a no to find the prime numbers"))  
for num in range(a, b+1):
    if prime_no(num):
        print(num,end=" ")
m=int(input("enter a no check if it is prime or not"))
if prime_no(m):
    print("yes")
else:
    print("no")            

        
    
