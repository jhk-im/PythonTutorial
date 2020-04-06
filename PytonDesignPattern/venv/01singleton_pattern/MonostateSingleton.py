class MonostateSingleton:
    __shared_state = {'a':'b'}
    def __init__(self):
        self.__dict__ = self.__shared_state

m1 = MonostateSingleton()
m2 = MonostateSingleton()
print(m1) # <__main__.MonostateSingleton object at 0x02C4B0E8>
print(m2) # <__main__.MonostateSingleton object at 0x02C4B118>

m1.a = 1
m2.b = 2
print(m1.__dict__) # {'a': 1, 'b': 2}
print(m2.__dict__) # {'a': 1, 'b': 2}