# 연속하는 정수의 합을 구하기 위해 값 정렬하기

a = int(input("a의 값을 입력하세요: "))
b = int(input("b의 값을 입력하세요: "))

# b가 더 큰 값!

if a > b:
    a, b = b, a

result = 0
for i in range(a, b+1):
    result += i

print("a부터 b까지 정수의 합은 {}입니다".format(result))

print(f'{a}부터 {b}까지 정수의 합은 {result}입니다.')
