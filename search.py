

# second method

def search_func(products, product):
    if not products:    # shorter way to test if the list is empty
        return "failure"
    for x in products: 
        if x == product: 
            return "success"
    else:
        return "failure" 
my_list = ["banana", "avocado", "carrots", "peas"]
prduct = "avocado"
index = search_func(my_list, prduct)
print(index) 
