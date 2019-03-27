from copy import deepcopy
from math import ceil
from random import shuffle

from src.classes import Class, ClassLesson, Lesson, Teacher


def compose(class_list, teacher_list):
    for current_class in class_list:
        for tmp_teacher in teacher_list:
            tmp_teacher.backup_schedule_save()
        while not compose_class(current_class):
            current_class.backup_lessons()
            for tmp_teacher in teacher_list:
                tmp_teacher.backup_schedule_load()



def compose_class(current_class):
    for tmp in range(current_class.get_number_of_days()):
        current_class.get_schedule().append([])
        for tmp2 in range(calculate_number_of_lessons_per_day(current_class)):
            best_lesson = compose_lesson(current_class)
            if best_lesson is not None:
                current_class.get_schedule()[-1].append(best_lesson)
                best_lesson.dec_number_per_week()
                best_lesson.get_teacher().get_schedule()[len(current_class.get_schedule())-1][len(current_class.get_schedule()[-1])-1] = [current_class, best_lesson.get_lesson()]
    if current_class.calculate_number_of_lesson():
        return False
    else:
        return True


def calculate_number_of_lessons_per_day(current_class):
    if not current_class.get_number_of_days() - len(current_class.get_schedule()):
        return current_class.get_number_of_days()
    else:
        return ceil(current_class.get_number_of_days()/(current_class.get_number_of_days()-len(current_class.get_schedule())))


def compose_lesson(current_class):
    lesson_list = []
    iterable = current_class.get_lesson_list()
    shuffle(iterable)
    for lesson in iterable:
        if lesson in current_class.get_schedule()[-1] or not lesson.get_number_per_week():
            continue
        while len(current_class.get_schedule()) > len(lesson.get_teacher().get_schedule()):
            lesson.get_teacher().get_schedule().append([])
        while len(current_class.get_schedule()[-1])+1 > len(lesson.get_teacher().get_schedule()[len(current_class.get_schedule())-1]):
            lesson.get_teacher().get_schedule()[len(current_class.get_schedule())-1].append([])
        if lesson.get_teacher().get_schedule()[len(current_class.get_schedule())-1][len(current_class.get_schedule()[-1])]:
            continue
        lesson_list.append(lesson)
    tmp = 0
    best_lesson = None
    for lesson in lesson_list:
        if lesson.get_number_per_week() > tmp:
            tmp = lesson.get_number_per_week()
            best_lesson = lesson
    return best_lesson


if __name__ == '__main__':
    print('TEST...')
    math = Lesson("Mathematics")
    rus = Lesson("Russian")
    tea1 = Teacher("Nina", [math])
    tea2 = Teacher("Boris", [rus])
    teacher_list = [tea1, tea2]
    class1 = Class("1A", [ClassLesson(math, 5, tea1), ClassLesson(rus, 5, tea2)], 5)
    class2 = Class("1B", [ClassLesson(math, 5, tea1), ClassLesson(rus, 5, tea2)], 5)
    class_list = [class1, class2]
    compose(class_list, teacher_list)
    print(class1.get_schedule())
    print(class2.get_schedule())
