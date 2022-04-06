import random
from max import max_of

number = int(input("난수의 개수를 입력하세요: "))
min_n = int(input("난수의 최솟값을 입력하세요: "))
max_n = int(input("난수의 최댓값을 입력하세요: "))

list = [0] * number

for i in range(number):
    list[i] = random.randrange(min_n, max_n)
    # 예제에서는 random.randint()를 사용함! 하지만 random.randrange()가 int를 매개변수로 받고 int형으로 리턴하기 때문에 굳이 randint() 안 써도 됨!

print(list)
print(f'이 가운데 최댓값은 {max_of(list)}입니다.')
