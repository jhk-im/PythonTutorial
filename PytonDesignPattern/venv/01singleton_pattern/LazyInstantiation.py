class LazyInstantiation:
    _instance = None
    def __init__(self):
        if not LazyInstantiation._instance:
            print('__init__ method called but nothing is created')
        else:
            print('instance already created:', self.getInstance())

    @classmethod
    def getInstance(cls):
        if not cls._instance:
            cls._instance = LazyInstantiation()
        return cls._instance

# __init__ method called but nothing is created
s = LazyInstantiation()
print(s._instance) # None
# __init__ method called but nothing is created
s1 = LazyInstantiation.getInstance()
s2 = LazyInstantiation.getInstance()
print('s와 s1은 서로 같은 인스턴스인가? -> ',s==s1) # True
print('s1 : ',s1._instance) # <__main__.LazyInstantiation object at 0x03A6B340>
print('s2 : ',s2._instance) # <__main__.LazyInstantiation object at 0x03A6B340>

s3 = LazyInstantiation() # instance already created: <__main__.LazyInstantiation object at 0x03A6B340>
print('s3 : ',s3._instance) #  <__main__.LazyInstantiation object at 0x03A6B340>