#%%
class Person(object):
    def __init__(self, id, name, age):
        self.id = id
        self.name = name
        self.age = age

    def __str__(self):
        return str(self.id) + ' ' + self.name + ' ' + str(self.age)


class student(Person):
    def __init__(self, id, name, age, Class):
        Person.__init__(self, id, name, age)
        self.Class = Class

    def __str__(self):
        return str(self.Class) + ' ' + str(
            self.id) + ' ' + self.name + ' ' + str(self.age)


class grade(student):
    Passed_count = 0
    Unpass_students = []
    Max_student = ''
    Max_grade = 0

    def __init__(self, id, name, age, Class, g1, g2, g3):
        student.__init__(self, id, name, age, Class)
        self.grade1 = g1
        self.grade2 = g2
        self.grade3 = g3
        self.total_grade = g1 + g2 + g3
        if self.total_grade > grade.Max_grade:
            grade.Max_grade = self.total_grade
            grade.Max_student = self.name
        if g1 >= 60 and g2 >= 60 and g3 >= 60:
            # print('通过')
            grade.Passed_count += 1
        else:
            # print('不通过')
            grade.Unpass_students.append(self.name)

    def judge_pass(self):
        if not (self.grade1 >= 60 and self.grade2 >= 60 and self.grade3 >= 60):
            return '不通过'
        else:
            return '通过'

    def mean(self):
        return (self.grade1 + self.grade2 + self.grade3) / 3

    @staticmethod
    def Max():
        print(grade.Max_student, grade.Max_grade)

    def __str__(self):
        return str(self.Class) + ' ' + str(
            self.id) + ' ' + self.name + ' ' + str(
                self.age) + '\n' + self.judge_pass() + ' ' + str(
                    self.grade1) + ' ' + str(self.grade2) + ' ' + str(
                        self.grade3)


# cj = Person(11, 'cj', 20)
# cj = student(11, 'cj', 20, 19052702)
students = []
students.append(grade(10, 'cj1', 20, 19052703, 65, 100, 100))
students.append(grade(11, 'cj2', 20, 19052703, 59, 100, 100))
students.append(grade(12, 'cj3', 20, 19052703, 100, 43, 100))
students.append(grade(13, 'cj4', 20, 19052703, 94, 100, 100))
students.append(grade(14, 'cj5', 20, 19052703, 100, 50, 100))
students.append(grade(15, 'cj6', 20, 19052703, 100, 59, 100))
students.append(grade(16, 'cj7', 20, 19052703, 100, 80, 100))
students.append(grade(17, 'cj8', 20, 19052703, 100, 70, 100))
students.append(grade(18, 'cj9', 20, 19052703, 100, 90, 100))
students.append(grade(19, 'cj10', 20, 19052703, 100, 58, 100))
# students.append([cj1, cj2, cj3, cj4, cj5, cj6, cj7, cj8, cj9, cj10])
# for x in students:
#     print(x)
# print(students[1].judge_pass())
print("挂科名单:", grade.Unpass_students)
print("通过人数:", grade.Passed_count)
grade.Max()
