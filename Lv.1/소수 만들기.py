# 문제 설명
"""
주어진 숫자 중 3개의 수를 더했을 때 소수가 되는 경우의 개수를 구하려고 합니다. 
숫자들이 들어있는 배열 nums가 매개변수로 주어질 때, 
nums에 있는 숫자들 중 서로 다른 3개를 골라 더했을 때 
소수가 되는 경우의 개수를 return 하도록 solution 함수를 완성해주세요.
"""

# 내 풀이
import itertools


def solution(nums):
    answer = []
    # 3개씩 선정
    result = list(itertools.combinations(nums, 3))
    print(result)
    for i in result:
        x = sum(i)
        if x == 7:
            if x not in answer:
                answer.append(x)
        elif x % 2 != 0 and x % 3 != 0 and x % 5 != 0 and x % 7 != 0:
            if x not in answer:
                answer.append(x)
    print(answer)
    return len(answer)


print(solution([1, 2, 3, 4]))
print(solution([1, 2, 3, 4, 9, 8, 7, 6, 5, 15, 76, 77]))
