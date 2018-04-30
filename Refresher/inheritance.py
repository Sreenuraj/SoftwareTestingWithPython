class Student:
    def __init__(self, name, school):
        self.name = name
        self.school = school
        self.mark = []

    def average(self):
        return sum(self.mark) / len(self.mark)

    @classmethod
    def friend(cls, origin, friend_name, salary):
        return cls(friend_name, origin.school, salary)


class WorkingStudent(Student):
    def __init__(self, name, school, salary):
        super().__init__(name, school)
        self.salary = salary


ramu = WorkingStudent('Ramu', 'KV', 10)
sreenu = WorkingStudent.friend(ramu, 'Sreenu', 11)
print(ramu.salary)
print(sreenu.name)
print(sreenu.school)
print(sreenu.salary)


