class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        total = 0
        for curr in [l1, l2]:
            num = 0
            level = 0
            while curr is not None:
                num = curr.val * (10**level) + num
                level = level + 1
                curr = curr.next
            total += num
        print total

        digit = total % 10
        node = ListNode(digit)
        lastNode = node

        while total != None:
            if (total / 10) != 0:
                total = int(total / 10)
                lastNode.next = ListNode(total % 10)
                lastNode = lastNode.next
            else:
                total = None

        return node

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
    sol.printNode(sol.addTwoNumbers(l1, l5))


