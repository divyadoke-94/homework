

class Queue:
    def _init_(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if not self.isEmpty():
            front_element = self.queue[0]
            self.queue = self.queue[1:]
            return front_element
        else:
            return "queue underflow"

    def peek(self):
        if not self.isEmpty():
            return self.queue[0]
        else:
            return "queue is empty"

    def isEmpty(self):
        return len(self.queue) == 0

    def size(self):
        return len(self.queue)

    def display(self):
        return self.queue


# Testing the queue
q = Queue()
print("initial queue:", q.display())

q.enqueue(100)
q.enqueue(20)
q.enqueue(30)
q.enqueue(40)
print("queue after enqueues:", q.display())
print("front element (peek):", q.peek())
print("removed element (dequeue):", q.dequeue())
print("queue after dequeue:", q.display())

print("is queue empty?", q.isEmpty())
print("queue size:", q.size())