# Function to check if the character is an operator
def is_operator(char):
    return char in ['+', '-', '*', '/', '^']

# Function to check precedence of operators
def precedence(op):
    if op == '^':
        return 3
    elif op in ['*', '/']:
        return 2
    elif op in ['+', '-']:
        return 1
    else:
        return 0

# Function to convert infix expression to prefix expression
def infix_to_prefix(expression):
    # Reversing the infix expression
    reversed_infix = expression[::-1]

    stack = []
    output = ''

    for char in reversed_infix:
        if char.isalnum():
            output += char
        elif char == ')':
            stack.append(char)
        elif char == '(':
            while stack and stack[-1] != ')':
                output += stack.pop()
            stack.pop()  # Discard '('
        elif is_operator(char):
            while stack and precedence(stack[-1]) > precedence(char):
                output += stack.pop()
            stack.append(char)

    while stack:
        output += stack.pop()

    # Reversing the obtained postfix expression to get the prefix expression
    prefix_expression = output[::-1]
    return prefix_expression

# Example usage
infix_expression = "(A + B) * C - D / E"
prefix_result = infix_to_prefix(infix_expression)
print("Prefix expression:", prefix_result)
