from change import card_conv

if __name__ == '__main__':

    print("10진수를 n진수로 변환합니다.")

    while True:
        number = int(input("변환할 값으로 음이 아닌 정수를 입력하세요: "))
        if number > 0:
            break
    while True:
        deci = int(input("어떤 진수로 변환할까요?: "))
        if 2 <= deci <= 36:
            break

    while True:
        print(f'2진수로는 {card_conv(number, deci)}입니다.')
        choice = input("한 번 더 변환할까요? (Y ... 예 / N ... 아니요) ")
        if choice == 'N' or 'n':
            break
