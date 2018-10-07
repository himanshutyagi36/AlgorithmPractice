## https://www.geeksforgeeks.org/expression-evaluation/
## infix expression evaluation
# 1. While there are still tokens to be read in,
#    1.1 Get the next token.
#    1.2 If the token is:
#        1.2.1 A number: push it onto the value stack.
#        1.2.2 A variable: get its value, and push onto the value stack.
#        1.2.3 A left parenthesis: push it onto the operator stack.
#        1.2.4 A right parenthesis:
#          1 While the thing on top of the operator stack is not a 
#            left parenthesis,
#              1 Pop the operator from the operator stack.
#              2 Pop the value stack twice, getting two operands.
#              3 Apply the operator to the operands, in the correct order.
#              4 Push the result onto the value stack.
#          2 Pop the left parenthesis from the operator stack, and discard it.
#        1.2.5 An operator (call it thisOp):
#          1 While the operator stack is not empty, and the top thing on the
#            operator stack has the same or greater precedence as thisOp,
#            1 Pop the operator from the operator stack.
#            2 Pop the value stack twice, getting two operands.
#            3 Apply the operator to the operands, in the correct order.
#            4 Push the result onto the value stack.
#          2 Push thisOp onto the operator stack.
# 2. While the operator stack is not empty,
#     1 Pop the operator from the operator stack.
#     2 Pop the value stack twice, getting two operands.
#     3 Apply the operator to the operands, in the correct order.
#     4 Push the result onto the value stack.
# 3. At this point the operator stack should be empty, and the value
#    stack should have only one value in it, which is the final result.
def helper(operator,x,y):
    if operator == '+': return x + y
    if operator == '-': return x - y
    if operator == '/': return y // x
    if operator == '*': return x * y

def evaluateExpression(expr):
    operandStack = []
    operatorStack = []
    operators = {
        '/': 1,
        '*': 1,
        '+': 2,
        '-': 2
    }

    for token in expr:
        if token.isdigit():
            operandStack.append(token)
        elif token == '(':
            operatorStack.append(token)
        elif token == ')':
            while operatorStack[-1] != ')':
                result = helper(operatorStack.pop(),int(operandStack.pop()),int(operandStack.pop()))
                operandStack.append(result)
            operatorStack.pop()
        elif token in operators:
            while len(operatorStack) and operators[operatorStack[-1]] <= operators[token]:
                result = helper(operatorStack.pop(), int(operandStack.pop()), int(operandStack.pop()))
                operandStack.append(result)
            operatorStack.append(token)
    while len(operatorStack):
        result = helper(operatorStack.pop(), int(operandStack.pop()), int(operandStack.pop()))
        operandStack.append(result)

    return operandStack.pop()

print(evaluateExpression('2 + 3 * 5')) # 17
print(evaluateExpression('4 * 5 / 2')) # 10