# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        smallest = 0
        largest = n 
        mid = (smallest+largest)//2
        x = guess(mid)
        while not x == 0:
            mid = (smallest+largest)//2
            x = guess(mid)
            if x == -1:
                largest = mid - 1
            elif x == 1:
                smallest = mid + 1

        return mid
        