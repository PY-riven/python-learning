with open('data/sales_report.txt','a',encoding = 'utf-8') as f:
    for _ in range(2):
        content = input()
        f.write(content+'\n')



