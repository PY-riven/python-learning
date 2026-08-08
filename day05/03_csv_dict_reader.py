import csv
csv_products = []
with open('data/products.csv',mode='r',encoding='utf-8') as f:
    csv_reader = csv.DictReader(f)
    for row in csv_reader:
        products = {
            'product_id':row['product_id'],
            'name':row['name'],
            'category':row['category'],
            'price':int(row['price']),
            'quantity':int(row['quantity'])
        }
        csv_products.append(products)
print(csv_products)
for rows in csv_products:
    xl = rows['price']*rows['quantity']
    print(f'商品：{rows['name']},销售额：{xl:.2f}元')

