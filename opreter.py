class Num :
    def __init__(self, num):
        self.num = num
    def __add__(self,u):
        return self.num + u.num
a=int(input("Enter a :"))
b=int(input("Enter b :"))
num1=Num(a)
num2=Num(b)

ans=num1 + num2
print(ans)