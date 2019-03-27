from copy import deepcopy


class Container:
    def __init__(self):
        self.__class_list = []
        self.__teacher_list = []
        self.__lessons = []

    def get_teachers(self):
        return self.__teacher_list

    def get_classes(self):
        return self.__class_list

    def get_lessons(self):
        return self.__lessons

class Class:
    def __init__(self, name, lesson_list, number_of_days):
        self.__schedule = []
        self.__name = name
        self.__lesson_list = lesson_list
        self.__number_of_days = number_of_days

    def calculate_number_of_lesson(self):
        tmp = 0
        for lesson in self.__lesson_list:
            tmp += lesson.get_number_per_week()
        return tmp

    def get_schedule(self):
        return self.__schedule

    def clear_schedule(self):
        self.__schedule.clear()

    def get_number_of_days(self):
        return self.__number_of_days

    def get_lesson_list(self):
        return self.__lesson_list

    def get_name(self):
        return self.__name

    def __repr__(self):
        return f'Class {self.__name}'

    def backup_lessons(self):
        for tmp in self.__lesson_list:
            tmp.backup()


class Teacher:
    def __init__(self, name, lesson_list):
        self.__schedule = []
        self.__name = name
        self.__lesson_list = lesson_list
        self.__schedule_backup = []

    def get_schedule(self):
        return self.__schedule

    def get_lesson_list(self):
        return self.__lesson_list

    def get_name(self):
        return self.__name

    def backup_schedule_save(self):
        self.__schedule_backup = deepcopy(self.__schedule)

    def backup_schedule_load(self):
        self.__schedule = deepcopy(self.__schedule_backup)

    def __repr__(self):
        return f'{self.__name}'


class Lesson:
    def __init__(self, name):
        self.__name = name

    def get_name(self):
        return self.__name


class ClassLesson:
    def __init__(self, lesson, number_per_week, teacher):
        self.__lesson = lesson
        self.__number_per_week = number_per_week
        self.__teacher = teacher
        self.__number_per_week_backup = self.__number_per_week

    def get_number_per_week(self):
        return self.__number_per_week

    def dec_number_per_week(self):
        self.__number_per_week -= 1

    def get_teacher(self):
        return self.__teacher

    def get_lesson(self):
        return self.__lesson

    def backup(self):
        self.__number_per_week = self.__number_per_week_backup

    def __repr__(self):
        return f'{self.__lesson.get_name()}'
