msg = "성적 출력 프로그램입니다."
print(msg)
name = input("성명 입력 >> ")
kor = int(input("국어 성적 >> "))
eng = int(input("영어 성적 >> "))
mat = int(input("수학 성적 >> "))

sum = kor + eng + mat
avg = sum/3

msg = f'성명 : {name}\n'
msg += f'국어 : {kor}\n'
msg += f'영어 : {eng}\n'
msg += f'수학 : {mat}\n'
msg += f'총점 : {sum}\n'
msg += f'평균 : {avg}\n'
print(msg)