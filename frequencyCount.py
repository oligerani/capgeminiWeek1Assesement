products="yogurt eggs cookies cookies eggs yogurt apple yogurt apple"
dict_to_store={}
List=products.split()
for i in List:
    if i in dict_to_store:
        dict_to_store[i]+=1
    else:
        dict_to_store[i]=1
print(dict_to_store)            
       
    