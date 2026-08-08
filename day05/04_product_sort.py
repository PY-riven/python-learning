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
csv_products1 = sorted(csv_products,key=lambda x:x['price'])
print(csv_products1)