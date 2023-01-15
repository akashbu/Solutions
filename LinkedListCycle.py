class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        next_arr = []
        flag = True
        cur = head
        
        while (cur != None):
            if cur in next_arr:
                return True
            else:
                next_arr.append(cur)
            cur = cur.next
            
        return False