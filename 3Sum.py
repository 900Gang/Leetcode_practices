class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
class solution(object):
    def threeSum(self,l1,l2):
        stepsum=0
        carry=0
        head=ListNode()
        current=head
        while(l1 or l2):
            if(l1):
                stepsum+=l1.val
                l1=l1.next
            if(l2):
                stepsum+=l2.val
                l2=l2.next
            current.next=ListNode()
            if stepsum+carry>=10:
                current.next.val=(stepsum+carry)-10
                carry=1
            else:
                current.next.val=stepsum+carry
                carry=0
        if carry:
            current.next=ListNode()
            current.next.val=1
        return head.next
    
print("Enter the first linked list:")
l1=eval(input())
print("Enter the second linked list:")
l2=eval(input())
s=solution()
result=s.threeSum(l1,l2)
print("The sum of the two linked lists is:")
print(result)