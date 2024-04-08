import sys

def isPalindrome(s: str) -> bool:
    strs = []
    for char in s:
        if char.isalnum():
            strs.append(char.lower())

    while len(strs) > 1:
        if strs.pop(0) != strs.pop():
            return False
            
    return True

# 표준 입력에서 문자열을 읽음
s = sys.stdin.readline().strip()

print(isPalindrome(s))
