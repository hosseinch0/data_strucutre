# ALTERNATECO.COM
# QUEUE REPLICA
class Queue:
    # USED A LIST TO STORE DATA
    queue_list = list()

    # INSERT METHOD FOR THE QUEUE
    def enqueue(self, data):
        self.queue_list.append(data)
        print(data, "Entered the queue")

    # DELETES THE FRONT OF THE QUEUE
    def dequeue(self):
        data = self.queue_list[0]
        self.queue_list.remove(data)
        print(data, "Left the queue")

    def front(self):
        front = self.queue_list[0]
        print("Front:", front)

    def rear(self):
        length = len(self.queue_list)
        print("Rear:", self.queue_list[length - 1])

    # SHOWS THE QUEUE
    def display(self):
        print("Left to right: Front to Rear")
        print(self.queue_list)

# MAKE AN OBJECT AND GO NUTS
