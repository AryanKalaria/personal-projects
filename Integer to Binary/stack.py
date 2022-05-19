# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

class Stack():
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def get_stack(self):
        return self.items

    def is_empty(self):
        return self.items == []

    def peek(self):
        if not self.is_empty():
            return self.items[-1]

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    s = Stack()
    print(s.is_empty())
    s.push("A")
    s.push("B")
    s.push("C")
    s.push("D")
    print(s.get_stack())
    print(s.pop())
    print(s.pop())
    print(s.get_stack())
    print(s.peek())
    print(s.is_empty())

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
