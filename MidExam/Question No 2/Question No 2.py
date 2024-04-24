print("Question No 2")

class School_system:
    def __init__(self,name,age,id):
        self.name = name
        self.age = age
        self.id = id

class Student(School_system):
    def __init__(self,name,age,id,grade,classes):
        super().__init__(name, age, id)
        self.grade = grade
        self.classes = classes

    def information(self):
        print(f"name : {self.name}")
        print(f"age : {self.age}")
        print(f"id : {self.id}")
        print(f"grade : {self.grade}")
        print(f"classes: {self.classes}")

class Teacher(School_system):
    def __init__(self,name, age, id,subject,classes):
        super().__init__(name, age, id)
        self.subject = subject
        self.classes = classes

    def information(self):
        print(f"name : {self.name}")
        print(f"age : {self.age}")
        print(f"id : {self.id}")
        print(f"subject : {self.subject}")
        print(f"classes : {self.classes}") 
        return self       


class Administration(School_system):
    def __init__(self, name, age, id,department, employee):
        super().__init__(name, age, id)
        self.department = department
        self.employee = employee

    def information(self):
        print(f"name : {self.name}")
        print(f"age : {self.age}")
        print(f"id : {self.id}")
        print(f"department : {self.department}")
        print(f"employee : {self.employee}")


student = Student("Waleed",20,271045628,"A",["Comp", "Physics"])
student.information()

teacher = Teacher("Sir Anique",35,1234,"Programming",["Comp 111"])
teacher.information()

administration = Administration("Ali",40,123,"Admoinistration",["Ahmad", "Usama"])
administration.information()











# write a recursive function reverse(string). it should take value string and return the reversed string. for eample"i like cocomelon" should return as "nolemococ ekil i".