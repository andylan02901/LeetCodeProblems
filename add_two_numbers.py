class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        curr1 = l1
        curr2 = l2
        carry = 0
        s = 0
        lastN = None
        n = None

        while curr1 and curr2 is not None:
            s = curr1.val + curr2.val
            if lastN is not None:
                lastN.next = ListNode(s % 10 + carry)
                lastN = lastN.next
            else:
                n = ListNode(s % 10)
                lastN = n
            carry = 1 if (s > 9) else 0

            curr1 = curr1.next
            curr2 = curr2.next

        if curr1 is not None:
            lastN.next = curr1
            curr1.val = curr1.val + carry
        if curr2 is not None:
            lastN.next = curr2
            curr2.val = curr2.val + carry
        if curr1 and curr2 is None:
            if carry > 0:
                lastN.next = ListNode(carry)

        return n

    def printNode(self, node):
        curr = node
        while curr is not None:
            print(curr.val)
            curr = curr.next


if __name__ == "__main__":
    l1 = ListNode(2)
    l2 = ListNode(4)
    l3 = ListNode(5)
    l1.next = l2
    l2.next = l3

    l4 = ListNode(7)
    l5 = ListNode(8)
    l6 = ListNode(4)
    l4.next = l5
    l5.next = l6

    sol = Solution()
    sol.printNode(sol.addTwoNumbers(l1, l4))


