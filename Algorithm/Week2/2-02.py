# 배열 원소의 최댓값을 구하는 프로그램

from typing import Any, Sequence


def max_of(list: Sequence) -> Any:
    # 원소값 정리

    maximum = list[0]

    for i in range(1, len(list)):
        if list[i] > maximum:
            maximum = list[i]
    return maximum


if __name__ == '__main__':

    num = 0
    print("원소 수를 입력하세요: ".format(num))
    list = [None] * num

    for i in range(num):
        list[i] = int(input("x[{}]값을 입력하세요: ".format(i)))

    print("최댓값은 {}입니다.".format(max_of(list)))
