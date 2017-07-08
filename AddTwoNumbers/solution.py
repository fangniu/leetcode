 # Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        carry = 0
        root = tmp_node = ListNode(0)
        while True:
            tmp_sum = 0
            if l1:
                tmp_sum += l1.val
                l1 = l1.next
            if l2:
                tmp_sum += l2.val
                l2 = l2.next
            carry, tmp_node.val = divmod(tmp_sum + carry, 10)
            if l1 is None and l2 is None and carry == 0:
                return root
            tmp_node.next = ListNode(0)
            tmp_node = tmp_node.next

if __name__ == '__main__':
    test_l1 = ListNode(4)
    test_l1.next = ListNode(4)
    test_l1.next.next= ListNode(4)
    test_l2 = ListNode(7)
    ret = Solution().addTwoNumbers(test_l1, test_l2)
    while ret:
        print ret.val
        ret = ret.next
