class Solution:
    def isValid(self, s: str) -> bool:
        curr = []
        for x in range(len(s)):
            if (s[x] == "{"  or s[x] == "[" or s[x] == "("):
                curr.append(s[x])
            elif s[x] == "}":
                if curr and curr[-1] == "{":
                    curr.pop()
                else:
                    return False
            elif s[x] == "]":
                if curr and curr[-1] == "[":
                    curr.pop()
                else:
                    return False
            elif s[x] == ")": 
                if curr and curr[-1] == "(":
                    curr.pop()
                else:
                    return False
        if len(curr) > 0:
            return False
        else: 
            return True
