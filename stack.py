# ALTERNATECO.COM
# STACK REPLICA
# FIRST OF ALL WE NEED A STACK CLASS
class Stack:
    # I USE A LIST TO STORE DATA AS STACK
    stack = list()

    # POP METHOD DELETES THE TOP ELEMENT OF THE STACK
    def pop(self):
        top_to_pop = self.top()
        self.stack.remove(top_to_pop)
        print(top_to_pop, "deleted from stack")

    # PUSH METHOD ADDS TO THE STACK
    def push(self, data):
        print(data, " added to stack")
        self.stack.append(data)

    # SHOWS THE STACK
    def display(self):
        print("From left to right: Top to Bottom")
        print(self.stack[::-1])

    # SHOWS THE TOP ELEMENT OF THE STACK
    def top(self):
        top = len(self.stack)
        print("Top element of the stack is: ", self.stack[top - 1])
        return self.stack[top - 1]

    # SHOWS THE BOTTOM ELEMENT OF THE STACK
    def bottom(self):
        print("Bottom element of the stack is: ", self.stack[0])

    # SHOWS THE LENGTH OF THE STACK
    def length(self):
        print("Length of the stack is :", len(self.stack))

    # MAKE AN OBJECT AND GO NUTS
