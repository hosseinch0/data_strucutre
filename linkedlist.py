# LINKED LIST
# LINKED LIST CONTAINS NODES SO WE NEED A CLASS FOR NODE
class Node:
    # constructor
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

# MULTIPLE NODES MAKE A LINKED LIST SO WE HAVE A CLASS THAT CONTAINS ALL THE NODES
# THE HEAD OF LINKED LIST WILL BE ASSIGNED HERE


class LinkedList:
    def __init__(self):
        self.head = None

    # Insertion to the linked list
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

    '''
        THIS METHOD COUNTS THE NODES IN LIST
        THE MECHANISM WORKS WITH NULL/NONE VALUE OF THE next 
        IF VALUE OF THE next IN WHILE LOOP EQUALS TO NULL/NONE IT STOPS COUNTING
    '''

    def node_counts(self):
        counter = 0
        current = self.head
        while (current != None):
            current = current.next
            counter += 1
        print(counter)


sample = LinkedList()
sample.insert(3)
sample.insert(4)
sample.insert(5)
sample.display()
sample.node_counts()


# PRINTS THE OBJECT VALUES IN HEXADECIMAL FORM
''' 

print(sample.head)
print(sample.head.next)
print(sample.head.next.next)

'''
