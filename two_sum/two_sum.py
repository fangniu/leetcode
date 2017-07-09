#!/usr/bin/env python
# _*_coding:utf-8_*_


__author__ = 'Sheng Chen'


'''
    Time complexity : O(n^2)O(n​2​). For each element, we try to find its complement by looping through the rest of 
                        array which takes O(n)O(n) time. Therefore, the time complexity is O(n^2)O(n2​).
    Space complexity : O(1)O(1).
'''


class Solution1(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        else:
            raise ValueError("No two sum solution")


# O(n) time

class Solution2(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        num_dict = {}
        for i in range(len(nums)):
            value_i = nums[i]
            value_j = target - value_i
            if value_j in num_dict:
                return [i, num_dict[value_j]]
            else:
                num_dict[value_i] = i
        else:
            raise ValueError("No two sum solution")

if __name__ == '__main__':
    print Solution2().twoSum([2, 4, 7], 11)
