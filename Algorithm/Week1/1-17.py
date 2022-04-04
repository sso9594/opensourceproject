area = int(input("직사각형의 넓이를 입력하세요: "))

# 계산 알고리즘
for i in range(1, area + 1):

    # i가 가장 긴 변의 길이가 되기 때문이다.
    if i * i > area:
        break
    if area % i:
        continue
    print("{} X {}".format(i, area // i))
