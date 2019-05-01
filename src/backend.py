from copy import copy
from math import ceil
from random import shuffle
from src.config import Configuration

from src.classes import Class, LessonOfClass, Lesson, Teacher


def compose(class_list, teacher_list):
    for current_class in class_list:
        for tmp_teacher in teacher_list:
            tmp_teacher.backup_schedule_save()
        attempt_counter = 0
        while not compose_class(current_class):
            attempt_counter += 1
            if attempt_counter > Configuration.max_attempts_of_scheduling_for_class:
                raise RuntimeError
            current_class.backup_lessons()
            current_class.clear_schedule()
            for tmp_teacher in teacher_list:
                tmp_teacher.backup_schedule_load()


def compose_class(current_class):
    for tmp in range(current_class.get_number_of_days()):
        current_class.get_schedule().append([])
        if current_class.is_second_shift():
            current_class.get_schedule()[-1] = [None]*Configuration.number_of_lessons_before_second_shift
        for tmp2 in range(calculate_number_of_lessons_per_day(current_class)):
            best_lesson = compose_lesson(current_class)
            if best_lesson is not None:
                current_class.get_schedule()[-1].append(best_lesson)
                best_lesson.dec_number_per_week()
                best_lesson.get_teacher().get_schedule()[len(current_class.get_schedule())-1][len(current_class.get_schedule()[-1])-1] = [current_class, best_lesson.get_lesson()]
    return False if current_class.calculate_number_of_lesson() else True


def calculate_number_of_lessons_per_day(current_class):
    if not current_class.get_number_of_days() - len(current_class.get_schedule()):
        return current_class.calculate_number_of_lesson()
    else:
        return ceil(current_class.calculate_number_of_lesson()/(current_class.get_number_of_days()-len(current_class.get_schedule())))


def compose_lesson(current_class):
    lesson_list = []
    iterable = copy(current_class.get_lesson_list())
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
    return choose_best_lesson(lesson_list)


def choose_best_lesson(lesson_list):
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
    ph = Lesson("Physics")
    tea1 = Teacher("Nina", [math])
    tea2 = Teacher("Boris", [rus])
    tea3 = Teacher("Zheka", [ph])
    teacher_list = [tea1, tea2, tea3]
    class1 = Class("1A", [LessonOfClass(math, 5, tea1), LessonOfClass(rus, 5, tea2), LessonOfClass(ph, 5, tea3)], 5)
    class2 = Class("1B", [LessonOfClass(math, 5, tea1), LessonOfClass(rus, 5, tea2), LessonOfClass(ph, 5, tea3)], 5)
    class_list = [class1, class2]
    compose(class_list, teacher_list)
    print(class1.get_schedule())
    print(class2.get_schedule())
