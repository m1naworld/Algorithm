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


######################################


# 문제 3.

"""
정수 배열 numbers가 매개변수로 주어집니다. 
numbers의 각 원소에 두배한 원소를 가진 배열을 return하도록 solution 함수를 완성해주세요.
"""


def solution1(numbers):
    for i, num in enumerate(numbers):
        numbers[i] = num*2

    return numbers


solution1([1, 2, 3, 4, 5])

# 리스트 내포(List comprehension)
# 리스트 안에 for문을 포함하는 리스트 내포를 사용하면 좀 더 편리하고 직관적인 프로그램을 만들 수 있음
# 리스트 내포 일반 문법: [표현식 for 항목 in 반복가능객체 if 조건문]

# 위의 코드를 리스트 내포를 활용해 변경해 보기.


def solution2(numbers):
    return [num*2 for num in numbers]

# solution1() 실행 결과, 가장 오래 걸린 시간: 0.13ms
# solution2() 실행 결과, 가장 오래 걸린 시간: 0.8ms
# 리스트 내포를 활용한 함수가 더욱 빠른걸 확인 할 수 있었다!
