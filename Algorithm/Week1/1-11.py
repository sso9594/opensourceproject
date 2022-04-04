# 실습 1-10(a부터 b까지 정수의 합을 구하는 과정과 최종값을 출력)을 개선

# 실행 결과는 같으나 판단 횟수가 n번에서 0번으로 바뀌고 반복 횟수 1번 감소하는 것이 조건 // if 문을 없앤다.

print("a부터 b까지 정수의 합을 구합니다")
a = int(input("정수 a를 입력하세요: "))
b = int(input("정수 b를 입력하세요: "))

# 정수의 합 구하는 과정과 최종값 출력 알고리즘

if a > b:
    a, b = b, a

sum = 0

# 판단 횟수 0번 / 반복 횟수 1번 감소
for i in range(a, b):
    print("{} +".format(i), end=" ")
    sum += i

print("{} =".format(b), end=" ")
sum += b

print(sum)
