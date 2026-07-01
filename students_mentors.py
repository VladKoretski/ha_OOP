class Student:
    """Класс студента с оценками за ДЗ и возможностью оценивать лекторов."""

    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def add_courses(self, course_name):
        """Добавляет завершённый курс."""
        self.finished_courses.append(course_name)

    def rate_lecture(self, lecturer, course, grade):
        """
        Оценивает лектора по курсу (только если лектор прикреплён к курсу
        и студент изучает этот курс).
        """
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if grade < 1 or grade > 10:
                return 'Ошибка: оценка не соответствует 10-балльной системе'
            else:
                if course in lecturer.grades:
                    lecturer.grades[course] += [grade]
                else:
                    lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def average_grade(self):
        """Средняя оценка студента за все домашние задания."""
        if len(self.grades) == 0:
            return 0
        grades_of_student = []
        for course in self.grades:
            grades_of_student.extend(self.grades[course])
        if grades_of_student:
            return sum(grades_of_student) / len(grades_of_student)
        return 0

    def __eq__(self, other):
        if not isinstance(other, Student):
            return NotImplemented
        return self.average_grade() == other.average_grade()

    def __lt__(self, other):
        if not isinstance(other, Student):
            return NotImplemented
        return self.average_grade() < other.average_grade()

    def __gt__(self, other):
        if not isinstance(other, Student):
            return NotImplemented
        return self.average_grade() > other.average_grade()

    def __str__(self):
        return (f'Имя: {self.name}\nФамилия: {self.surname}\n'
                f'Средняя оценка за домашние задания: {self.average_grade()}\n'
                f'Курсы в процессе изучения: {", ".join(self.courses_in_progress)}\n'
                f'Завершенные курсы: {", ".join(self.finished_courses)}')


class Mentor:
    """Базовый класс для наставников (лекторов и проверяющих)."""

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    """Лектор, получает оценки от студентов."""

    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def average_grade(self):
        """Средняя оценка лектора за все лекции."""
        if len(self.grades) == 0:
            return 0
        grades_of_lecturer = []
        for course in self.grades:
            grades_of_lecturer.extend(self.grades[course])
        if grades_of_lecturer:
            return sum(grades_of_lecturer) / len(grades_of_lecturer)
        return 0

    def __eq__(self, other):
        if not isinstance(other, Lecturer):
            return NotImplemented
        return self.average_grade() == other.average_grade()

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            return NotImplemented
        return self.average_grade() < other.average_grade()

    def __gt__(self, other):
        if not isinstance(other, Lecturer):
            return NotImplemented
        return self.average_grade() > other.average_grade()

    def __str__(self):
        return (f'Имя: {self.name}\nФамилия: {self.surname}\n'
                f'Средняя оценка за лекции: {self.average_grade()}')


class Reviewer(Mentor):
    """Проверяющий (эксперт), выставляет оценки студентам за ДЗ."""

    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_hw(self, student, course, grade):
        """
        Выставляет оценку студенту за курс (только если проверяющий
        прикреплён к этому курсу и студент его изучает).
        """
        if grade < 1 or grade > 10:
                return 'Ошибка: оценка не соответствует 10-балльной системе'
        else:        
            if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
                if course in student.grades:
                    student.grades[course] += [grade]
                else:
                    student.grades[course] = [grade]
            else:
                return 'Ошибка - это не студент или курса нет'

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}'


# ---------- Функции для подсчёта средних (задание №4) ----------
def avg_student_grade(students, course):
    """Средняя оценка за ДЗ по всем студентам на указанном курсе."""
    total, count = 0, 0
    for student in students:
        if course in student.grades:
            total += sum(student.grades[course])
            count += len(student.grades[course])
    return total / count if count else 0


def avg_lecturer_grade(lecturers, course):
    """Средняя оценка за лекции всех лекторов по указанному курсу."""
    total, count = 0, 0
    for lecturer in lecturers:
        if course in lecturer.grades:
            total += sum(lecturer.grades[course])
            count += len(lecturer.grades[course])
    return total / count if count else 0


# ---------- Создание экземпляров и тесты (задание №4) ----------
# Студенты
student1 = Student('Алёхина', 'Ольга', 'Ж')
student2 = Student('Иванов', 'Егор', 'М')
student1.courses_in_progress += ['Python', 'Java']
student1.finished_courses += ['C++']
student2.courses_in_progress += ['Python', 'Java']

# Лекторы
lecturer1 = Lecturer('Иван', 'Иванов')
lecturer2 = Lecturer('Петр', 'Петровский')
lecturer3 = Lecturer('Ганс', 'Клитке')
for lec in (lecturer1, lecturer2, lecturer3):
    lec.courses_attached += ['Python', 'C++', 'Java']

# Проверяющие
reviewer1 = Reviewer('Пётр', 'Петров')
reviewer2 = Reviewer('Анна', 'Смирнова')
for rev in (reviewer1, reviewer2):
    rev.courses_attached += ['Python', 'C++', 'Java']

# Выставление оценок за ДЗ (только проверяющие)
reviewer1.rate_hw(student1, 'Python', 4)
reviewer1.rate_hw(student1, 'Python', 5)
reviewer1.rate_hw(student1, 'Java', 3)

reviewer2.rate_hw(student2, 'Python', 5)
reviewer2.rate_hw(student2, 'Python', 5)
reviewer2.rate_hw(student2, 'Java', 3)

# Оценки лекторам от студентов
print(student1.rate_lecture(lecturer1, 'Python', 7))   # None
print(student1.rate_lecture(lecturer1, 'Java', 8))     # Ошибка (студент не изучает Java)
print(student1.rate_lecture(lecturer1, 'С++', 8))      # Ошибка (нет такого курса)

student1.rate_lecture(lecturer1, 'Python', 4)
student1.rate_lecture(lecturer2, 'Python', 7)
student1.rate_lecture(lecturer2, 'Python', 9)
student2.rate_lecture(lecturer3, 'Python', 7)
student2.rate_lecture(lecturer3, 'Python', 4)

# Вывод информации
print('\n')
print(reviewer1, '\n')
print(lecturer1, '\n')
print(student1, '\n')

# Сравнения
print(lecturer1 > lecturer2)          # False (4+7 vs 7+9)
print(lecturer2 == lecturer3)         # False (8 vs 5.5)
print(student1 < student2)            # True (4.0 vs 4.33)
print(student1 == student2)           # False

# Проверка функций подсчёта средних
students_list = [student1, student2]
lecturers_list = [lecturer1, lecturer2, lecturer3]
print('\nСредняя оценка студентов по Python:', avg_student_grade(students_list, 'Python'))
print('Средняя оценка лекторов по Python:', avg_lecturer_grade(lecturers_list, 'Python'))
