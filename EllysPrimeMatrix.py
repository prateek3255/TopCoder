class EllysPrimesMatrix:
    def getCount(self,s):
        cz=self.everyRowContainsZero(s)
        l=list(s)
        x=s[len(s)-1]
        if not cz:
            x=x.replace("2","")
            x=x.replace("5","")
        z=str(x)
        for i in x:
            if int(i)%2==0 and i!="2":
                z=z.replace(i,"")
        l[len(l)-1]=z
        count=0


    def everyRowContainsZero(self,s):
        for i in range(len(s)-1):
            if "0" not in s[i]:
                return False
        return True

    def Prime(n):
        if n & 1 == 0:
            return True
        d = 3
        while d * d <= n:
            if n % d == 0:
                return True
            d = d + 2
        return False

g=EllysPrimesMatrix()
g.getCount(("120","450","289"))
