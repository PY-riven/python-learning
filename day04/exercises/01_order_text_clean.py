orders = [
    "  键盘,199,12  ",
    "鼠标,89,25",
    "  显示器,1299,5 ",
    "耳机,299,18  "
]
arr = []
for order in orders:
    dictorder = {'商品名称':0,'商品价格':0,'销售数量':0}
    order0 = order.strip()
    order1 = order0.split(',')
    dictorder['商品名称'] = order1[0]
    dictorder['商品价格'] = order1[1]
    dictorder['销售数量'] = order1[2]
    arr.append(dictorder)
print(arr)


