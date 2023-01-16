class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0,head)
        curr = dummy
        length = 0

        while(curr):
            curr = curr.next
            length +=1

        count = length - n

        i = 0
        cur = dummy

        while cur.next is not None:
            if i == count-1:
                cur.next = cur.next.next
                return dummy.next
            cur = cur.next            
            i+=1
