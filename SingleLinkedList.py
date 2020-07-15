# -*- coding: utf-8 -*-
class Node:
    
    def __init__(self,value):
        self.info=value
        self.link=None

class SingleLinkedList:
    def __init__(self):
        self.start=None
 
# Display the list 
    def displaylist(self):
        if self.start==None:
            print("List is empty")
            return
        else:
            print("List is:")
            p=self.start
            while p is not None:
                print(p.info," ",end='')
                p=p.link
            print()
            
#Count the data in the list
    def countlist(self):
         p = self.start
         n=0
         while p is not None:
             n +=1
             p=p.link
             print("Number of counts in the list:",n)

#Search the position of the particular data in the list, it will return true else false
    def search(self,x):
        position=1
        p=self.start
        while p is not None:
            if p.info==x:
                print(x,"is at the position",position)
                return True
            position+=1
            p=p.link
        else:
            print(x,"not found in the list")
            return False
# Insertion at the beginning of the list
    def insert_in_beginning(self,data):
        temp=Node(data)
        temp.link=self.start
        self.start=temp
            
#Insertion at the end of the list
    def insert_at_end(self,data):
        temp=Node(data)
        
        if self.start==None:
           self.start=temp
           return
        
        p=self.start
        while p.link is not None:
            p=p.link
        p.link=temp
            
    def create_list(self):
        n=int(input("Enter the number of nodes : "))
        if n==0:
            return
        for i in range(n):
            data=int(input("Enter the number of elements to be inserted: "))
            self.insert_at_end(data)

#Insert after the node        
    def insert_after(self,data,x):
        p=self.start
        while p is not None:
            if p.info==x:
                break
            p=p.link
        if p is None:
            print(x,"is not present in the list")
        else:
            temp=Node(data)
            temp.link=p.link
            p.link=temp

#Insert at the before of the node
    def insert_before(self,data,x):
    #if list is empty
        if self.start is None:
            print("List is empty")
            return
    #x is the first node,new node is insert before the first node
        if x == self.start.info:
            temp=Node(data)
            temp.link=self.start
            self.start=temp
            return
    #Find the reference to predecessor of node contains x
        p=self.start
        while p.link is not None:
            if p.link.info==x:
                break
            p=p.link
            if p.link is None:
                print(x,"is not present in the list")
            else:
                temp=Node(data)
                temp.link=p.link
                p.link=temp
                
    def deletenode(self,x):
    #Deletion of node from between
        if self.start.info==x:
            self.start=self.start.link
            return
        p=self.start
        while p.link is not None:
             if p.link.info==x:
                 break
             p=p.link
        if p.link is None:
           print(x,"is not in the list")
        else:
            p.link=p.link.link
    #Deletion of the first node
    def delete_first_node(self):
        if self.start is None:
            return
        self.start=self.start.link
        
    #Deletion of only node
    def delete_only_node(self):
        if self.start is None:
            return
        if self.start.link is None:
            self.start=None
            return
        p=self.start
        while p.link.link is None:
            p=p.link
            p.link=None
    #Reverse the list
    def reverse_list(self):
        prev=None
        p=self.start
        while p is not None:
            next=p.link
            p.link=prev
            prev=p
            p=next
        self.start=prev
        
    # Bubble Sort Exchange of data 
    def bubblesort_excdata(self):
        end=None
        while end!=self.start.link:
            p=self.start
            while p.link!=end:
                q=p.link
                if p.info>q.info:
                    p.info,q.info=q.info,p.info #swapping of element if its greater
                p=p.link
            end=p
    # Bubble Sort Exchange of link or rearranging of data
    def bubblesort_exclinks(self):
        end =None
        while end!=self.start.link:
            r=p=self.start
            while p.link!=end:
               q=p.link
               if p.info>q.info:
                   p.link=q.link
                   q.link=p
                   if p!=self.start:
                       r.link=q
                   else:
                       self.start=q
                   p,q=q,p # swappin of elements if greater
               r=p
               p=p.link
            end=p
                
            
        
      
list= SingleLinkedList()
list.create_list()

while True:
    print("1.Display List")
    print("2.Count the list")
    print("3.Search the position of list")
    print("4.Insertion of empty list/beginning of the list")
    print("5.Insertion node at the end of list")
    print("6.Insertion after the specified node")
    print("7. Insertion before the specified node")
    print("8. Deletion of any node")
    print("9. Deletion of first node")
    print("10. Deletion of last node")
    print("11. Reverse the list")
    print("12. Bubble sort by exchanging data")
    print("13. Bubble sort by exchanging links")
    
    option=int(input("Enter your choices:"))
    
    if option==1:
        list.displaylist()
    elif option==2:
        list.countlist()
    elif option==3:
        data=int(input("Enter the element to be searched:"))
        list.search(data)
    elif option==4:
        data=int(input("Enter the element for insertion: "))
        list.insert_in_beginning(data)
    elif option==5:
        data=int(input("Enter the element at the end"))
        list.insert_at_end(data)        
    elif option==6:
        data=int(input("Insert a node after specified node"))
        x=int(input("Enter the element after which to inserted"))
        list.insert_after(data,x)
    elif option==7:
        data=int(input("Insert a node"))
        x=int(input("Enter the element before which to inserted"))
        list.insert_before(data,x)
    elif option==8:
        data=int(input("Delete node from between"))
        list.deletenode(data)
    elif option==9:
        data=int(input("Delete the first node"))
        list.delete_first_node(data)
    elif option==10:
        data=int(input("Delete the last node"))
        list.delete_last_node(data)
    elif option==11:
        list.reverse_list()
    elif option==12:
        list.bubblesort_excdata()
    elif option==13:
        list.bubblesort_exclinks()
        
        
        
        
        
