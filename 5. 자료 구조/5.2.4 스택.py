'''
- 스택 : 가장 마지막으로 들어간 데이터가 가장 첫 번째로 나오는 성질을 가진 자료 구조
'''

# Stack - init :  python은 빈 리스트로 스택을 흉내 냄. / 빈 리스트를 만들어서 초기화
stack = []

# Stack - push : 스택에 원소를 넣을 때에는 append를 통해 맨 마지막에 원소를 넣는다.
stack = [1, 2, 3]
stack.append(4)

# Stack - pop : 스택에서 원소를 제거할 땐 pop()을 통해 맨 마지막 원소를 제거해준다. 제거한 원소를 return 받을 수 있다.
top = stack.pop()   # 4 / stack = [1,2,3]

# Stack - top : 스택에서 원소를 제거하지 않고 가져오기만 할 땐 [-1]을 이용한다.
top = stack[-1]     # 3



class Stack:
    # 스택 객체 생성
    def __init__(self):
        self.items = []

    # 스택 요소 추가 push(.append())    
    def push(self, item):
        self.items.append(item)

    # 스택 요소 삭제 pop
    def pop(self):
        return self.items.pop()

    # 스택 맨 앞 요소 리턴
    def peek(self):
        return self.items[0]

    # 스택이 비었는지 확인 (비었으면 True return)
    def isEmpty(self):
        return not self.items
        

stk = Stack()        # stack 객체 생성
print(stk)           # stack object 생성 확인
print(stk.isEmpty()) # 처음에는 아무것도 들어있지 않으므로 True 출력
stk.push(1)          # stk 에 1 넣음 : [1]
stk.push(2)          # stk 에 2 넣음 : [1,2]
print(stk.items)     #  [1,2]
print(stk.pop())     # stk 에 2가 꺼내지면서 출력 : 2 / [1]
print(stk.peek())    # stk 맨 앞 값 출력 : 1
print(stk.isEmpty()) # 비어있지 않으므로 False 출력
print(stk.pop())     # stk 에 1가 꺼내지면서 출력 : 1 / []
print(stk.isEmpty()) # 객체에 아무것도 들어있지 않으므로 True 출력