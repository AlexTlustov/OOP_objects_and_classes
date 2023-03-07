class Student:
    def __init__(self, name, surname, gender) -> None:
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
    def __str__(self) -> str:
        res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задание: {sum(self.average_rate()) / len(self.average_rate())}\nКурсы в процессе изучения: {", ".join(self.courses_in_progress)}\nЗавершенные курсы: {", ".join(self.finished_courses)}'
        return res
# Получаем оценки объекта 
    def average_rate(self):
        lst = []
        for value in self.grades.values():
            lst.extend(value)
        return lst 
    def add_courses(self, course_name):
        self.finished_courses.append(course_name)
# Сравниниваем и считаем среднюю оценку    
    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Это нельзя сравнивать!')
            return
        else:
            one_objects = sum(self.average_rate()) / len(self.average_rate()) 
            two_objects = sum(other.average_rate()) / len(other.average_rate()) 
            return one_objects < two_objects
# Задание 2 "Студент дает оценку лектору"
    def rate_st(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.finished_courses:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'  
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname 
        self.courses_attached = []       
# Задание 1 "Создаем класс Лекторы (родит. Ментор)"
class Lecturer(Mentor):
    def __init__(self, name, surname):
        self.grades = {}
        self.courses_attached = [] 
        super().__init__(name, surname)
# Сравниниваем и считаем среднюю оценку        
    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Это нельзя сравнивать!')
            return
        else:
            one_objects = sum(self.average_rate()) / len(self.average_rate()) 
            two_objects = sum(other.average_rate()) / len(other.average_rate()) 
            return one_objects < two_objects
# Получаем оценки объекта 
    def average_rate(self):
        lst = []
        for value in self.grades.values():
            lst.extend(value)
        return lst
    def __str__(self) -> str:
        res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {sum(self.average_rate()) / len(self.average_rate())}'
        return res
# Задание 1 "Создаем класс Эксперты (родит. Ментор)"
class Reviewer(Mentor):
    def __str__(self) -> str:
        res = f'Имя: {self.name}\nФамилия: {self.surname}'
        return res
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

# Добавление объектов класса
some_student = Student('Ruoy', 'Eman', 'Man')
any_student = Student('Josh', 'Stone', 'Man')
some_lecturer = Lecturer('Some', 'Buddy')
any_lecturer = Lecturer('Any', 'Way')
some_reviewer = Reviewer('Some', 'Buddy')
any_reviewer = Reviewer('Any', 'Rev')

# Параметры атрибутов Лектора
some_lecturer.courses_attached += ['Python', 'Git', 'Введение в программирование']
any_lecturer.courses_attached += ['Python', 'Git', 'Введение в программирование']

# Параметры атрибутов Студента
some_student.finished_courses += ['Введение в программирование']
any_student.finished_courses += ['Введение в программирование']
some_student.courses_in_progress += ['Python', 'Git']
any_student.courses_in_progress += ['Python', 'Git']
some_student.rate_st(some_lecturer, 'Введение в программирование', 10)
some_student.rate_st(some_lecturer, 'Введение в программирование', 10)
some_student.rate_st(some_lecturer, 'Введение в программирование', 10)
some_student.rate_st(some_lecturer, 'Введение в программирование', 9.5)
some_student.rate_st(some_lecturer, 'Введение в программирование', 10)
some_student.rate_st(any_lecturer, 'Введение в программирование', 9)
some_student.rate_st(any_lecturer, 'Введение в программирование', 9)
some_student.rate_st(any_lecturer, 'Введение в программирование', 9)
some_student.rate_st(any_lecturer, 'Введение в программирование', 9.5)
some_student.rate_st(any_lecturer, 'Введение в программирование', 9)

# Параметры атрибутов Эксперта
some_reviewer.courses_attached += ['Python']
any_reviewer.courses_attached += ['Python']
some_reviewer.rate_hw(some_student, 'Python', 10)
some_reviewer.rate_hw(some_student, 'Python', 10)
some_reviewer.rate_hw(some_student, 'Python', 10)
some_reviewer.rate_hw(some_student, 'Python', 10)
some_reviewer.rate_hw(some_student, 'Python', 9.5)
some_reviewer.rate_hw(any_student, 'Python', 9)
some_reviewer.rate_hw(any_student, 'Python', 8)
some_reviewer.rate_hw(any_student, 'Python', 7)
some_reviewer.rate_hw(any_student, 'Python', 6)
some_reviewer.rate_hw(any_student, 'Python', 9.5)

# Задание 3 "Добавили маг. метод __str__ и выводим информацию об объекте класса"
print('---------------------------- Задание 3 -------------------------------------')
print(some_reviewer)
print()
print(some_lecturer)
print()
print(some_student)
print()

# Задание 3 часть 2 "Добавили маг. метод __lt__ для сравнения оценок"
print('---------------------------- Задание 3 Часть 2 -------------------------------------')
print(some_student > any_student)
print(some_student < any_student)
print()

# Задание 4 Подсчет средней оценки за домашние задания по всем
def avg_grade_students(students, courses):
    all_grades_in_course = []
    for student in students:
        if courses in student.courses_in_progress:
            all_grades_in_course.extend(student.grades[courses])
    avg_grade = round(sum(all_grades_in_course) / len(all_grades_in_course), 1)
    return avg_grade

def avg_grade_lectors(lectors, courses):
    all_grades_in_course = []
    for lector in lectors:
        if courses in lector.courses_attached:
            all_grades_in_course.extend(lector.grades[courses])
    avg_grade = round(sum(all_grades_in_course) / len(all_grades_in_course), 1)
    return avg_grade

print('---------------------------- Задание 4 -------------------------------------')
students = [some_student, any_student]
print(f"Средняя оценка студентов по всему курсу: {avg_grade_students(students, 'Python')}")
lectors = [some_lecturer, any_lecturer]
print(f"Средняя оценка лекторов по всему курсу: {avg_grade_lectors(lectors, 'Введение в программирование')}")






# f'{cool_lecturer.name} {cool_lecturer.surname}: {" ".join("{0} {1}".format(key, val) for key, val in cool_lecturer.grades.items())}')
