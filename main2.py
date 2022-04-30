class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}


    def rate_lect(self, lecturer, course, grade):
        if isinstance(lecturer,
                    Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'


    def __str__(self):
        grades = []
        for course in self.grades:
            grades.extend(self.grades[course])
        avg_grade = round(sum(grades) / len(grades), 2)

        c_prog = ", ".join(self.courses_in_progress)
        c_fin = ", ".join(self.finished_courses)

        info = f'Имя: {self.name}\n' \
               f'Фамилия: {self.surname}\n' \
               f'Средняя оценка за домашние задания: {avg_grade}\n' \
               f'Курсы в процессе изучения: {c_prog}\n' \
               f'Завершенные курсы: {c_fin}'
        return info


    def __lt__(self, person):
        self_grades = []
        person_grades = []

        for course in self.grades:
            self_grades.extend(self.grades[course])
        for course in person.grades:
            person_grades.extend(person.grades[course])
        avg_self_gr = sum(self_grades) / len(self_grades)
        avg_person_gr = sum(person_grades) / len(person_grades)

        if avg_self_gr > avg_person_gr:
            print(f'Средняя оценка студента {self.name} {self.surname} больше средней оценки студента '
                  f'{person.name} {person.surname}')
        elif avg_self_gr < avg_person_gr:
            print(f'Средняя оценка студента {self.name} {self.surname} меньше средней оценки студента '
                  f'{person.name} {person.surname}')
        else:
            print(f'Средняя оценка студента {self.name} {self.surname} равна средней оценке студента '
                  f'{person.name} {person.surname}')


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def __str__(self):
        grades = []
        for course in self.grades:
            grades.extend(self.grades[course])
        avg_grade = round(sum(grades) / len(grades), 1)

        info = f'Имя: {self.name}\n' \
               f'Фамилия: {self.surname}\n' \
               f'Средняя оценка за лекции: {avg_grade}'
        return info

    def __lt__ (self, person):
        self_grades = []
        person_grades = []

        for course in self.grades:
            self_grades.extend(self.grades[course])
        for course in person.grades:
            person_grades.extend(person.grades[course])
        avg_self_gr = sum(self_grades) / len(self_grades)
        avg_person_gr = sum(person_grades) / len(person_grades)

        if avg_self_gr > avg_person_gr:
            print(f'Средняя оценка лектора {self.name} {self.surname} больше средней оценки лектора '
                   f'{person.name} {person.surname}')
        elif avg_self_gr < avg_person_gr:
            print(f'Средняя оценка лектора {self.name} {self.surname} меньше средней оценки лектора '
                   f'{person.name} {person.surname}')
        else:
            print(f'Средняя оценка лектора {self.name} {self.surname} равна средней оценке лектора '
                   f'{person.name} {person.surname}')


class Reviewer(Mentor):

    def rate_stud(self, student, course, grade):
        if isinstance(student, Student) and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        info = f'Имя: {self.name}\nФамилия: {self.surname}'
        return info


Brad_Pitt = Student('Brad', 'Pitt', 'man')
Kate_Beckinsale = Student('Kate', 'Beckinsale', 'woman')

Brad_Pitt.courses_in_progress += ['Python', 'Git']
Brad_Pitt.finished_courses += ['Введение в программирование', 'SQL', 'C']

Kate_Beckinsale.courses_in_progress += ['Python', 'Git', 'C#']
Kate_Beckinsale.finished_courses += ['Введение в программирование', 'SQL']

Elton_John = Lecturer('Elton', 'John')
Marylin_Manson = Lecturer('Marylin', 'Manson')

Elton_John.courses_attached += ['Python', 'Git']
Marylin_Manson.courses_attached += ['Python', 'Git']

Brad_Pitt.rate_lect(Elton_John, 'Python', 8)
Brad_Pitt.rate_lect(Marylin_Manson, 'Python', 6)
Brad_Pitt.rate_lect(Elton_John, 'Git', 4)
Brad_Pitt.rate_lect(Marylin_Manson, 'Git', 2)

Kate_Beckinsale.rate_lect(Elton_John, 'Python', 7)
Kate_Beckinsale.rate_lect(Marylin_Manson, 'Python', 10)
Kate_Beckinsale.rate_lect(Elton_John, 'Git', 5)
Kate_Beckinsale.rate_lect(Marylin_Manson, 'Git', 5)

Dmitriy_Kiselev = Reviewer('Dmitriy', 'Kiselev')
Alexey_Navalniy = Reviewer('Alexey', 'Navalniy')

Dmitriy_Kiselev.rate_stud(Brad_Pitt, 'Python', 7)
Dmitriy_Kiselev.rate_stud(Kate_Beckinsale, 'Python', 9)
Dmitriy_Kiselev.rate_stud(Brad_Pitt, 'Git', 4)
Dmitriy_Kiselev.rate_stud(Kate_Beckinsale, 'Git', 10)

Alexey_Navalniy.rate_stud(Brad_Pitt, 'Python', 9)
Alexey_Navalniy.rate_stud(Kate_Beckinsale, 'Python', 5)
Alexey_Navalniy.rate_stud(Brad_Pitt, 'Git', 3)
Alexey_Navalniy.rate_stud(Kate_Beckinsale, 'Git', 8)

print(f'{Dmitriy_Kiselev}\n')
print(f'{Alexey_Navalniy}\n')
print(f'{Elton_John}\n')
print(f'{Marylin_Manson}\n')
print(f'{Brad_Pitt}\n')
print(f'{Kate_Beckinsale}\n')

Elton_John.__lt__(Marylin_Manson)
Brad_Pitt.__lt__(Kate_Beckinsale)
print('')

def avg_grade_stud(list, course):
    list_grades = []
    for student in list:
        x = student.grades.setdefault(course)
        for val in x:
            list_grades.append(val)
    if course in student.courses_in_progress:
        avg_grade = round(sum(list_grades) / len(list_grades), 2)
        print(f'По курсу {course} средний балл у студентов - {avg_grade}')
    else:
        print('Ошибка')

student_list = [Brad_Pitt, Kate_Beckinsale]
avg_grade_stud(student_list, 'Python')
avg_grade_stud(student_list, 'Git')
print('')

def avg_grade_lect(list, course):
    list_grades = []
    for lecturer in list:
        x = lecturer.grades.setdefault(course)
        for val in x:
            list_grades.append(val)
    if course in lecturer.courses_attached:
        avg_grade = round(sum(list_grades) / len(list_grades), 2)
        print(f'По курсу {course} средний балл у лекторов - {avg_grade}')
    else:
        print('Ошибка')

lecturer_list = [Elton_John, Marylin_Manson]
avg_grade_lect(lecturer_list, 'Python')
avg_grade_lect(lecturer_list, 'Git')
