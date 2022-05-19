from stack import Stack

def is_match(s1, s2):
    if s1 == "(" and s2 == ")":
        return True
    elif s1 == "[" and s2 == "]":
        return True
    elif s1 == "{" and s2 == "}":
        return True
    else:
        return False

def is_balanced(paren):
    if paren == "":
        return True

    s = Stack()

    for i in range(len(paren)):
        if paren[i] in "([{":
            print("pushes")
            s.push(paren[i])
        else:
            if paren[i] == "":
                return False
            elif is_match(s.peek(), paren[i]):
                print("pops")
                s.pop()
            else:
                return False
        print(s.get_stack())
        '''
        elif not s.is_empty() and is_match(s.peek(), paren[i]) and paren[i] == ")" or paren[i] == "]" or paren == "}":
            s.pop()
        elif s.is_empty():
            return False
        '''


    return s.is_empty()


    '''
    s.push(paren[0])

    if paren[1] != "":
        i = paren[1]
    else:
        return False

    for i in paren:
        if i != "" and i == "(":
            s.push(i)
        elif i != "" and i == ")":
            s.pop()
        print(s.get_stack())

    return s.is_empty()
    '''


if __name__ == '__main__':
    print(is_balanced("([)]"))