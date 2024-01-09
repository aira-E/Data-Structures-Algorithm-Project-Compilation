def infixToPostfix(exp):
    precedence = {
        '+':1,
        '-':1,
        '*':2,
        '/':2,
        '^':3,
        '(':0,
        ')':0
    }
    postfix = ''
    stack = []
    for char in exp:
        if char.isalpha() or char.isdigit():
            postfix += char
        elif char == '(':
            stack.append(char)
        elif char == ')':
            while stack[-1] != '(':
                operator = stack.pop()
                if operator:
                    postfix += operator
            stack.pop()
        elif char in precedence:
            while(len(stack) > 0 and precedence[char] <= precedence[stack[-1]]):
                postfix += stack.pop()
            stack.append(char)

    while len(stack) > 0:
        postfix += stack.pop()
    
    return postfix

infix = input("Enter the infix expression: ")
print ("Postfic Expression is: ", infixToPostfix(infix))
#print(infixToPostfix(infix))