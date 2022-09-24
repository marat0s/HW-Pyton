class Triangle:
    def __init__(self, a, b, c):
        self.a = float(a)
        self.b = float(b)
        self.c = float(c)

a = int(input("a="))
b = int(input("b="))
c = int(input("c="))

class Count(Triangle):

    def __init__(self,a,b,c):
        super().__init__(a,b,c)

    def get_area(self):
        s = (a + b + c) / 2
        return (s*(s-a)*(s-b)*(s-c)) ** 0.5 
    def get_perimeter(self):
        p = a + b + c
        return p     

t = Count(a,b,c)

print("area: {}".format(t.get_area()))
print("perimeter: {}".format(t.get_perimeter()))
