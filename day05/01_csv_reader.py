import csv
with open('data/products.csv',mode='r',encoding='utf-8') as f:
    reader_products = csv.reader(f)
    header = next(reader_products)
    count = 0
    for row in reader_products:
        print(row)
        count += 1
    print(header)
    print(count)


