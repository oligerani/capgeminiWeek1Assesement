def factorial_no(n):
    if n==0 or n==1:
       return 1
    return n*factorial_no(n-1)
n=int(input("enter a no"))
res=factorial_no(n)
print(res)

     
