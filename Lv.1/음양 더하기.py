# 문제 설명
"""
어떤 정수들이 있습니다. 
이 정수들의 절댓값을 차례대로 담은 정수 배열 absolutes와 
이 정수들의 부호를 차례대로 담은 불리언 배열 signs가 매개변수로 주어집니다. 
실제 정수들의 합을 구하여 return 하도록 solution 함수를 완성해주세요.
"""


# 내 풀이)
def solution(absolutes, signs):
    answer = 0
    for index, value in enumerate(signs):
        if value == False:
            x = absolutes[index]
            absolutes[index] = -x

    for i in absolutes:
        answer += i

    return answer


print(solution([4, 7, 12], [True, False, True]))


# 다른 사람 풀이)
def solution1(absolutes, signs):
    return sum(absolutes if sign else -absolutes for absolutes, sign in zip(absolutes, signs))

# sum함수..대박..!
# for문의 zip()..대박..!
