class Queue:
    def __init__(self, size=None):
        if size is not None:
            self.__buff = [0] * size
            self.__front = 0  # 큐의 첫 번째 요소를 가리킵니다.
            self.__rear = 0   # 큐의 마지막 요소 바로 다음 인덱스를 가리킵니다.
            self.size = size
        else:
            self.list = []
            self.size = None

    def isfull(self):
        if self.size is None:
            return False  # 동적 리스트는 꽉 찰 수 없습니다.
        return (self.__rear - self.__front) == self.size

    def isempty(self):
        if self.size is None:
            return len(self.list) == 0
        return self.__rear == self.__front

    def enqueue(self, val):
        if self.size is not None:
            if self.isfull():
                print("Queue is full")
            else:
                self.__buff[self.__rear % self.size] = val
                self.__rear += 1
        else:
            self.list.append(val)

    def dequeue(self):
        if self.size is not None:
            if self.isempty():
                print("Queue is empty")
                return None
            val = self.__buff[self.__front % self.size]
            self.__front += 1
            return val
        else:
            if self.isempty():
                print("Queue is empty")
                return None
            return self.list.pop(0)

q = Queue(5)

q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
print(q.dequeue())  # 출력: 10
print(q.dequeue())  # 출력: 20

q.enqueue(40)
q.enqueue(50)
q.enqueue(60)
print(q.dequeue())  # 출력: 30