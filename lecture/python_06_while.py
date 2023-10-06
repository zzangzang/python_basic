# while 반복문
# - 반복 횟수를 모르는 경우
# - 조건이 만족하는 동안 계속 반복
# - 조건이 True이면 무한 반복
# - 조건이 False이면 반복 종료
# - while 문에 조건 True => 무한 Loop문 (조심!)
#   -> 반드시 break문과 함께 사용할 것!

# while 기본 문법
# while 조건:
#      실행문

a = list(range(1, 6))   # [1, 2, 3, 4, 5]
print(a)

i = 0   # index
while i < len(a):
    print(a[i])
    i += 1  # 최종 결과로 i값은 5임 출력은 1, 2, 3, 4, 5

# 사용자가 입력하는 값 -> 1, 2, 3만 가능
