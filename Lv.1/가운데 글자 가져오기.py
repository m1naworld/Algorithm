# 문제 설명
"""
단어 s의 가운데 글자를 반환하는 함수, 
solution을 만들어 보세요. 
단어의 길이가 짝수라면 가운데 두글자를 반환하면 됩니다.
"""


# 내 풀이)
def solution(s):
    x = len(s) % 2
    y = int(len(s) / 2)
    if x != 0:
        return s[y]
    else:
        return s[y-1:y+1]


print(solution("abcde"))
print(solution("qwer"))


# 다른 사람 풀이)
def solution1(s):
    return s[(len(s)-1)//2:len(s)//2+1]

# *(len(s)-1)//2
# ex) 짝수, 짝수 + 1의 몫이 같다는 걸 이용 !!
