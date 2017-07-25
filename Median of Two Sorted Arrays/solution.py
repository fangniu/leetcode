# coding=utf-8
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        k = (len(nums1) + len(nums2))/2
        if (len(nums1) + len(nums2)) % 2 == 0:
            return (self.find_kth(nums1, nums2, k + 1) + self.find_kth(nums1, nums2, k)) * 0.5
        else:
            return self.find_kth(nums1, nums2, k + 1)

    def find_kth(self, list_a, list_b, k):
        """
        :param list_a: 
        :param list_b: 
        :param k: 在2个数组中找到第K小的数; 第K小也代表合并后数组的第K个位置
        :return: float
        这个findKth()函数写的非常经典，思路如下：
            1. 保持A是短的那一个数组，B是长的
            2. 平分k, 一半在A，一半在B （如果A的长度不足K/2,那就pa就指到最后一个）
            3. 如果pa的值 < pb的值，那证明第K个数肯定不会出现在pa之前，递归，把A数组pa之前的砍掉，同理递归砍B数组。
            4. 递归到 m == 0 （短的数组用完了） 就返回 B[k - 1], 或者k == 1（找第一个数）就返回min(A第一个数，B第一个数）。
        """
        len_a = len(list_a)
        len_b = len(list_b)
        if len_a > len_b:
            return self.find_kth(list_b, list_a, k)
        if len_a == 0:
            return list_b[k-1]
        if k == 1:
            return min(list_a[0], list_b[0])
        pa = min(len_a, k/2)
        pb = k - pa
        if list_a[pa-1] <= list_b[pb-1]:
            return self.find_kth(list_a[pa:], list_b, pb)
        else:
            return self.find_kth(list_a, list_b[pb:], pa)


if __name__ == '__main__':
    print Solution().findMedianSortedArrays([1, 5], [2, 4])