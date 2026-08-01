sales = [120, 85, 260, 175, 90, 310, 205]
countlen = len(sales)
sumsales = sum(sales)
meansales = sumsales / countlen
meansales = round(meansales,2)
maxsales = max(sales)
minsales = min(sales)
count1 = 0
count2 = 0
for sale in sales:
    if sale > 150:
        count1 += 1
count2 = countlen-count1
print(countlen,sumsales,meansales,maxsales,minsales,count1,count2)

