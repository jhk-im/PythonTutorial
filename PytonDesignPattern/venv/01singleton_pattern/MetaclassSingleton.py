class MetaclassSingleton(type):
    _instance = {}
    def __call__(cls,*args,**kwargs):
        if cls not in cls._instance:
            cls._instance[cls] = super(MetaclassSingleton, cls).__call__(*args,*kwargs)
        return cls._instance[cls]

class TestMetaclass(metaclass=MetaclassSingleton):
    pass

class SecondMetaclass(metaclass=MetaclassSingleton):
    pass

t = TestMetaclass()
t1 = TestMetaclass()
print(t) # <__main__.TestMetaclass object at 0x037FB100>
print(t1) # <__main__.TestMetaclass object at 0x037FB100>

t2 = SecondMetaclass()
t3 = SecondMetaclass()
print(t2) # <__main__.SecondMetaclass object at 0x037FB310>
print(t3) # <__main__.SecondMetaclass object at 0x037FB310>
print(MetaclassSingleton._instance)
