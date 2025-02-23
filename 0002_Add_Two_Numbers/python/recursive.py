class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode], carry=0) -> Optional[ListNode]:
        if not l1 and not l2 and not carry:
            return None

        val1 = l1.val if l1 else 0
        val2 = l2.val if l2 else 0
        total = val1 + val2 + carry
        carry = total // 10

        result = ListNode(total % 10)
        result.next = self.addTwoNumbers(l1.next if l1 else None, l2.next if l2 else None, carry)
        return result
