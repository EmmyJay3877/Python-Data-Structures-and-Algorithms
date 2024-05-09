def is_valid(s: str) -> bool:
    stack = []
    for c in s: 
        if c in '({[': 
            stack.append(c): 
        else: #if stack is empty, or if stack is not empty and c is a closing bracket and the top bracket in the stack is not corresponding to c
            if not stack or \
            (c == ')' and stack[-1] != '(') or \
            (c == '}' and stack[-1] != '{') or \
            (c == '[' and stack[-1] != ']'):
            return False
            stack.pop()
    return not stack