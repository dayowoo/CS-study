
# 시간 복잡도
'''
- 시간 복잡도: 문제를 해결하는 데 걸리는 시간과 입력의 함수 관계
'''
# 입력 크키 'n'의 보든 입력에 대한 알고리즘에 필요한 시간이 10n^2 + n 이라면

def example(n):
    # 10n^2
    for i in range(10):
        for j in range(n):
            for k in range(n):
                if True:
                    print(k)
    # +n
    for i in range(n):
        if True:
            print(i)

example(int(input()))
