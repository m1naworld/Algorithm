# 문제 설명
"""
배열 arr가 주어집니다. 
배열 arr의 각 원소는 숫자 0부터 9까지로 이루어져 있습니다. 
이때, 배열 arr에서 연속적으로 나타나는 숫자는 하나만 남기고 전부 제거하려고 합니다. 
단, 제거된 후 남은 수들을 반환할 때는 배열 arr의 원소들의 순서를 유지해야 합니다. 
예를 들면,
arr = [1, 1, 3, 3, 0, 1, 1] 이면 [1, 3, 0, 1] 을 return 합니다.
arr = [4, 4, 4, 3, 3] 이면 [4, 3] 을 return 합니다.
배열 arr에서 연속적으로 나타나는 숫자는 제거하고 남은 수들을 return 하는 solution 함수를 완성해 주세요.
"""

# 내 풀이)
# 재귀함수 -> 효율성 테스트에서 모두 실패
# def solution(arr):
# for i in range(len(arr)):
#     if i < len(arr)-1 and arr[i] == arr[i+1]:
#         del arr[i]
#         solution(arr)

# return arr

# while문 -> 효율성 테스트에서 모두 실패
# def solution(arr):
#     i = 0
#     while(i < len(arr) - 1):
#         if 0 <= i and arr[i] == arr[i+1]:
#             del arr[i]
#             i -= 1
#         else:
#             i += 1
#     return arr

# 질문을 통해) 기존 배열의 원소를 빼는 것보다, 새 배열에 추가하는 방식이 더 빠르다는 것을 알게됨.
# 삭제 -> 추가로 코드를 바꿔봤지만, 효율성 테스트 4개중 3개만 성공
# def solution(arr):
#     i = 0
#     answer = []
#     while i < len(arr) - 1:
#         if arr[i-1] != arr[i] != arr[i+1]:
#             answer.append(arr[i])
#             i += 1
#         elif arr[i] == arr[i+1]:
#             if len(answer) > 0 and answer[-1] == arr[i]:
#                 i += 1
#             else:
#                 answer.append(arr[i])
#                 i += 1
#         else:
#             i += 1

#     return answer


# print(solution([1, 1, 3, 3, 0, 1, 1]))
# print(solution([4, 4, 4, 3, 3]))
