# 리스트를 활용하여 건너뛰는 값을 제외한 범위 생성

for i in list(range(1, 8)) + list(range(9, 13)):
    print(i, end=" ")
