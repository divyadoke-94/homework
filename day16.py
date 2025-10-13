#singlylinkedlist
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None



class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = new_node

    def display(self):
            curr = self.head
            while curr:
                print(curr.data, end=" -> ")
                curr = curr.next
            print("None")


s11= SinglyLinkedList()
s11.insert_at_end(10)
s11.insert_at_end(20)
s11.insert_at_end(30)
s11.insert_at_end(1.222)
s11.display()

class DNode:
    def __init__(self,data):
        self.data = data
        self.prev = None
        self.next = None

#DoublyLinkedList
class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_end(self,data):
        new_node = DNode(data)
        if not self.head:
            self.head = new_node
            return
        curr = self.head
        while curr.next:
            curr = curr.next
            curr.next = new_node

    def display(self):
            curr = self.head
            while curr:
                print(curr.data, end=" <-> ")
                curr = curr.next
            print("None")
 
d11 = DoublyLinkedList()
d11.insert_at_end(200)
d11.insert_at_end(100)
d11.insert_at_end(300)
d11.display()

#circular singly Linked List
class CNode:
    def __init__(self,data):
        self.data = data
        self.next = None

class CircularSinglyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_end(self,data):
        new_node = CNode(data)
        if not self.head:
            self.head = new_node
            new_node.next = self.head
            return
        curr = self.head
        while curr.next:
            curr = curr.next
            curr.next = new_node
            new_node.next = self.head

            
    def display(self):
        if not self.head:
            curr = self.head
            print("Empty List ")
            return
    curr= self.head
    while True:
        print(curr. data, end=" ->")
        curr = curr.next
        if curr ==  self.head:
            break
        print("(back to head)")

cs11 = CircularSinglyLinkedList()
cs11.insert_at_end(5)
cs11.insert_at_end(10)
cs11.insert_at_end(15)
cs11.display()

class CDNode:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class CircularDoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_end(self, data):
        new_node = CDNode(data)
        if not

    def display(self):
            if not self.head:
                print("Empty List")
                return
            curr = self.head
            while True:
                print(curr.data, end="<->")
                curr = curr.next
                if curr == self.head:
                    break
                print("(back to head)")

            cd11 = CircularDoublyLinkedList()
            cd11.insert_at_end(50)
            cd11.insert_at_end(60)
            cd11.insert_at_end(70)
            cd11.display()

    
                

        

