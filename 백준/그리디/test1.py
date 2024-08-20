class Queue:
    def __init__(self):
        self.list = []  # 큐를 저장할 리스트를 초기화합니다.

    def enqueue(self, item):
        self.list.append(item)  # 새로운 요소를 큐의 끝에 추가합니다.

    def dequeue(self):
        if not self.isempty():  # 큐가 비어 있지 않으면
            return self.list.pop(0)  # 큐의 앞에서 요소를 제거하고 반환합니다.
        else:
            print("Queue is empty")  # 큐가 비어있으면 메시지를 출력하고 None을 반환합니다.
            return None

    def isempty(self):
        return len(self.list) == 0  # 큐가 비어있는지 확인합니다.

queue = Queue()
queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)

print(queue.dequeue())
print(queue.dequeue())
print(queue.dequeue())