class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)   # simpler way

    def pop(self):
        if not self.isEmpty():
            return self.stack.pop()   # Python’s built-in pop
        else:
            return "Stack is empty"

    def peek(self):
        if not self.isEmpty():
            return self.stack[-1]   # last element
        else:
            return "Stack is empty"

    def isEmpty(self):
        return len(self.stack) == 0

    def size(self):
        return len(self.stack)

    def display(self):
        return self.stack    # show actual stack


# Testing
s = Stack()
print("Initial stack:", s.display())
s.push(10)
s.push(20)
s.push(30)
print("Stack after pushes:", s.display())
print("Top element (peek):", s.peek())
print("Removed element (pop):", s.pop())
print("Stack after pop:", s.display())
print("Is stack empty?", s.isEmpty())
print("Stack size:", s.size())


def next_greater_element_dict(arr):
    n = len(arr)
    result = {}
    stack = []
    
    for i in range(n-1, -1, -1):  # Traverse from right to left
        while stack and stack[-1] <= arr[i]:
            stack.pop()
        
        # If stack not empty → next greater exists
        if stack:
            result[arr[i]] = stack[-1]
        else:
            result[arr[i]] = -1
        
        stack.append(arr[i])
    
    return result


# Example usage
arr = [4, 5, 2, 25]
print(next_greater_element_dict(arr))


def next_greater_element_dict(arr):
    result = {}
    stack = []
  
    for num in arr:
     while stack and stack[-1] < num:
           result[stack.pop()] = num
     stack.append(num)
     
     while stack:
          result[stack.pop()] = -1

    
    return result
# Example usage
arr = [4, 5, 2, 25]
print("next greater elemnts:",(arr))



def isBalanced(s):
    stack = []
    # Mapping of closing to opening brackets
    pairs = {')': '(', '}': '{', ']': '['}
    
    for ch in s:
        if ch in "({[":   # If opening bracket → push to stack
            stack.append(ch)
        elif ch in ")}]": # If closing bracket
            if not stack or stack[-1] != pairs[ch]:
                return "not balanced"
            stack.pop()
    
    # Balanced if stack is empty at the end
    return "balanced" if not stack else "not balanced"


# Test cases
print(isBalanced("{[()]}"))   # True (Balanced)
print(isBalanced("{[(])}"))   # False (Not Balanced)


def reverseString(s):
    stack = []
    
    # Push all characters onto stack
    for ch in s:
        stack.append(ch)
    
    reversed_str = ""
    
    # Pop all characters from stack
    while stack:
        reversed_str += stack.pop()
    
    return reversed_str


# Test
print(reverseString("Hello"))