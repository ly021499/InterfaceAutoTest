

class Sample(object):

    _instance = None

    @classmethod
    def get_driver(cls):
        if not Sample._instance:
            Sample._instance = 'Hello'
        return cls._instance


A = Sample().get_driver()
B = Sample().get_driver()
D = Sample()._instance
print(id(A))
print(id(B))
print(id(D))