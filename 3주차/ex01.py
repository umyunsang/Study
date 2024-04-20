import random

alist = [10,20,30,40,50,60,70,80,90,100]
random_list =[0,0,0]
hap = 0
for i in range(3):
    random_list[i] = random.choice(alist)
    hap += random_list[i]
print(random_list)
print(hap)
