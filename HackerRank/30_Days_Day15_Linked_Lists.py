class Node:
    def __init__(self,data):
        self.data = data
        self.next = None 
class Solution: 
    def display(self,head):
        current = head
        while current:
            print(current.data,end=' ')
            current = current.next
    def insert(self,head,data):
        node = Node(data)
        if head:        #if bool(head)  . False when empty or None or 0
            current = head
            while current.next:
                current=current.next
            current.next = node
            return head
        else:           #if head is blank . return new node created
            return node 

"""  # Recursion
    def insert(self,head,data): 
    #Complete this method
        if(head==None):
            head = Node(data)
        elif(head.next == None):
             head.next = Node(data)  
        else:
            self.insert(head.next,data)
        return head

"""
mylist= Solution()
