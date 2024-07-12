def isValid(s: str) -> bool:
    # Dictionary to hold the mappings of closing to opening brackets
    bracket_map = {')': '(', '}': '{', ']': '['}
    # Stack to keep track of opening brackets
    stack = []
    
    # Iterate over each character in the input string
    for char in s:
        # If the character is a closing bracket
        if char in bracket_map:
            # Pop the top element from the stack if it's not empty, otherwise assign a dummy value
            top_element = stack.pop() if stack else '#'
            # Check if the popped element is the matching opening bracket
            if bracket_map[char] != top_element:
                return False
        else:
            # If it's an opening bracket, push it onto the stack
            stack.append(char)
    
    # If the stack is empty at the end, all brackets were properly closed
    return not stack
print("puneeth")
# Test cases
print(isValid("()"))     # True
print(isValid("()[]{}")) # True
print(isValid("(]"))     # False
print(isValid("([)]"))   # False
print(isValid("{[]}"))   # True
