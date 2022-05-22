# 문제 설명
"""
함수 solution은 정수 n을 매개변수로 입력받습니다. 
n의 각 자릿수를 큰것부터 작은 순으로 정렬한 새로운 정수를 리턴해주세요. 
예를들어 n이 118372면 873211을 리턴하면 됩니다.
"""


# 풀이 생각 중)
def solution(n):
    answer = []
    for i in str(n):
        answer.append(int(i))
    return sorted(answer, reverse=True)


print(solution(118372))
