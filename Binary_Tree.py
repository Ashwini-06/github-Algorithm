#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 23 13:44:54 2020

@author: anerker
"""
from collections import deque 
class Node:
    def __init__(self,value):
        self.info=value
        self.lchild=None
        self.rchild=None
        
class BinaryTree:
    def __init__(self):
        self.root = None
    
    def is_empty(self):
        return self.root==None
    
    def display(self):
        self._display(self.root,0)
        print()
    
    def _display(self,p,level):
        if p is None:
            return
        self._display(p.rchild,level+1)
        print()
        
        for i in range(level):
            print("  ",end='')
        print(p.info)
        self._display(p.lchild,level+1)
     
# Preorder Traversal(NLR)
    def preorder(self): #Inside this method we call recursive method with root as argument
        self._preorder(self.root)
        print()
    
    def _preorder(self,p): # This is the recusive method in which p denotes the root of the subtree
        if p is None:
            return
        print(p.info," ",end='') # Print the info if p is not none 
        self._preorder(p.lchild) # Left order traversal
        self._preorder(p.rchild) # Right order traversal
    
# Inorder Traversal (LNR)
    def inorder(self):
        self._inorder(self.root)
        print()

    def _inorder(self,p):
        if p is None:
            return
        self._inorder(p.lchild) 
        print(p.info," ",end='')
        self._inorder(p.rchild)

#Postorder Traversal (LRN)
    def postorder(self):
        self._postorder(self.root)
        print()

    def _postorder(self,p):
        if p is None:
            return
        self._postorder(p.lchild)
        self._postorder(p.rchild)
        print(p.info," ",end='')
    
    def level_order(self):
        if self.root is None:
            print("Tree is Empty")
            return
        qu = deque() # deque is use for inserting or removing the elements
        qu.append(self.root) #insert root node in queue
    
        while len(qu)!= 0: # It will run till the queue is not empty
            p = qu.popleft()  # Remove the element from queue
            print(p.info," ",end='') # Print the removed element
            if p.lchild is not None:    # visit the left side of printed element
                qu.append(p.lchild) # Add in queue  if left side is not none
            if p.rchild is not None:
                qu.append(p.rchild) #Add in queue if right side is not none

# Find height of Binary Tree
    def height(self):
        return self._height(self.root)

    def _height(self,p):
        if p is None:
            return 0
        hL= self._height(p.lchild) # Left Child
        hR = self._height(p.rchild) # Right Child
        if hL>hR:
            return 1 + hL # if left child is greater return the height by adding 1 
        else:
            return 1 + hR #if right child is greater return the height by adding 1

    def create_tree(self): # Creating Tree
        self.root = Node('P')
        self.root.lchild = Node('Q')
        self.root.rchild = Node('R')
        self.root.lchild.lchild= Node('A')
        self.root.lchild.rchild= Node('B')
        self.root.rchild.lchild= Node('X')

bt = BinaryTree()

bt.create_tree()

bt.display()
print()

print("Preorder: ")
bt.preorder()
print("")

print("Inorder: ")
bt.inorder()
print("")

print("Postorder: ")
bt.postorder()
print("")

print("Level order: ")
bt.level_order()
print("")

print("Height of a tree is: ",bt.height())   
    
    
    
    

 




