class SubstitutionCode:
    def getValue(self,key,code):
        s=""
        value=lambda x: 0 if x==9 else x+1
        for i in code:
            if i in key:
                s+=str(value(key.index(i)))
        return s

s=SubstitutionCode()
print(s.getValue("TRADINGFEW","LGXWEV"))