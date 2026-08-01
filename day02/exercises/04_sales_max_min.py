sales = [120, 85, 260, 175, 90]
max_sale = sales[0]
min_sale = sales[0]
for sale in sales[1:]:
    if sale > max_sale:
        max_sale = sale
    min_sale = sale
print(max_sale,min_sale)

