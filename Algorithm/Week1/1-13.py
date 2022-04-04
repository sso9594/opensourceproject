# 1-12 기능 개선
# 반복문에서 if문을 수행하지 않기
# 카운터용 변수를 0에서 1로 변경해도 유연하게 대응 OK

num = int(input("+와 -를 번갈아 출력합니다. \n몇 개를 출력할까요?: "))

for i in range(num//2):
    print("+-", end="")

if num % 2 != 0:
    print("+")
