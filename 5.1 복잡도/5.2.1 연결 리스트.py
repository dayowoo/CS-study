'''
<연결 리스트>
- 싱글 연결 리스트 : next 포인터만 가지며, 한 방향으로 연결됨
- 이중 연결 리스트 : prev, next 포인터를 가짐.
- 원형 연결 리스트 : prev, next 포인터를 가짐, 마지막 노드의 next 포인터가 헤드를 가리킴
'''

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self):
        return str(self.data)


# 싱글 연결 리스트
class SingleLinkedList:
    # 노드 생성
    def __init__(self, data):
        new_node = Node(data)
        self.head = new_node
        self.list_size = 1

    def __str__(self):
        print_list = '[ '
        node = self.head
        while True:
            print_list += str(node)
            if node.next == None:
                break
            node = node.next
            print_list += ', '
        print_list += ' ]'
        return print_list

    # 첫 번째 노드 삽입
    def insertFirst(self, data):
        new_node = Node(data)       # 새 노드 생성
        temp_node = self.head       # 기존 헤드를 잠시 보관
        self.head = new_node        # 헤드를 새로운 노드로 변경
        self.head.next = temp_node  # 새로 생성된 헤드 링크를 > 기존 헤드의 링크로 변경
        self.list_size += 1

    # 중간 노드 삽입 
    def insertMiddle(self, num, data):
        if self.head.next == None:
            # 헤더가 만들어진 직후에 메서드 사용
            self.insertLast(data)
            return
        node = self.selectNode(num)
        new_node = Node(data)
        temp_next = node.next
        node.next = new_node
        new_node.next = temp_next
        self.list_size += 1

    # 마지막 노드 삽입
    def insertLast(self, data):
        node = self.head
        while True:
            if node.next == None:   # 다음 링크가 없으면
                break
            node = node.next

        new_node = Node(data)
        node.next = new_node        # 마지막 노드로 링크
        self.list_size += 1


    # 인덱스 번호로 노드 선택
    def selectNode(self, num):
        if self.list_size < num:
            print("Overflow")
            return
        node = self.head
        count = 0
        while count < num:
            node = node.next
            count += 1
        return node

    # 노드 삭제
    def deleteNode(self, num):
        if self.list_size < 1:
            return # Underflow
        elif self.list_size < num:
            return # Overflow

        if num == 0:
            self.deleteHead()
            return
        node = self.selectNode(num - 1)
        node.next = node.next.next
        del_node = node.next
        del del_node

    def deleteHead(self):
        node = self.head
        self.head = node.next
        del node

    def size(self):
        return str(self.list_size)


# 이중 연결 리스트
class DualLinkedList:
    def __init__(self, data):
        new_node = Node(data)
        self.head = new_node
        self.list_size = 1

    def __str__(self):
        print_list = '[ '
        node = self.head
        while True:
            print_list += str(node)
            if node.next == self.head:
                break
            node = node.next
            print_list += ', '
        print_list += ' ]'
        return print_list

    def insertFirst(self, data):
        new_node = Node(data)
        if not self.head.prev == None:
            new_node.prev = self.head.prev
            self.head.prev.next = new_node
        if not self.head.next == None:
            new_node.next = self.head.next
        self.head.prev = new_node
        self.head = new_node

    def insertMiddleAfter(self, num, data):
        node = self.selectNode(num)
        new_node = Node(data)
        new_node.prev = node
        new_node.next = node.next
        node.next.prev = new_node
        node.next = new_node
        self.list_size += 1

    def insertMiddleBefore(self, num, data):
        node = self.selectNode(num)
        new_node = Node(data)
        new_node.prev = node.prev
        new_node.next = node
        node.prev.next = new_node
        node.prev = new_node
        self.list_size += 1

    def insertLast(self, data):
        new_node = Node(data)
        if self.head.next == None:
            self.head.next = new_node
            new_node.prev = self.head

        if not self.head.prev == None:
            self.head.prev.next = new_node
            new_node.prev = self.head.prev
        self.head.prev = new_node
        new_node.next = self.head
        self.list_size += 1

    def selectNode(self, num):
        if self.list_size < 1:
            return # Underflow
        elif self.list_size <= num:
            return # Overflow
        count = 0
        node = self.head
        if int(self.list_size/2) > num:
            while count < num:
                node = node.next
                count += 1
        else:
            repeat = self.list_size - num
            while count < repeat:
                node = node.prev
                count += 1
        return node

    def deleteNode(self, num):
        if self.list_size < 1:
            return # Underflow
        elif self.list_size <= num:
            return # Overflow

        if num == 0:
            self.deleteHead()
            return
        node = self.selectNode(num)
        node.prev.next = node.next
        node.next.prev = node.prev
        del node

    def deleteHead(self):
        node = self.head
        node.prev.next = node.next
        node.next.prev = node.prev
        self.head = node.next
        del node

    def size(self):
        return str(self.list_size)



# 원형 연결 리스트
class CircleLinkedList:
    def __init__(self, data):
        new_node = Node(data)
        self.head = new_node
        self.tail = None
        self.list_size = 1

    def __str__(self):
        print_list = '[ '
        node = self.head
        while True:
            print_list += str(node)
            if node == self.tail:
            # 단순 연결 리스트와 달리
            # 노드가 테일 노드면 끝난다
                break
            node = node.next
            print_list += ', '
        print_list += ' ]'
        return print_list

    def insertFirst(self, data):
        new_node = Node(data)
        if self.tail == None:
            self.tail = self.head
        temp_node = self.head
        self.head = new_node
        self.head.next = temp_node
        self.tail.next = new_node
        self.list_size += 1

    def insertMiddle(self, num, data):
        node = self.selectNode(num)
        new_node = Node(data)
        temp_next = node.next
        node.next = new_node
        new_node.next = temp_next
        self.list_size += 1

    def insertLast(self, data):
        new_node = Node(data)
        if self.tail == None:
            self.tail = new_node
            self.head.next = self.tail
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.tail.next = self.head
        self.list_size += 1

    def selectNode(self, num):
        if self.list_size < num:
            print("Overflow")
            return
        node = self.head
        count = 0
        while count < num:
            node = node.next
            count += 1
        return node

    def deleteNode(self, num):
        if self.list_size < 1:
            return # Underflow
        elif self.list_size < num:
            return # Overflow

        if num == 0:
            self.deleteHead()
            return
        node = self.selectNode(num - 1)
        node.next = node.next.next
        del_node = node.next
        del del_node

    def deleteHead(self):
        node = self.head
        self.head = node.next
        del node

    def size(self):
        return str(self.list_size)





# 메인 함수의 선언, 시작
if __name__ == "__main__":
    m_list = SingleLinkedList(1)
    m_list.insertLast(5)
    m_list.insertLast(6)
    print('LinkedList :', m_list)   # [1,5,6]
    print('LinkedList Size() :', m_list.size()) # 3 
    print('LinkedList SelectNode(1) :', m_list.selectNode(1))   # 5 (list[1])

    m_list.insertMiddle(1, 15)
    print('LinkedList Insert Middle(1, 15) :', m_list)  # [1,5,15,6]

    m_list.insertFirst(100)
    print('LinkedList Insert First(100) : ', m_list)    # [100,1,5,15,6]
    print('LinkedList SelectNode(0) :', m_list.selectNode(0))   # 100 (list[0])

    m_list.deleteNode(0)
    print('LinkedList Delete Node(0) : ', m_list)   # [1,5,15,6]
    m_list.deleteNode(1)
    print('LinkedList Delete Node(1) : ', m_list)   # [1,15,6]
