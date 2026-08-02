customers = [
    "张三",
    "李四",
    "张三",
    "王五",
    "李四",
    "赵六"
]
orlength = len(customers)
print('原始记录数据',orlength)
setarr = set(customers)
length = len(setarr)
print(length)
print(setarr)
print('张三' in setarr)
setarr.add('沅七')
print(setarr)
setarr.pop()
print(setarr)

