# 기수 변환하기 (n진수 구하기)

def card_conv(x: int, r: int) -> str:

    # 반환값
    d = ''
    dchar = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    while x > 0:
        # 나머지 부분
        d += dchar[x % r]
        # 몫 부분
        x //= r

    return d[::-1]
