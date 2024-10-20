#WAP linkedlist

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

start = None

def printlist():
    if start is None:
        print("List is empty")
        return
    currentNode = start
    while currentNode is not None:
        print(currentNode.data, end=" -> " if currentNode.next is not None else "")
        currentNode = currentNode.next
    print()

while True:
    k = int(input("\nEnter 1 to insert at the start of the linked list \nEnter 2 to insert at the end of the linked list \nEnter 3 to insert at any point in the linked list \nEnter 7 to print the linked list \nEnter 8 to break \n "))
    
    if k == 1:
        ptr = Node(int(input("Enter the value: ")))
        if start is None:
            start = ptr
        else:
            ptr.next = start
            start = ptr

    if k == 2:
        ptr1 = Node(int(input("Enter the value: ")))
        if start is None:
            start = ptr1
        else:
            ptr = start
            while ptr.next is not None:
                ptr = ptr.next
            ptr.next = ptr1
    
    if k == 3:
        pos = int(input("Enter the position: "))
        ptr1 = Node(int(input("Enter the value: ")))
        count= 1
        ptr = start
        while ptr.next is not None:
            count += 1
            if count is pos:
                ptr1.next = ptr.next
                ptr.next = ptr1
                break
            ptr = ptr.next
    if k == 7:
        printlist()
    
    if k == 8:
        break
