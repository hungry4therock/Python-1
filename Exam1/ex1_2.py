"""
날짜 : 2021/04/08
이름 : 김철학
내용 : 1 ~ 10까지의 정수에서 2의배수와 3의 배수 정수의 합을 구하시오.
"""
sum = 0

for k in range(1, 11):

    if k % 2 == 0 or k % 3 == 0:
        sum += k

print('2와 3배수의 정수의 합 :', sum)
