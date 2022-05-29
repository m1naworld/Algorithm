# 문제 설명
"""
함수 solution은 정수 n을 매개변수로 입력받습니다. 
n의 각 자릿수를 큰것부터 작은 순으로 정렬한 새로운 정수를 리턴해주세요. 
예를들어 n이 118372면 873211을 리턴하면 됩니다.
"""


# 내풀이)
def solution(n):
    answer = []
    for i in str(n):
        answer.append(int(i))
    new_answer = sorted(answer, reverse=True)
    result = ''.join(str(s) for s in new_answer)
    return int(result)


print(solution(118372))


# 다른사람 풀이)
def solution1(n):
    ls = list(str(int(n)))
    ls.sort(reverse=True)
    return int("".join(ls))


def solution1(n):
    return int("".join(list(sorted(str(n)), reverse=True)))

# sorted하면 리스트로 반환해서 나오기 때문에 list로 감싸줄 필요 없음.
