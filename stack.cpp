#include <iostream>
using namespace std;

class StackReplica
{
private:
    int size = 100;
    int stack[100];

public:
    int top = -1;
    void push(int value)
    {
        if (top >= size - 1)
        {
            cout << "Stack Overflow";
        }
        else
        {
            top++;
            stack[top] = value;
        }
    }

    int pop()
    {
        if (top <= -1)
        {
            return -1;
        }
        else
        {
            int top_temp = stack[top];
            top--;
            return top_temp;
        }
        return 0;
    }

    int peak()
    {
        return stack[top];
    }

    int capacity()
    {
        return this->top + 1;
    }

    bool is_empty()
    {
        if (top == -1)
        {
            return true;
        }
        return false;
    }

    bool is_full()
    {
        if (top == size - 1)
        {
            return true;
        }
        return false;
    }
};
