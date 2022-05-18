# 문제 설명
"""
자연수 N이 주어지면, 
N의 각 자릿수의 합을 구해서 return 하는 solution 함수를 만들어 주세요.
예를들어 N = 123이면 1 + 2 + 3 = 6을 return 하면 됩니다.
"""


# 내 풀이)
def solution(n):
    answer = 0
    while n > 0:
        answer += n % 10
        n = n // 10
    return answer


print(solution(123))


# 다른 사람 풀이)
def solution1(n):
    return sum([int(i) for i in str(n)])
# 처음에 문자열인줄 알고 int()기능을 쓰고 싶었는데.. 정말 문자열로 바꾼 후 구현하면 되는 거 였다..


# map 이용
def solution2(n):
    return sum(map(int, str(n)))


# 재귀함수 이용
def solution3(n):
    if n < 10:
        return n
    return (n % 10) + solution3(n // 10)
