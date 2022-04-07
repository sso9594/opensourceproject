# 알고리즘 개선하기
# 한 변을 기준으로 n의 제곱근 이하로 나눔
# 만약 나눴을 때 나누어 떨어지지 않는다면 소수라고 판단

# 1000 이하의 모든 소수를 나열하는 프로그램 (프로그램 개선 2)

counter = 0
ptr = 0
prime = [None] * 500

prime[ptr] = 2
ptr += 1

prime[ptr] = 3
ptr += 1

for n in range(5, 1001, 2):
    i = 1
    while prime[i] * prime[i] <= n:
        counter += 2
        if n % prime[i] == 0:
            break
        i += 1
    else:
        prime[ptr] = n
        ptr += 1
        counter += 1

print(f'곱셈과 나눗셈을 실행한 횟수: {counter}')
