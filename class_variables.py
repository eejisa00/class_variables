class Student:
	dep= "ECE"
	def __init__(self,name,rollno):
		self.name = name
		self.rollno = rollno
	def change_dep(self,stream):
		self.dep=stream
s1=Student("Ananya","2532")
s2=Student("Lavanya","2533")
s2.change_dep("EEE")
print(Student.dep)
print(s1.dep)
print(s2.dep)
"""print(Student.dep)
print(s2.dep)
s1.department = "CSE"
print(s1.dep)
print(s2.dep)
Student.dep= "CIVIL"
print(Student.dep)"""

