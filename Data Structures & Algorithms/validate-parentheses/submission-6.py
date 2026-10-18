class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        sHashMap ={")": "(", "}": "{", "]": "["}
        for char in s:
            if char in sHashMap:
                if stack and (stack[-1] == sHashMap[char]):
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)
        return not stack


