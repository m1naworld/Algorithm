# 문제 4.
"""
오름차순으로 정렬이 된 두 배열이 주어지면 두 배열을 오름차순으로 합쳐 출력하는 프로그램을 작성하시오.

A, B 두 개의 집합이 주어지면 두 집합의 공통 원소를 추출하여 오름차순으로 출력하는 프로그램을 작성하시오.
첫 번째 줄에 첫 번째 배열의 크기 N(1<=N<=30,000)이 주어진다.
두 번째 줄에 N개의 배열 원소가 오름차순으로 주어진다.
세 번째 줄에 두 번째 배열의 크기 M(1<=M<=30,000)이 주어진다.
네 번째 줄에 M개의 배열 원소가 오름차순으로 주어진다.
각 리스트의 원소는 int형 변수의 크기를 넘지 않는다.

오름차순으로 정렬된 배열을 출력한다.

입력예제 1
3
1 3 5 
5
2 3 6 7 9

출력예제 1
1 2 3 3 5 6 7 9
"""


def solution(n, n_list, m, m_list):

    for i in n_list:
        print(i)
        m_list.append(i)

    m_list.sort()
    return m_list


print(solution(3, [1, 3, 5], 5, [2, 3, 6, 7, 9]))


def solution1(n, n_list, m, m_list):

    index = 0

    for n in n_list:
        if (max(m_list) > n):
            for j in range(index, len(m_list)):
                print(j)
                if (n <= m_list[j]):
                    index = j
                    m_list.insert(j, n)
                    print(m_list, index)
                    break
        else:
            m_list.append(n)
    return m_list


print(solution1(5, [2, 3, 6, 7, 9], 3,  [1, 3, 5]))


# 아래의 코드는 이중 for문을 사용했을 경우 시간복잡도가 n제곱이었다면,
# while문을 통해 시간 복잡도가 n으로 줄었다.
def solution2(n, arr1, m, arr2):
    answer = []

    p1 = 0
    p2 = 0

    while(p1 < n and p2 < m):
        print(p1, p2)
        if(arr1[p1] <= arr2[p2]):
            answer.append(arr1[p1])
            p1 += 1
        else:
            answer.append(arr2[p2])
            p2 += 1

    while(p1 < n):
        print("p1", p1)
        answer.append(arr1[p1])
        p1 += 1

    while(p2 < m):
        print("p2", p2)
        answer.append(arr2[p2])

    return answer


print(solution2(5, [2, 3, 6, 7, 9], 3,  [1, 3, 5]))
