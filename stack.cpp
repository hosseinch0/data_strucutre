#include <iostream>
using namespace std;

class Stack
{
private:
    int n = 100;
    int stack[100];

public:
    int top = -1;
    void push(int value)
    {
        if (top >= n - 1)
        {
            cout << " Stack Overflow";
        }
        else
        {
            top++;
            stack[top] = value;
        }
    }

    void pop()
    {
        if (top <= -1)
        {
            cout << "Stack Is Empty";
        }
        else
        {
            cout << "The popped element is: " << stack[top];
            top--;
        }
    }

    void peak()
    {
        cout << stack[top];
    }

    void size()
    {
        cout << "Occupied : " << this->top + 1;
    }
};

int main()
{
    Stack replica = Stack();

    return 0;
}