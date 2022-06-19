class Node:
    def __init__(self, item):
        self.item = item
        self.left = None
        self.right = None

# BinaryTree 만들기
class BinaryTree():
    def __init__(self):
        self.root = None

     # 트리 높이
    def height(self, root):
        if root == None:
            return 0
        return max(self.height(root.left), self.height(root.right)) + 1
    
    # 전위 순회
    '''
    1. 자기 자신 출력
    2. 왼쪽 서브 트리 호출
    3. 오른쪽 서브 트리 호출
    ex) 10 > 20 > 40 > 80 > 50 > 30 > 60 > 70 
    '''
    def preorder(self, n):
        if n!=None:
            print(n.item, '', end='')   # 노드 방문
            if n.left:
                self.preorder(n.left) # 왼쪽 서브트리 순회
            if n.right:
                self.preorder(n.right) # 오른쪽 서브트리 순회
    
    # 후위 순회
    '''
    1. 왼쪽 서브 트리 호출
    2. 오른쪽 서브 트리 호출
    3. 자기 자신 출력
    ex) 80 > 40 > 50 > 20 > 60 > 70 > 30 > 10
    '''
    def postorder(self, n):
        if n != None:
            if n.left:
                self.postorder(n.left)
            if n.right:
                self.postorder(n.right)
            print(n.item, '', end='') # 노드 방문
    
    # 중위 순회
    '''
    * 자기 자신 출력이 중간에 있음.
    1. 왼쪽 서브 트리 호출
    2. 자기 자신 출력
    3. 오른쪽 서브 트리 호출
    ex) 80 > 40 > 20 > 50 > 10 > 60 > 30 > 70
    '''
    def inorder(self, n):
        if n != None:
            if n.left:
                self.inorder(n.left)
            print(n.item, '', end='') # 노드 방문
            if n.right:
                self.inorder(n.right)

    # 레벨 순회
    '''
    깊이(레벨) 단위로 출력 - 깊이가 낮은 순서대로 > 선입선출 구조인 큐로 구현
    ex) 10 > 20 > 30 > 40 > 50 > 60 > 70 > 80
    '''
    def levelorder(self, n):
        q = []
        q.append(n)
        while q:
            t = q.pop(0)
            print(t.item, '', end='')
            if t.left != None:
                q.append(t.left)
            if t.right != None:
                q.append(t.right)

# 노드 엮기
tree = BinaryTree()
n1 = Node(10)
n2 = Node(20)
n3 = Node(30)
n4 = Node(40)
n5 = Node(50)
n6 = Node(60)
n7 = Node(70)
n8 = Node(80)

tree.root = n1
n1.left = n2
n1.right = n3
n2.left = n4
n2.right = n5
n3.left = n6
n3.right = n7
n4.left = n8

print('트리 높이 : ', tree.height(tree.root))

# 전위 순회: 10 20 40 80 50 30 60 70
print('전위 순회: ', end='')
tree.preorder(tree.root)
print()

# 후위 순회: 80 40 50 20 60 70 30 10 
print('후위 순회 : ', end='')
tree.postorder(tree.root)
print()

# 중위 순회: 80 40 20 50 10 60 30 70
print('중위 순회 : ', end='')
tree.inorder(tree.root)
print()

# 레벨 순회: 10 20 30 40 50 60 70 80
print('레벨 순회 : ', end='')
tree.levelorder(tree.root)
print()
