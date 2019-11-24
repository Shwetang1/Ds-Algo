class A:
    def __init__(self):
        self.x = 0

    def spam(self):
        print('A.spam')


class B(A):
    def __init__(self):
        super().__init__()
        self.y = 1

    def spam(self):
        print('B.spam')
        super().spam()


print(A.__mro__)
print(B.__mro__)
print(B().y)
print(B().x)
print(A().x)
