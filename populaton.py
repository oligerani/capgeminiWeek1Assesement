def product_des():
     cities = [
    {"name": "New York", "population": 8419600},
    {"name": "Los Angeles", "population": 3980400},
    {"name": "Chicago", "population": 2716000},
    {"name": "Houston", "population": 2328000}
    ]
     population=sorted(cities,key=lambda x:(-x["population"],x["name"]))
     print(population)
     
product_des()
    