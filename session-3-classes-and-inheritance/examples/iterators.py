# Shell 
for element in [1, 2, 3]:
    print(element)

class NumberCounter:
    def __init__(self, num):
        self.max = num
    
    def __iter__(self):
        self.count = 0
        return self
    
    def __next__(self):
        self.count = self.count + 1
        if self.count <= self.max:
            return self.count
        else:
            raise StopIteration

count9 = NumberCounter(9)
	  
for elem in count9:
	print(elem)'

#Extra: Generators
def countGen(max):
    for i in range(1, max+1):
        yield i

#Generator Expressions
count20 = (x for x in range(1, 20))