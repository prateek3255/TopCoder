class SimpleDarts:
    def highestScore(self,f):
        l=[]
        if f>=3:
           for i in range(f,f-3,-1):
               l.append(i)
               l.append(i*2)
               l.append(i*3)

        else:
            for i in range(f, 0, -1):
                l.append(i)
                l.append(i * 2)
                l.append(i * 3)
        l.append(25)
        l.append(50)
        l.sort()
        return (l[len(l)-1]+l[len(l)-2]+l[len(l)-3])
s=SimpleDarts()
s.highestScore(20)

