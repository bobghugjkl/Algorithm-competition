# Forward declaration of compare API.
# def compare(a, b):
# @param a, b int
# @return bool
# return bool means whether a is less than b.

class Solution(object):
    def specialSort(self, N):
        """
        :type N: int
        :rtype: List[int]
        """
        res = [1]
        for i in range(2, N+1):
            l = -1
            r = len(res) - 1

            while l < r:
                mid = l + r + 1 >> 1
                if compare(res[mid],i):
                    l = mid
                else:
                    r = mid - 1

            res.insert(l+1, i)

        return res
