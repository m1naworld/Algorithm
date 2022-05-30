# 문제 설명
"""
길이가 n이고, "수박수박수박수...."와 같은 패턴을 유지하는 문자열을 리턴하는 함수, solution을 완성하세요. 
예를들어 n이 4이면 "수박수박"을 리턴하고 3이라면 "수박수"를 리턴하면 됩니다.
"""


# 내풀이
def solution(n):
    str = "수박"
    if n == 0:
        return ""
    if n == 1:
        return str[0]
    if n % 2 == 0:
        return str * int(n/2)
    else:
        return str * int(n/2) + str[0]

# // 버림나눗셈로 바꾸면 더 좋을 것 같음 !


print(solution(3))
print(solution(4))


# 다른 사람 풀이
def solution1(n):
    return (n*"수박")[:n]

# 내가 처음에 생각했던 풀이 -> 불필요한 메모리와 CPU연산을 사용하게 됨
