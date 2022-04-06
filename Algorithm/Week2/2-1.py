num = 0

num = int(input("학생 수를 입력하세요: "))
list = list(range(num))
score = 0

# 의문점 input()에 end=""추가하면 loop 안 돌아감
# TypeError: input() takes no keyword argumnets

for i in range(num):
    list[i] = int(input("{}번째 학생의 성적을 입력하세요: ".format(i+1)))
    score += list[i]

print("점수 합계: {}\n점수 평균: {}".format(score, score/num))
