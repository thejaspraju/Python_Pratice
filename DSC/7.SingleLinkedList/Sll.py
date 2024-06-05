class Node:
    def __init__(self, val) -> None:
        self.val = val
        self.next = None
 
 
class SinglyLinkedList:
    def __init__(self) -> None:
        self.head = None
 
    def append(self,value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            temp.next = new_node
    
    def traverse(self):
        if self.head is None:
            print("SLL is emply, can not traverse")
            return
        temp = self.head
        while temp is not None:
            print(temp.val,end=" ")
            temp = temp.next
        print()

    def inserAtstart(self,value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node
    def insert(self,value,index):
        new_node = Node(value)
        if index == 0:
            pass
        else:
            temp = self.head
            count = 0
            while temp:
                count += 1
                if count == index:
                    break
            temp = temp.next
        new_node.next = temp.next
        temp.next = new_node


sll = SinglyLinkedList()
sll.append(100)
sll.append(200)
sll.append(300)
sll.append(700)
sll.append(900)
sll.inserAtstart(24)
sll.insert(5,6)
sll.traverse()