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


def soultion(n, n_list, m, m_list):
    min_num = n if n <= m else m
    min_list = n_list if min_num == n else m_list

    for i in min_list:
        min_list.append(i)

    min_list.sort()
    return min_list


print(soultion(3, [1, 3, 5], 5, [2, 3, 6, 7, 9]))


def soultion1(n, n_list, m, m_list):

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


print(soultion1(3, [2, 3, 6, 7, 9], 5,  [1, 3, 5]))
