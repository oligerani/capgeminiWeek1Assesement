products = [
    {"name": "Laptop", "price": 1200},
    {"name": "Headphones", "price": 80},
    {"name": "Smartphone", "price": 700},
    {"name": "Monitor", "price": 150}
   ]
l=[]
m=[]
for i in products:
    l.append((80/100)*i['price'])
    
print(l)
for i in l:
    if i>100:
        m.append(i)
print(m)        