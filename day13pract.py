queue = []
print("initial queue:",queue)

queue = []
queue.append(10)
queue.append(20)
queue.append(30)
print("queue after enqueues:",queue)

queue = [10,20,30]
removed = queue.pop(0)
print("removed element:",removed)
print("queue after dequeue:",queue)

queue = [10,20,30]
print("front element:",queue[0])

queue = []  
print("is queue empty?",len(queue)==0)

class queueusingstacks:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def enqueue(self, item):
        self.stack.append(item)

    def dequeue(self):
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        if not self.stack2:
            return "queue underflow"
        return self.stack2.pop()
q = queueusingstacks()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
print(q.dequeue())  #10
print(q.dequeue())  #20
