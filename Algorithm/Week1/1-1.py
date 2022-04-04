a, b, c, maximum = 0, 0, 0, 0

a = int(input("a의 값을 입력하세요: "))
b = int(input("b의 값을 입력하세요: "))
c = int(input("c의 값을 입력하세요: "))

maximum = a
if maximum < b:
    maximum = b
if maximum < c:
    maximum = c

print("가장 큰 값은 {}이다.".format(maximum))
