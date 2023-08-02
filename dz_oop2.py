class Student:
    def __init__(self, name, surname, male):
        self.name = name
        self.surname = surname
        self.male = male
        self.finished_courses = []
        self.courses_in_progress = [] 
        self.courses_attached = [] 
        self.grades = {}
        self.avarage_grades = 0

    def rate_lecture(self, lecturer, course, grade):
            if (isinstance(lecturer, Lecturer) 
                and course in self.courses_in_progress and course in lecturer.courses_attached):
                if course in lecturer.grades:
                   lecturer.grades[course] += [grade] 
                   lecturer.avarage_grade()
                else:
                   lecturer.grades[course] = [grade]  
                   lecturer.avarage_grade()
            else:
                return print( 'Ошибка' )
            
    def avarage_grade(self):
        total_sum = 0
        total_count = 0
        for course, grade in self.grades.items():
            total_sum += sum(grade)  
            total_count += len(grade) 
        self.avarage_grades = round(total_sum / total_count, 1)

    def __lt__(self,other):
        if not isinstance(other, Student):
            return print('Not a Student!')
        return self.avarage_grades < other.avarage_grades
    
    def __str__(self):
        res = (f'Имя: {self.name}\nФамилия: {self.surname}\nПол: {self.male}\n'
               f'Средняя оценка за домашние задания: {self.avarage_grades}\n'
               f'Курсы в процессе изучения: { ",".join(self.courses_in_progress)}\n'
               f'Завершенные курсы: {",".join(self.finished_courses)}')
        return res
    

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}'
        return res


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_hw(self, student, course, grade):
        if (isinstance(student, Student) and course in self.courses_attached 
            and course in student.courses_in_progress):
            if course in student.grades:
                student.grades[course] += [grade]
                student.avarage_grade()
            else:
                student.grades[course] = [grade]
                student.avarage_grade()
        else:
            return print( 'Ошибка' )
        
    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}'
        return res


class Lecturer(Mentor):    
    def __init__(self, name, surname):     
        super().__init__(name, surname)
        self.grades = {}   
        self.avarage_grades = int

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка: {self.avarage_grades}'
        return res
        
    
    def avarage_grade(self):
        total_sum = 0
        total_count = 0
        for course, grade in self.grades.items():
            total_sum += sum(grade)
            total_count += len(grade)
        self.avarage_grades = round(total_sum / total_count, 1)

    def __lt__(self,other):
        if not isinstance(other, Lecturer):
            return print('Not a Lecturer!')
        return self.avarage_grades < other.avarage_grades

def avg_lecturer_course_grade(lecturers, course):
    avg_lect_cour_gr, count = 0, 0
    for lecturer in lecturers:
        if not isinstance(lecturer, Lecturer):
            return 'Есть не лектор'
    for lecturer in lecturers:
        if course in lecturer.grades.keys():
            count += 1
            t_sum = 0
            t_count = 0
            for c, g in lecturer.grades.items():
                if c == course:
                    t_sum += sum(g)
                    t_count += len(g)
            avg_lect_cour_gr += t_sum / t_count

    return round(avg_lect_cour_gr / count, 1)



def avg_student_course_grade(students, course):
    avg_stud_cour_gr, count = 0, 0
    for student in students:
        if not isinstance(student, Student):
            return 'В списке есть не студент'
    for student in students:
        if course in student.grades.keys():
            count += 1
            t_sum = 0
            t_count = 0
            for c,g in student.grades.items():
                if c == course:
                    t_sum += sum(g)
                    t_count += len(g)
            avg_stud_cour_gr += t_sum / t_count
    return round(avg_stud_cour_gr / count, 1)




student1 = Student('Mary', 'Smith', 'female')
student1.courses_in_progress += ['Git' , 'Python']
student1.finished_courses += ['Введение в программирование']
student2 = Student('Jim', 'Carry', 'male')
student2.courses_in_progress += ['Git' , 'Python']
student2.finished_courses += ['Введение в программирование']

reviewer1 = Reviewer('Mary','Jane')
reviewer1.courses_attached += ['Python']
reviewer2 = Reviewer('John', 'Seena')
reviewer2.courses_attached += ['Git']


lecturer1 = Lecturer('Donald', 'Duck')
lecturer1.courses_attached += ['Python', 'Git']
lecturer2 = Lecturer('Gomer','Simpson')
lecturer2.courses_attached += ['Python', 'Git']

reviewer1.rate_hw(student1,'Python', 10)
reviewer1.rate_hw(student1,'Python', 7)
reviewer1.rate_hw(student1,'Python', 3)
reviewer1.rate_hw(student2,'Python', 9)
reviewer1.rate_hw(student2,'Python', 4)
reviewer1.rate_hw(student2,'Python', 5)

reviewer2.rate_hw(student1,'Git', 10)
reviewer2.rate_hw(student1,'Git', 7)
reviewer2.rate_hw(student1,'Git', 3)
reviewer2.rate_hw(student1,'Git', 10)
reviewer2.rate_hw(student1,'Git', 9)
reviewer2.rate_hw(student1,'Git', 2)

student1.rate_lecture(lecturer1, 'Python', 10)
student1.rate_lecture(lecturer1, 'Python', 9)
student1.rate_lecture(lecturer1, 'Python', 4)
student1.rate_lecture(lecturer1, 'Git', 10)
student1.rate_lecture(lecturer1, 'Git', 3)
student1.rate_lecture(lecturer1, 'Git', 1)

student2.rate_lecture(lecturer2, 'Python', 10)
student2.rate_lecture(lecturer2, 'Python', 9)
student2.rate_lecture(lecturer2, 'Python', 4)
student2.rate_lecture(lecturer2, 'Git', 10)
student2.rate_lecture(lecturer2, 'Git', 7)
student2.rate_lecture(lecturer2, 'Git', 1)

print(f'Первый студент:\n{student1}\n')
print(f'Второй студент:\n{student2}\n')

print(f'Первый проверяющий:\n{reviewer1}\n')
print(f'Второй проверяющий:\n{reviewer2}\n')

print(f'Первый лектор:\n{lecturer1}\n')
print(f'Второй лектор:\n{lecturer2}\n')

print(f'Средняя оценка первого студента выше, чем у второго?'
      f'\nОтвет: {student1 > student2}\n')
print(f'Средняя оценка первого лектора выше, чем у второго?'
      f'\nОтвет: {lecturer1 > lecturer2}\n')

print(f'Средняя оценка студентов по курсу Python: '
      f'{avg_student_course_grade([student1, student2], "Python")}')
print(f'Средняя оценка студентов по курсу Git: '
      f'{avg_student_course_grade([student1,student2],"Git")}')

print(f'Средняя оценка лекторов по курсу Python: ' 
      f'{avg_lecturer_course_grade([lecturer1,lecturer2], "Python")}')
print(f'Средняя оценка лекторов по курсу Git: '
      f'{avg_lecturer_course_grade([lecturer1, lecturer2], "Git")}')

