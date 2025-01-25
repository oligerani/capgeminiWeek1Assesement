name=input("enter name of the student")
total=0
m1=int(input("enter m1 marks"))
m2=int(input("enter m2 marks"))
pys=int(input("enter pys marks"))
che=int(input("enter che marks"))
wt=int(input("enter wt marks"))
total=m1+m2+pys+che+wt
print(total)
percentage=(total/150)*100
print(percentage)
if percentage >= 85:
    print("A grade")
elif percentage >=70 and percentage <80:
    print("B grade")
    
elif percentage >=60 and percentage <70:
    print("C grade")    
else:
    print("fail")        


    

