class Solution:
    def isPalindrome(self, s: str) -> bool:
        updated_s = s.lower()
        updated_s = ''.join(filter(str.isalnum, updated_s))
        updated_s = str(updated_s)
        for i in range (0, len(updated_s) // 2,):
            if updated_s[i] == updated_s[-1-i]:
                continue
            else:
                return False
        return True
