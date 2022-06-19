'''
* 힙 : 최댓값과 최솟값을 빠르게 찾기 위해 고안된 자료구조
- 최대힙 : key(T.parent(v)) > key(v)
- 최소힙 : key(T.parent(v)) < key(v)
- 시간복잡도 : O(logn)
- 노드 추가: heapq.heappush(heap, 1)
- 노드 삭제: heapq.heappop(heap) / 가장 작은 원소를 꺼내 리턴
'''

import heapq        # 최소힙으로 사용 가능하도록 함.

'''
힙의 인덱스는 각 깊이에 따라 인덱스 값이 주어짐.
원소(k)는 항상 자식 원소들(2k+1, 2k+2) 보다 크기가 작거나 같도록 원소가 추가되고 삭제됨.

'''
list1 = [1, 2, 3, 4]
heapq.heapify(list1)

heap = []
heapq.heappush(heap, 4)
heapq.heappush(heap, 1)
heapq.heappush(heap, 7)
heapq.heappush(heap, 3)
print(heap)     # [1,3,7,4]
'''
1. heap[0] : 가장 작은 1
2. heap[1(k)] : 3 < heap[2k(1)+1] = heap[3] = 4

'''

heap2 = [50 ,10, 20]
heapq.heapify(heap2)    # 힙 자료형으로 변환

print(heap2)    # [10,50,20]

# 최대힙
def max_heap(heap_items):
    heap = []

    for item in heap_items:
        heapq.heappush(heap, (-item, item))  # (우선 순위, 값)

    while heap:
        print(heapq.heappop(heap)[1])  # index 1

# 최대힙 (우선순위,값)
list2 = [(1, 10), (2, 9), (3, 8), (4, 7)]
heapq.heapify(list2)

max_heap([1,3,5,7,9])   # 9 7 5 3 1