class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        temp = ListNode()
        tail = temp
        cur1 = list1
        cur2 = list2

        while cur1 and cur2:
            if cur1.val < cur2.val :
                tail.next = cur1
                cur1 = cur1.next
                tail = tail.next
            else:
                tail.next = cur2
                cur2 = cur2.next
                tail = tail.next

        if cur1:
             tail.next = cur1

        if cur2:
            tail.next = cur2

        return  temp.next