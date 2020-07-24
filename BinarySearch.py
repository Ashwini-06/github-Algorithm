#!/usr/bin/env python3
# -*- coding: utf-8 -*-
class TreeEmptyError(Exception):
    pass

class Node:
    def __init__(self,value):
        self.info=value
        self.lchild=None
        self.rchild=None

class BinarySearch:
    def __init__(self):
        self.root=None
    
    def is_empty(self):
       return self.root == None
       
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
     
#Recursive Method of BST
    def search(self,x): #if x is present in the tree it will return True otherwise False
        return self._search(self.root,x) is not None # it will call recursive method for searching BST
        
    def _search(self,p,x):
        if p is None:
            return None # key not found
        if x<p.info: # Search in left subtree
            self._search(p.lchild,x)
        if x > p.info: # search in right subtree
            self._search(p.rchild)
        return p # key found

#Iterative Method of BST 
    def search1(self,x):
        p=self.root
        while p is not None:
            if x < p.info:
                p=p.lchild # Move to left child
            if x > p.info:
                p = p.rchild # Move to right child
            return True
        return False
#Insertion in a Binary Search Tree (Iterative Method)
    def insert1(self,x):
        p=self.root
        par=None
        while p is None:
            par = p
        if x < p.info:
             p=p.lchild
        elif x > p.info:
            p = p.rchild
        else:
            print(x,"is already present in the tree")
        return
    
        temp = Node(x)
        if par == None:
            self.root = temp
        elif x < p.info:
            par.lchild = temp
        elif x > p.info:
            par.rchild = temp

# Insertion in a BST with Recursive Method
    def insert2(self,x):
        self.root = self._insert(self.root , x) # insert the new node in BST
    
    def _insert(self, p, x):
        if p is None:
            p = Node(x)
        elif x < p.info:
            p.lchild = self._insert(p.lchild, x)
        elif x > p.info:
            p.rchild = self._insert(p.rchild,x)
        else:
            print(x,"is already present in the tree")
        return p

#Deletion of node using Iterative Method
    def delete1(self,x):
        p = self.root
        par = None
        
        while p is not None:
            if x == p.info:
                break
            par = p
            if x < p.info:
                p = p.lchild
            else:
               p = p.rchild
        if p == None:
            print(x,"is not found")
            return
# Case C :2 children
# Find inorder successor and its parent

        if p.lchild is not None and p.rchild is not None:
            ps = p
            s = p.rchild
            
            while s.lchild is not None:
                ps = s
                s = s.lchild
            p.info = s.info
            p = s
            par = ps

# Case B and Case A : 1 or no child
        if p.lchild is None: # Node to be deleted has lchild
            ch = p.lchild
        else:
            ch = p.rchild # Node to be deleted has rchild or no child
        if par == None: # Node to be deleted is a root node
            self.root = ch
        elif p == par.lchild: #node is left child of its parent
            par.lchild = ch
        else: # node is right child of its parent
            par.rchild = ch

# Recursive Method for deletion of BST
    def delete2(self, x):
        self.root = self._delete(self.root,x)

    def _delete(self,p,x):
        if p is None:
            print(x,"is not found")
            return p
        if x < p.info: # delete from left subtree
            p.lchild = self._delete(p.lchild,x)
        elif x > p.info: # delete from right subtree
            p.rchild = self._delete(p.rchild,x)
        else:
            #key to be deleted is found
            if p.lchild is not None and p.rchild is not None: # 2 Children
                s = p.rchild
                while s.lchild is not None:
                    s = s.lchild
                p.info = s.info
                p.rchild = self._delete(p.rchild,s.info)
            
            else: # 1 or no child
                if p.lchild is not None: # only left child
                    ch = p.lchild
                else: #only right child or no child
                    ch = p.rchild
                p = ch
            return p
        
# Iterative Method to find Min & Max in Binary Search Tree
    def min1(self):
        if self.is_empty():
            raise TreeEmptyError("Tree is Empty")
        p = self.root
        while p.lchild is not None:
            p = p.lchild
        return p.info
    
    def max1(self):
        if self.is_empty():
            raise TreeEmptyError("Tree is Empty")
        p = self.root
        while p.rchild is not None:
            p = p.rchild
        return p.info

# Recursive method to find Min & Max in Binary Search Tree
    def min2(self):
        if self.is_empty():
            raise TreeEmptyError("Tree is Empty")
        return self._min(self.root).info
    
    def _min(self,p):
        if p.lchild is None:
            return p
        return self._min(p.lchild)
        
    def max2(self):
        if self.is_empty():
            raise TreeEmptyError("Tree is Empty")
        return self._max(self.root).info
    
    def _max(self,p):
        if p.rchild is not None:
            return p
        return self._max(p.rchild)
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

bst = BinarySearch()

while True:
    print("1. Display the Tree")  
    print("2. Search the Tree by Iterative Method")  
    print("3. Search the Tree by Recurssive Method")  
    print("4. Insert the Tree by Recurssive Method")  
    print("5. Insert the Tree by Iterative Method")  
    print("6. Delete the Tree by Recurssive Method")  
    print("7. Delete the Tree by Iterative Method")  
    print("8. Find Min Key by Recurssive Method")  
    print("9. Find Max Key by Recurssive Method")  
    print("10.Find Min Key by Iterative Method")  
    print("11.Find Max Key by Iterative Method")  
    print("12. Preorder: ")
    print("13. Postorder: ")
    print("14.Inorder: ")
    print("15. Height of the tree")
    print("16. Quit")
    
    choice =int(input("Enter your choice : "))
    
    if choice ==1:
        bst.display()
    elif choice ==2:
       x=int(input("Enter the key to be searched: "))
       if bst.search1(x):
           print("key found")
       else:
           print("key not found")
    elif choice ==3:
        x=int(input("Enter the key to be searched: "))
        if bst.search(x):
            print("key found")
        else:
            print("key not found")
    elif choice == 4:
        x=int(input("Enter the key to be inserterd: "))
        bst.insert2(x)
    elif choice == 5:
        x=int(input("Enter the key to be inserterd: "))
        bst.insert1(x)
    elif choice == 6:
        x=int(input("Enter the key to be deleted: "))
        bst.delete2(x)
    elif choice == 7:
        x=int(input("Enter the key to be deleted: "))
        bst.delete1(x)
    elif choice == 8:
        print("Min key is: ", bst.min2())
    elif choice == 9:
        print("Max key is: ", bst.max2())
    elif choice == 10:
        print("Min key is: ", bst.min1())
    elif choice == 11:
        print("Max key is: ", bst.min1())
    elif choice == 12:
        bst.preorder()
    elif choice == 13:
        bst.postorder()
    elif choice == 14:
        bst.inorder()
    elif choice == 15:
        print("Hdight of the tree is: ", bst.height())
    elif choice == 16:
        break
    else:
        print("Wrong Choice")
    print






    
  
            
            
            
                

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        