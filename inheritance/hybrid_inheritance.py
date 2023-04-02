class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self):
        print(f"{self.name} says hi!")

class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

    def study(self):
        print(f"{self.name} is studying.")

class Teacher(Person):
    def __init__(self, name, age, teacher_id):
        super().__init__(name, age)
        self.teacher_id = teacher_id

    def teach(self):
        print(f"{self.name} is teaching.")

class TeachingAssistant(Student, Teacher):
    def __init__(self, name, age, student_id, teacher_id):
        Student.__init__(self, name, age, student_id)
        Teacher.__init__(self, name, age, teacher_id)

    def assist(self):
        print(f"{self.name} is assisting the teacher.")

my_student = Student("Subhash", 22, "S001")
my_teacher = Teacher("Ms. Shrma", 40, "T001")
my_ta = TeachingAssistant("Ashish", 5, "S002", "T002")
my_student.speak()
my_teacher.speak()
my_ta.speak()
my_student.study()
my_teacher.teach()
my_ta.assist()
