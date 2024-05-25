class Task1:
    def fun(self,n):
        if n%2!=0:
            print("Weird")
        else:
            if n>=2 and n<=5:
                print("Not Weird")
            if n>=6 and n<=20:
                print("Weird")
            if n>20:
                print("Not Weird")
obj=Task1()
obj.fun(int(input()))