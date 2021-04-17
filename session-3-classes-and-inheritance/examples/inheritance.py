class Person:
    def __init__(self, first, last):
        print("I am a Person")
        self.firstname = first
        self.lastname = last
    
    def introduce(self): 
        print("Hi! My name is", self.firstname, self.lastname)
    
    def burp(self):
        print("~~burp~~")

    _dna = 'secret dna'

x = Person('Jakob', 'Reinwald')
x.introduce()

class Student(Person):
    def __init__(self, first, last):
        print("I am a Student")
        super().__init__(first, last)

    def introduce(self):
        super().introduce()
        # print("Hi! My name is", self.firstname, self.lastname)
        print("I am a student")
    
    def study(self):
        print("studying~")

class Adult(Person):
    def __init__(self, first, last):
        print("I am an Adult")
        super().__init__(first, last)

class UCLAStudent(Student, Adult):
    def __init__(self, first, last, uid):
        print("I am a UCLA Student")
        super().__init__(first, last)
        self.uid = uid
    
    def study(self):
        print("Studying for the Reinman midterm~")
        super().burp()
        
y = Student("Alex", "Xia")
y.introduce()
y.burp()
y.study()
print(y._dna)

z = UCLAStudent("Einar", "Balan", 123456789)