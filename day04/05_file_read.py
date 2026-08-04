with open('data/sales.txt','r',encoding = 'utf-8') as f:
    content = f.readlines()
    for line in content:
        print(line.strip())
        line = line.strip()
        line = line.split(',')
        print(line)
