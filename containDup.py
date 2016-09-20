__author__ = 'jerry'

import collections

class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        col = collections.Counter(nums)

        lst = [idx for idx,val in col.items() if val == 1]
        index = col.keys()
        if lst == index:
            return False
        else:
            return True

if __name__ == "__main__":
    so = Solution()
    nums = [1,2,3,4,5,6,7,1];
    print so.containsDuplicate(nums)