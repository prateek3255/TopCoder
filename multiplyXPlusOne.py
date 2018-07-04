class MultiplyXPlusOne:
	def minimalSteps(self,s,t,count=0):
		if s==t:
			return count
		elif s>t:
			return
		else:
			self.minimalSteps(2*s+1,t,count+1)
			self.minimalSteps(3*s+1,t,count+1)
m=MultiplyXPlusOne()
print(m.minimalSteps(1,22))