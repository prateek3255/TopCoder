class Multifactorial:
    def calcMultiFact(self, n,k):
        if k>=n:
            return str(k)
        else:
            fac=1
            for i in range(n,1,-k):
                if fac>10**18:
                    return "overflow"
                fac=fac*i
            return str(fac)

m=Multifactorial()
print(m.calcMultiFact(2000000000,1))