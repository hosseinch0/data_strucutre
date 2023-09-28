# LINKED LIST
class Node:
    # constructor
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        newNode = Node(data)
        if (self.head):
            current = self.head
            while (current.next):
                current = current.next
            current.next = newNode
        else:
            self.head = newNode

    def display(self):
        current = self.head
        while (current):
            print(current.data)
            current = current.next

    def node_counts(self):
        counter = 0
        current = self.head
        while (current != None):
            current = current.next
            counter += 1
        print(counter)


sample = LinkedList()
sample.insert(3)
print(sample.head.next)
# sample.insert(4)
# sample.insert(5)
sample.display()
sample.node_counts()


# PRINTS THE OBJECT VALUES IN HEXADECIMAL FORM
''' 

print(sample.head)
print(sample.head.next)
print(sample.head.next.next)

'''
