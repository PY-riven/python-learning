import csv
data = [
    ['Alice', '30', '纽约'],
    ['Bob', '25', 'Los Angeles']
]
with open('data/new_products.csv',mode='w',newline='',encoding='utf-8') as f:
    csv_writer = csv.writer(f)
    header = ['Name', 'Age', 'City']
    csv_writer.writerow(header)
    for row in data:
        csv_writer.writerow(row)
