class stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
         self.stack += [item]

    def pop(self):
        if not self.isEmpty():
            top_elemnt = self.stack[len(self.stack)-1]
            self.stack = self.stack[:-1]
            return top_elemnt
        else:
            return "stack is empty"
    def isEmpty(self):
        return len(self.stack)==0
    def size(self):
         return len(self.stack)
    def display(self):
         return len(self.stack)


s = stack()
print("initial stack:", s.display())
s.push(10)
s.push(20)
s.push(30)
print("stack after pushes:",s.display())
print("removed element (pop):", s.pop())
print("stack after pop:", s.display())
print("is stack empty?",s.isEmpty())
print("stack size:",s.size())

stack = [10,20,30]
removed = stack.pop()
print("removed elemnt:",removed)
print("after pop operation:",stack)

stack = [10,20,30]
print("top elemnt:",stack[-1])

stack = [10,20,30]
print("size of stack:",len(stack))

def sortStack(stack):
    temp_stack = []
    
    while stack:
        # Pop top element from original stack
        temp = stack.pop()
        
        # While temp_stack not empty and top > temp
        while temp_stack and temp_stack[-1] > temp:
            stack.append(temp_stack.pop())
        
        # Place temp in correct position
        temp_stack.append(temp)
    
    return temp_stack   # Sorted stack


# Test
stack = [34, 3, 31, 98, 92, 23]
print("Sorted Stack:", sortStack(stack))