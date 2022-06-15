'''
큐(queue) : 먼저 집어넣은 데이터가 먼저 나오는 성질
- List 자료구조 사용하기 : pop(0) 연산의 경우 O(n)이어서 연산이 매우 느려지기 때문에 비추
- Collections 모듈의 deque 사용하기
- queue 모듈의 Queue 클래스 사용하기
'''

# List
queue = [1, 2, 3]
queue.append(4)
queue.append(5)
print(queue)    # [1, 2, 3, 4, 5]
queue.pop(0)    # 1 / 맨 앞 요소를 제거&return
queue.pop(0)    # 2
print(queue)    # [3, 4, 5]


# deque : popleft() == pop(0)
from collections import deque

queue = deque([1, 2, 3])
queue.append(4)     # [1,2,3,4]
queue.popleft()     # 1
queue.popleft()     # 2


# Queue : deque와 달리 방향성이 없기 때문에 데이터 추가와 삭제가 하나의 메서드로 처리된다.
# 데이터를 추가 할 때 : put(x) 메서드를 사용
# 데이터 삭제 : get() 메서드 사용

from queue import Queue

que = Queue()   # init: <queue.Queue object at 0x00000293C27BFB48>
que.put(1)      # 
que.put(2)      # 
que.put(3)      # 
que.get()       # 1
que.get()       # 2
