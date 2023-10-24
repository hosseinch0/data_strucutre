#include <iostream>
using namespace std;

class Queue
{
private:
    int queue[10];
    int cruiser;

public:
    Queue()
    {
        cruiser = -1;
    }

    void enqueue(int value)
    {
        if (cruiser == -1)
        {
            cruiser++;
            queue[cruiser] = value;
        }
        else
        {
            cruiser++;
            queue[cruiser] = value;
        }
    }

    void dequeue()
    {
        if (cruiser != -1)
        {
            cout << queue[0] << " Left the Queue." << endl;

            for (int i = 0; i <= cruiser; i++)
            {
                queue[i] = queue[i + 1];
            }
            cruiser--;
        }
    }

    void front()
    {
        cout << "The Front Element is : " << queue[0] << endl;
    }

    void rear()
    {
        cout << "Rear Element is : " << queue[cruiser] << endl;
    }

    void display()
    {
        for (int i = 0; i <= cruiser; i++)
        {
            cout << "(" << i + 1 << ") " << queue[i] << "\t";
        }
    }

    void size()
    {
        cout << "Occupied : " << cruiser + 1 << endl;
    }
};

int main()
{
    Queue replica = Queue();
    return 0;
}