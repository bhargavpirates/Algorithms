class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
    def getdata(self):
        return self.data
        
class linkedlist:
    def __init__(self,head=None):
        self.head=head
        
    def add(self,data):
        temp=Node(data)
        if(self.head==None):
            self.head=temp
        else:
            #self.head.next=temp.data
            lastnode=self.head
            while(lastnode.next is not  None):
                #if(lastnode.next is None):
                 #   break
                lastnode=lastnode.next
            lastnode.next=temp
            
    def addHead(self,data):
        temp=Node(data)
        if(self.head==None):
            self.head=temp
        else:
            #print(self.head.data)
            second=self.head
            self.head=temp
            self.head.next=second
            del second
   
    def addBetween(self,data,atwhatindex):
        current=self.head
        count=0
        while(current is not None):
            count+=1
            #current=current.next
            if(count==atwhatindex):
                temp=current.next
                current.next=Node(data)
                current.next.next=temp
            current=current.next
                
        
    def printnode(self):
        current=self.head
        if(current is None):
            print("list is Empty")
        else:
            while(current!=None):
                print(current.data)
                current=current.next
                
    def delete(self):
        current=self.head
        while(current.next is not None):
            previous=current
            current=previous.next
        print(previous.data)
        previous.next=None
        
    def deleteInBetween(self,Index):
        current=self.head
        count=0
        if(Index<0 or Index>=self.size()):
            print("NOt Valid Index")
            return
        if(self.head is None):
            print("List is empty")
            return 
        while(current is not None):           
            if(count==Index-1):
                temp=current.next.next
                current.next=temp
            count+=1
            current=current.next    
            
    def size(self):
        current=self.head
        print(current.data)
        print(current.next)
        count=0
        while(current!=None):
            count+=1
            current=current.next
        return count
    
    def search(self,findData):
        current=self.head
        found=False
        while(current is not None):
            if(current.data == findData):
                print("Data is present in linked list")
                found=True
                return
            current=current.next
        print("Data is not present")
                
            
ll=linkedlist()

ll.add("Satyanarayana")
ll.add("lakshmi")
ll.add("Bhargav")
ll.add("pavan")

#ll.printnode()
#print(ll.size())
ll.addHead("Family Members")
ll.addBetween(20,2)
ll.printnode()
#ll.delete()
ll.deleteInBetween(2)
ll.printnode()
ll.search("12pavan")
#nodeA=Node(5)

#nodeB=Node(8)
#print(nodeA.data)
#print(nodeB.data)
#print(nodeA.getdata())
#print(nodeB.getdata())
#print('*'*9)
#nodeA.next=nodeB
#print(nodeA.data)
#print(nodeA.next.data)