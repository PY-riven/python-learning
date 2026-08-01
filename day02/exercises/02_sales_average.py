sales = [120, 85, 260, 175, 90]
print(len(sales))
length = len(sales)
sum = 0
for sale in sales:
    sum += sale
print(sum)
res = sum / length
print('%.2f'% res)
