import math

print("원의 둘레와 넓이를 구하는 프로그램")
r = int(input("원의 반지름 입력>> "))
round = math.pi * 2 * r
size = math.pi * r **2


print(f'반지름이 {r}인 원 둘레의 길이는 {round:.3f}이고 넓이는 {size:.4f}입니다.')