import math
from stack import Stack

def convert_to_str(li):
    s = ""
    for i in li:
        s = s + str(i)
    return s

def reverse_stack(s):
    li = []
    while not s.is_empty():
        li.append(s.pop())
    return li

def int_to_binary(num):
    if num == 0:
        return 0
    rem = Stack()
    while num > 0:
        rem.push(num % 2)
        num = math.trunc(num / 2)
    s = convert_to_str(reverse_stack(rem))
    return s

if __name__ == '__main__':
    print(int_to_binary(0))