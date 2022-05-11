# 문제 설명
'''
0부터 9까지의 숫자 중 
일부가 들어있는 정수 배열 numbers가 매개변수로 주어집니다. 
numbers에서 찾을 수 없는 0부터 9까지의 숫자를 모두 찾아 더한 수를 
return 하도록 solution 함수를 완성해주세요.
'''

# 내 문제 풀이)


def solution(numbers):
    x = 0

    a_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    for i in numbers:
        for j in a_list:
            if i == j:
                a_list.remove(j)

    print(a_list)

    for i in a_list:
        x += i

    return x


print(solution([1, 2, 3, 4, 6, 7, 8, 0]))


# 다른 사람 풀이)
def solution1(numbers):
    return 45 - sum(numbers)


def solution2(numbers):
    answer = 0

    for i in range(1, 10):
        if i not in numbers:
            answer += i
    return answer
