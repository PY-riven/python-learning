sales = [120, 85, 260, 175, 90]
def calculate_total(sales):
    total = sum(sales)
    return total
def calculate_average(sales):
    total = calculate_total(sales)
    average = total / len(sales)
    return average

def count_target_sales(sales, target):
    count = 0
    for sale in sales:
        if sale >= target:
            count += 1
    return count
target = int(input())
total = calculate_total(sales)
average = calculate_average(sales)
count = count_target_sales(sales,target)
print('总销售额:',total,'平均销售额:',average,'大于等于目标销售的天数',count)
