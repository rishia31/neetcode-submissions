class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        char_list_s = sorted(list(s))
        char_list_t = sorted(list(t))
        if len(list(s)) == len(list(t)):
            for i in range(0, len(char_list_s)):
                if char_list_s[i] != char_list_t[i]:
                    return False
                else:
                    continue
            return True
        return False
