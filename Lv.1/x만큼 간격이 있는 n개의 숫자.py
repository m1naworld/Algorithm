# 문제 설명)

"""
함수 solution은 정수 x와 자연수 n을 입력 받아, 
x부터 시작해 x씩 증가하는 숫자를 n개 지니는 리스트를 리턴해야 합니다. 
다음 제한 조건을 보고, 조건을 만족하는 함수, solution을 완성해주세요.
"""


# 내 풀이)
def solution(x, n):
    answer = []
    k = 0
    for i in range(n):
        k += x
        answer.append(k)
    return answer


print(solution(2, 5))
print(solution(4, 3))
print(solution(-4, 2))


# 다른 사람 풀이)
def solution1(x, n):
    return [i * x + x for i in range(n)]
