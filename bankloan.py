salary=int(input("enter your salary"))
age=int(input("enter your age"))
credit_score=int(input("enter your credit score"))
if salary >=5000 and age>=21 and credit_score>=200:
    print("loan approved")
else:
    print("rejected,due to your salary or age or credit score are in sufficeint")    