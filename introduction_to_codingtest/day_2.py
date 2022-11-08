# 문제 2.

"""
첫 번째 분수의 분자와 분모를 뜻하는 denum1, num1, 
두 번째 분수의 분자와 분모를 뜻하는 denum2, num2가 매개변수로 주어집니다. 
두 분수를 더한 값을 기약 분수로 나타냈을 때 분자와 분모를 순서대로 담은 배열을 return 하도록 solution 함수를 완성해보세요.
"""


def solution(denum1, num1, denum2, num2):
    denum3 = (denum1*num2 + denum2*num1)
    num3 = num1*num2

    low_num = num3 if denum3 > num3 else denum3

    # for i in reversed(range(low_num)): 리스트 원소를 거꾸로 뒤집고 이를 반환
    for i in range(low_num, 1, -1):
        if (num3 % i == 0 and denum3 % i == 0):
            denum3 = denum3 // i
            num3 = num3 // i

    return [denum3, num3]


print(solution(1, 2, 3, 4))
print(solution(9, 2, 1, 3))
print(solution(3, 20, 4, 7))

# 최대 공약수 math 라이브러리 gcd 함수
# import math
# math.gcd(a, b)


# 느낀점
# 나는 최대 공약수를 라이브러리 함수를 사용하지 않고 풀어보고 싶었다.
# 정말 생각의 전환!!의 중요성!
# 같은 코드에 for문 도는 순서만 반대로 바꿨다.
# 큰 수부터 돌 경우 약수를 공통으로 가지고 있는 처음의 경우가 바로 최대공약수! 작은 수 부터 돌 경우 최대 공약수를 찾지 못하는 문제를 해결하게 되었다!
