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






























































































