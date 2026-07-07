class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        trusts = {}
        trustedBy = {}
        #fill in dicts
        for i in range(1, n+1):
            trusts[i] = 0
            trustedBy[i] = 0

        for ai, bi in trust:
            trusts[ai] += 1
            trustedBy[bi] += 1
        
        #checks for if trusts = 0 and trusted = n-1
        for x in range(1, n+1):
            if trusts[x]==0 and trustedBy[x]==(n-1):
                return x
        #else
        return -1