product = {
    "name": "键盘",
    "price": 199,
    "sales": 12,
    "category": "电脑配件"
}
for key in product:
    print(key)
print('-------------')
product['sales']=15
product['stock']=20
print(product)
print(product.get('brand','暂时不知道品牌'))
print('category' in product)
for key,value in product.items():
    print(key,value)
