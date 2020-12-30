class Node:
    """
    Linked List in Python
    """
    data = None
    next_node = None

    def __init__(self, data):
        self.data = data

    def __repr__(self):
        return f"<Node data: {self.data}>"


N1 = Node(1)
print(N1)

N2 = Node(2)
N1.next_node = N2
print(N1, end=" ")
print(N1.next_node)

class LinkedList:
    head = None

    def is_empty(self):
        return self.head == None
    
    def size(self):
        current = self.head
        count = 0
        while(current != None):
            count += 1
            current = current.next_node
        return count

    def insert(self, data):
        # if list is empty
        if self.head == None:
            self.head = Node(data) 
        else:
            last = self.head
            while last.next_node != None:
                last = last.next_node
            last.next_node = Node(data)
    
    def remove(self, index):
        if self.head == None:
            print('The list is empty!')
        else:
            count = self.size()
            if index >= count:
                print('Index is out of bound!')
            else:
                # removing the first element
                if index == 0:
                    self.head = self.head.next_node
                else:
                    count = 0
                    current = self.head
                    while current != None:
                        last = current
                        current = current.next_node
                        count += 1
                        if index == count:
                            last.next_node = current.next_node
                            break
                            
    def search(self, data):
        current = self.head
        found = False
        while current != None:
            if current.data == data:
                found = True
                break
            current = current.next_node
        return found


    def print(self):
        current = self.head
        print('<Singly LinkedList>')
        print('-------------------')
        if current == None:
            print('<empty>', end=' ')
        else:
            while current != None:
                print(current, end=' ')
                current = current.next_node
        print('\n-------------------')

    
    def display(self):
        disp = []
        current = self.head
        while current != None:
            if current == self.head:
                disp.append(f'[Head: {current.data}]')
            elif current.next_node == None:
                disp.append(f'[Tail: {current.data}]')
            else:
                disp.append(f'[{current.data}]')
            
            current = current.next_node
        
        print(' -> '.join(disp))


myLinkedList = LinkedList()
myLinkedList.insert(1)
myLinkedList.insert(2)
myLinkedList.insert(3)
myLinkedList.insert(4)
myLinkedList.insert(5)
print('Size of the list: ', myLinkedList.size())
myLinkedList.print()
myLinkedList.display()

print('3 exists in the list: ', myLinkedList.search(3))

myLinkedList.remove(0)
myLinkedList.print()

myLinkedList.remove(3)
myLinkedList.print()
    
myLinkedList.remove(10)
myLinkedList.remove(myLinkedList.size()-1)
myLinkedList.remove(myLinkedList.size()-1)
myLinkedList.remove(myLinkedList.size()-1)
myLinkedList.print()