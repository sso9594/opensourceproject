# 1~12까지 출력할 때 8을 건너뛰게 하는 프로그램
# 조건문과 continue문 활용

for i in range(1, 13):
    if i == 8:
        continue
    print("{}".format(i), end=" ")
