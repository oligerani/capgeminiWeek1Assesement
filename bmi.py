w=int(input("enter your weigth"))
h=float(input("enter your heigth"))
bmi=w/(h*h)
print(bmi)
if 25<=bmi< 30:
    print("overweigth")
elif 18.5<=bmi <25:
    print("normal")   
elif 16<=bmi < 18.5:
    print("underweigt") 
else:
    print("severely underweigt")        