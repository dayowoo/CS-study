'''
- 싱글톤 패턴 : https://wikidocs.net/69361
'''


# 객체 생성과 초기화
class Foo(object):
    def __new__(cls, *args, **kwargs):
        print("__new__ is called\n")
        instance = super().__new__(cls)
        return instance

    def __init__(self):
        print("__init__ is called\n")


s = Foo()
print(s)


# 싱글톤 패턴
class Singleton(object):
    """
    하나의 싱글톤 인스턴스를 생성
    이미 생성된 인스턴스가 있다면 재사용
    """
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, "_instance"):         # Foo 클래스 객체에 _instance 속성이 없다면
            print("__new__ is called\n")
            cls._instance = super().__new__(cls)  # Foo 클래스의 객체를 생성하고 Foo._instance로 바인딩
        return cls._instance                      # Foo._instance를 리턴

    def __init__(self, data):
        cls = type(self)
        if not hasattr(cls, "_init"):             # Foo 클래스 객체에 _init 속성이 없다면
            print("__init__ is called\n")
            self.data = data
            cls._init = True


s1 = Singleton(3)
s2 = Singleton(4)
print(s1.data)
print(s2.data)