# ООП: наследование, инкапсуляция и полиморфизм
## Автор

Выполнил Корецкий В.П. в рамках обучения на платформе Netology.
Домашнее задание по теме «Объектно-ориентированное программирование» в рамках курса.  
Реализована модель учебной группы, включающая студентов, лекторов и проверяющих (экспертов), с возможностью выставления оценок, расчёта средних баллов и сравнения по успеваемости.

## Требования
- Python 3.6 или выше (используются f-строки и аннотации типов не обязательны).

## Python Code
[Ссылка на Python](Code{https://github.com/VladKoretski/ha_OOP/blob/main/students_mentors.py)

## Установка и запуск
1. Склонируйте репозиторий:
   ```bash
   git clone https://github.com/your-username/homework-oop.git
   ```
2. Перейдите в каталог проекта:
   ```bash
   cd homework-oop
   ```
3. Запустите скрипт:
   ```bash
   python main.py
   ```

## Структура классов

### `Mentor` (родительский класс)
- Атрибуты: `name`, `surname`, `courses_attached` (список курсов, к которым прикреплён наставник).

### `Lecturer` (наследует `Mentor`)
- Дополнительный атрибут: `grades` – словарь, где ключ – название курса, значение – список оценок от студентов.
- Методы:
  - `average_grade()` – средняя оценка за все лекции.
  - Переопределены `__str__`, `__eq__`, `__lt__`, `__gt__` для сравнения лекторов по средней оценке.

### `Reviewer` (наследует `Mentor`)
- Метод `rate_hw(student, course, grade)` – выставляет оценку студенту за курс (только если проверяющий прикреплён к этому курсу и студент его изучает).
- Переопределён `__str__` для вывода имени и фамилии.

### `Student`
- Атрибуты: `name`, `surname`, `gender`, `finished_courses`, `courses_in_progress`, `grades` (оценки за ДЗ).
- Методы:
  - `add_courses(course_name)` – добавляет завершённый курс.
  - `rate_lecture(lecturer, course, grade)` – оценивает лектора по курсу (только если лектор прикреплён к курсу и студент его изучает).
  - `average_grade()` – средняя оценка за все домашние задания.
  - Переопределены `__str__`, `__eq__`, `__lt__`, `__gt__` для сравнения студентов по средней оценке.

### Вспомогательные функции (задание №4)
- `avg_student_grade(students, course)` – средняя оценка за ДЗ по всем студентам на указанном курсе.
- `avg_lecturer_grade(lecturers, course)` – средняя оценка за лекции всех лекторов по указанному курсу.

## Пример использования

```python
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
```
Результаты вывод:
```bash
None
None
Ошибка


Имя: Пётр
Фамилия: Петров 

Имя: Иван
Фамилия: Иванов
Средняя оценка за лекции: 6.333333333333333 

Имя: Алёхина
Фамилия: Ольга
Средняя оценка за домашние задания: 4.0
Курсы в процессе изучения: Python, Java
Завершенные курсы: C++ 

False
False
True
False

Средняя оценка студентов по Python: 4.75
Средняя оценка лекторов по Python: 6.333333333333333
```
---

Лицензия: MIT
