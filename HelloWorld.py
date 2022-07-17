print("Task 1")
print("Eroom Nedyah")
print("---")
print("Task 2")
print("My favorite number is 22")
for number in range(1, (22 ** 2 + 1)):
    print(number)
print("---")
print("Task 3")

class Engineers:
    skill = 'Problem Solver'

    def __init__(self, name, type, Years_of_Experience):
        self.name = name
        self.type = type
        self.Years_of_Experience = Years_of_Experience

    def employee(self):
        return '{}'.format(self.name)

    def employee(self):
        return '{}'.format(self.type)

    def employee(self):
        return '{}'.format(Years_of_Experience)

p1 = Engineers('Bob Skye', 'Mechanical', 4)
p2 = Engineers('John Doe', 'Civil', 2)

print ('---')

print ('Engineer 1')
print('Name:', p1.name)
print('Engineering Discipline:', p1.type)
print('Skill:', p1.skill)
print('Years of Experience:', p1.Years_of_Experience)

print ('---')

print ('Engineer 2')
print('Name:', p2.name)
print('Engineering Discipline:', p2.type)
print('Skill:', p2.skill)
print('Years of Experience:', p2.Years_of_Experience)

print ('---')

#Left out the fixed class attribute step from previous Github Upload