# 문제 설명
"""
주어진 숫자 중 3개의 수를 더했을 때 소수가 되는 경우의 개수를 구하려고 합니다. 
숫자들이 들어있는 배열 nums가 매개변수로 주어질 때, 
nums에 있는 숫자들 중 서로 다른 3개를 골라 더했을 때 
소수가 되는 경우의 개수를 return 하도록 solution 함수를 완성해주세요.
"""

import random


# 풀이 생각 중
def solution(nums):
    answer = 0
    num = sum(random.sample(nums, 3))
    print(num)
    if num & 2 != 0 | num & 3 != 0:
        answer += 1
    # 3개씩 선정
    # 소수 분별
    return answer


print(solution([1, 2, 3, 4]))
