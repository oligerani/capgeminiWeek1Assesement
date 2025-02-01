l=list(map(int,input("enter the list of items").split()))
el=[]
ol=[]
for i in l:
    if i%2==0:
        el.append(i*2)
    else:
        ol.append(i)    
print("odd literals",ol) 
print("even literals",el)  
m=ol+el
m.sort
print(m)     