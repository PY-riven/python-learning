order_text = "  键盘,199,12,电脑配件  "
order_text1 = order_text.strip()
order_text2 = order_text1.split(',')
print(order_text1)
print(order_text2)
for i in order_text2:
    print(i)
print('键盘' in order_text2)
order_text2[0] = '机械键盘'
print(order_text2)
count = 0
for j in order_text1:
    if j == ',':
        count += 1
print(count)
