class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        sam = { "}" : "{", "]" : "[" , ")" : "("}
        for i in s:
            if i in sam:
                if stack and stack[-1] == sam[i] :
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)
        return True if len(stack) == 0 else False