value_lsit =["no","name","phone","email"]
dic = {}
for i in value_lsit:
    dic[i] = input(f'{i} 입력>> ')

print(dic.keys())
print(dic.values())