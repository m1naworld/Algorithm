# 문제 설명
"""
두 정수 left와 right가 매개변수로 주어집니다. 
left부터 right까지의 모든 수들 중에서, 
약수의 개수가 짝수인 수는 더하고, 
약수의 개수가 홀수인 수는 뺀 수를 return 하도록 solution 함수를 완성해주세요.
"""


# 내 풀이)
import math


def solution(left, right):
    answer = 0
    for i in range(left, right + 1):
        if math.sqrt(i) - int(math.sqrt(i)) == 0.0:
            answer -= i
        else:
            answer += i

    return answer


print(solution(24, 27))


# 다른 사람 풀이)
def solution1(left, right):
    answer = 0
    for i in range(left, right+1):
        if int(i**0.5) == i**0.5:
            answer -= i
        else:
            answer += i
    return answer

# i**0.5 : i의 제곱근을 구하는 식
