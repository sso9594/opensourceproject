# 배열 원소를 역순으로 정렬하기
# 역순으로 정렬하는 알고리즘 함수
from typing import MutableSequence, Any

# 파이썬에서는 튜플로 교환하는 형식 쓰자!
# C의 temp 교환 형식 ㅠㅠ 버리자!


def revese(a: MutableSequence) -> None:
    for i in range(len(a)//2):
        a[i], a[(len(a) - 1) - i] = a[(len(a) - 1) - i], a[i]


a = [2, 5, 1, 3, 9, 6, 7]


print(a)


print(a)
