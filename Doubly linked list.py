class node:
    def __init__(self, data=None):
        self.next=None
        self.prev=None
class DoublyLinkedList:
    def __init__(self):
        self.first=None
    def insertatend(self, data):
        newnode=Node(data)
        if self.first==None:
            self.first=newnode
        else:
            cur=self.first
            while cur.next!=none:
                cur=cur.next
            cur.next=newnode
            newnode.prev=cur
    def removeFirst(self):
        if(self.first==None):
            print("list is empty")
        else:
            cur=self.first
            self.first=self.first.next
            print("the deleted item is",cur.data)
    def display(self):
        if(self.first==None):
            print("list is empty")
            return
        cur=self.first
        while(cur):
            print(cur.data,end=" ")
            cur=cur.next
    def search(self,item):
        if (self.first==None):
            print("list is empty")
            return
    def search(self,item):
         if(self.first==None):
             print("list is empty")
             return
         cur = self.first
         found=False
         while cur!=None and not found:
            if cur.data==item:
                found=True
            else:
                cur=cur.next
            if found:
                print("the data item is present in the list")
            else:
                print("{the data item is not present")
dll=DoublyLinkedList()
while(True):
    choice=int(input("\nEnter your choice 1-insert at end 2-delete from first 3-search 4-display 5.exit:"))
    if ( choice == 1):
        item=input("Enter the element to insert:")
        dll.removeFirst()
        dll.display()
    elif ( choice==2):
        dll.removeFirst()
        dll.display()
    elif ( choice==3):
        item = input("enter the element to search:")
        dll.search(item)
    elif ( choice==4):
        dll.display()
    else:
        break
            
