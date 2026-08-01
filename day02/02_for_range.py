for i in range(1,11):
    print(i,end=' ')
print()
for x in range(10,0,-1):
    print(x,end=' ')
print()
sum=0
arr=[]
arr1=[]
for k in range(1,101):
    if k%2==0:
        arr.append(k)
    else:
        arr1.append(k)
    sum+=k

print('偶数为：',arr)
print('奇数为：',arr1)
print(sum)

