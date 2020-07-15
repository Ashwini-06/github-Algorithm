#!/usr/bin/env python3
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
# Insert at the end
    def insert_at_end(self,data):
        temp=Node(data)
        
        if self.start==None:
           self.start=temp
           return
        
        p=self.start
        while p.link is not None:
            p=p.link
        p.link=temp

#Create list
    def create_list(self):
        n=int(input("Enter the number of nodes : "))
        if n==0:
            return
        for i in range(n):
            data=int(input("Enter the number of elements to be inserted: "))
            self.insert_at_end(data)
            
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
            
#Merging Two Linked List
    def merge1(self,list1):
        merge_list=SingleLinkedList()
        merge_list.start=self._merge1(self.start,list1.start)
        return merge_list
    
    def _merge1(self,p1,p2):
        if p1.info<=p2.info:
            startM = Node(p1.info)
            p1=p1.link #Moving forward p1.link if p1 is smaller, p.link will become p1 for next pass
        else:
            startM=Node(p2.info)
            p2=p2.link #Moving forward p2.link if p2 is smaller , p2.link will become p2 for next pass
            
        pM = startM
        
        while p1 is not None and p2 is not None:
            if p1.info<=p2.info:
                pM=Node(p1.info)
                p1=p1.link
            else:
                pM = Node(p2.info)
                p2=p2.link
            
            pM=pM.link
            
        #If second list has finished and elements left in the first list
        while p1 is not None:
            pM = Node(p1.info)
            p1=p1.link
            pM = pM.link
            
        #If first list has finished and elements left in the second list
        while p2 is not None:
            pM=Node(p2.info)
            p2=p2.link
            pM=pM.link
        
        return startM 
    
    # Merging of rearrange of links
    def merge2(self,list2):
        merge_list=SingleLinkedList()
        merge_list.start=self._merge2(self.start,list2.start)
        return merge_list

    def _merge2(self,p1,p2):
        if p1.info<=p2.info:
            startM = p1
            p1=p1.link
        else:
            startM = p2
            p2=p2.link
        
        pM = startM
        
        while p1 is not None and p2 is not None:
            if p1.info<=p2.info:
                pM.link = p1
                pM = pM.link
                p1 = p1.link
            else:
                pM.link=p2
                pM = pM.link
                p2 =p2.link
            
        if p1 is None:
            pM.link = p2
        else:
            pM.link = p1
        
        return startM
        
############################################################################

list1 = SingleLinkedList()
list2 =SingleLinkedList()

# creating list by calling create list
list1.create_list()
list2.create_list()

# Sorting the list 
list1.bubblesort_excdata()
list2.bubblesort_excdata()

#Display first list 
print("First List -")
list1.displaylist()

#Display Second list
print("Second List -")
list2.displaylist()

#Merging by creating two list
list3 = list1.merge1(list2)
print("Merged list -")
list3.displaylist()

# shows that the orignal list is not change
print("First List -")
list1.displaylist()
print("Second List -")
list2.displaylist()

#Merging by rearranging links
list3 = list1.merge2(list2)
print("Merged List - ")
list3.displaylist()

# shows that the orignal list is not change
print("First List -")
list1.displaylist()
print("Second List -")
list2.displaylist()

        
        
        
        
        
        
        
        
        
        
        
        
                 
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
