def create_dictionary_products(products):
    product_dict = {}

    for item in products:
        prodname, category, price, stock = item.split(":")
        product_dict[prodname] = {
            "category": category,
            "price": int(price),
            "stock": int(stock)
        }


    # print(product_dict)
    print('Category-wise Most Expensive Products:') 
    products1 = product_dict

    res_elec = ''
    res_fash = ''
    for prod in products1:
        if products1[prod]['stock'] == 0 and products1[prod]['category'] == 'Electronics':
            res_elec += prod

        if products1[prod]['stock'] == 0 and products1[prod]['category'] == 'Fashion':
            res_fash += prod



    total_Elec = 0
    total_fashion = 0
    for prod in products1:
        if products1[prod]['category'] == 'Electronics':
            total_Elec += products1[prod]['price']
        
        if products1[prod]['category'] == 'Fashion':
            total_fashion += products1[prod]['price']



    max_prod = max(products1, key=lambda k : products1[k]['price'])
    min_prod = min(products1, key=lambda k : products1[k]['price'])
    print(f"{products1[max_prod]['category']}: {max_prod}: {products1[max_prod]['price']}")
    print(f"{products1[min_prod]['category']}: {min_prod}: {products1[min_prod]['price']}")
    print("                      ")
    print("Out of Stock Products")
    print(f"{res_elec} ({products1[prod]['category']})")
    print(f"{res_fash} ({products1[prod]['category']})")
    print("                      ")
    print('Category-wise total inventary Value:')
    print(f'Electronics: {total_Elec}')
    print(f'Fashion: {total_fashion}')


        

products = [ 
"iPhone14:Electronics:89999:15", 
"Samsung_TV:Electronics:45000:0", 
"Nike_Shoes:Fashion:8999:25", 
"Adidas_Shirt:Fashion:2999:10", 
"MacBook:Electronics:129999:5", 
"Levi_Jeans:Fashion:4999:0", 
"iPad:Electronics:35999:12" 
]
create_dictionary_products(products)

