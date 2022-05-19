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
            s.push(paren[i])
        else:
            if paren[i] == "":
                return False
            elif is_match(s.peek(), paren[i]):
                s.pop()
            else:
                return False

    return s.is_empty()
