'''
If Statement Nesting Depth

Many teams use a type of tool called a linter to scan code to ensure it follows certain standards and best practices. One common rule a linter might check for is the depth of nesting of control flow. Functions with many levels of nesting are often overly complex, hard to read or modify, and can be bug farms. We're going to write a function to determine the depth of control flow for if-statements so that teams will be automatically notified if it gets too deep.

In Visual Basic (an old language I hope most of you never need to use), if statements are bounded by four keywords: if, elseif, else, and endif. Given a sequence of these keywords, return the max nesting depth or -1 if the structure is incorrect.

The structure is incorrect when:
1. The first keyword is anything other than an if.
2. If and endif keywords do not pair up or are out of order.
3. An else or elseif is not inside an if.
4. There are two else blocks in a row.
5. An elseif follows an else at a given level.

Start by implementing this with only if, and endif. Then add support for else. Once that is working, modify the code to support elseif as well.
 

EXAMPLE(S)
vbNesting(["if"]) == -1
vbNesting(["endif"]) ==  -1
vbNesting(["if", "endif"]) == 1
vbNesting(["if", "else", "endif"]) == 1
vbNesting(["if", "endif", "if", "endif"]) == 1
vbNesting(["if", "if", "endif", "endif"]) == 2
vbNesting(["if", "if", "if", "endif", "endif", "endif"]) == 3
vbNesting(["if", "if", "if", "endif", "endif", "if", "endif", "endif"]) == 3
 

FUNCTION SIGNATURE
function vbNesting(controlFlow) {
def vbNesting(controlFlow: list[str]) -> int:

EXPLORE:

Similar to bracket balance question
is a number of levels

BRAINSTORM:
output is a maximum elements in the stack

`if` is always valid

for `else` proceeding element must be `if`

for `endif` ~ one or two pops if the first preceeding is [`else` + `if`] or `if` 

PLAN:
O(n) array iteration once
O(n) = worse case, stack is full, for valid input = O(n / 2)

OUTLINE:
create stack
create a variable for max_depth
create a variable current_depth
go over elements in input array and check individual elements
    if `if` then add to stack
        increment current_depth
        and track best
    if `else`, prev must be `if` (add `else` to stack)
        if stack is empty then return -1
        otherwise return -1
    if `endif`, pop one or two element, `else` is a conditional pop
        if stack is empty then return -1
        decrement current_depth

    if stack is not empty return -1

return max_depth
'''

def vbNesting(controlFlow: list[str]) -> int:
    
    max_depth = 0
    curr_depth = 0

    stack = []

    for token in controlFlow:

        if token == "if":

            stack.append(token)
            curr_depth += 1
            max_depth = max(max_depth, curr_depth)

        if token == "else":

            if not stack or stack[-1] == "else":
                return -1

            stack.append(token)

        if token == "endif":

            if not stack:
                return -1

            # Optionally pop else
            if stack[-1] == "else":
                stack.pop()

            # Pop an if off the stack
            stack.pop()
            curr_depth -= 1
    
    if stack:
        return -1

    return max_depth


print(vbNesting(["if"]) == -1)
print(vbNesting(["endif"]) ==  -1)
print(vbNesting(["else"]) ==  -1)
print(vbNesting(["if", "endif"]) == 1)
print(vbNesting(["if", "else", "endif"]) == 1)
print(vbNesting(["if", "endif", "if", "endif"]) == 1)
print(vbNesting(["if", "if", "endif", "endif"]) == 2)
print(vbNesting(["if", "if", "if", "endif", "endif", "endif"]) == 3)
print(vbNesting(["if", "if", "if", "endif", "endif", "if", "endif", "endif"]) == 3)
print(vbNesting(["if", "if", "if", "else", "else" "endif", "endif", "if", "endif", "endif"]) == -1)
print(vbNesting(["if", "if", "endif", "endif", "endif"]) == -1)
