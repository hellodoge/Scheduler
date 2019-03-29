import sys
from copy import copy

from PyQt5 import QtWidgets

from src.backend import compose
from src.resultWriter import save

from src.design import design_main, design_lesson, design_teacher, design_class, design_author, design_config
from src.classes import Container, Lesson, ClassLesson, Teacher, Class
from src.config import Configuration

container = Container()


class MainWindow(QtWidgets.QMainWindow, design_main.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushLesson.clicked.connect(self.lesson_edit)
        self.pushTeacher.clicked.connect(self.teacher_edit)
        self.pushClass.clicked.connect(self.class_edit)
        self.pushSchedule.clicked.connect(self.produce)
        self.pushAuthor.clicked.connect(self.show_autor)
        self.pushConfig.clicked.connect(self.configure)

    def lesson_edit(self):
        DialogLesson().exec()

    def teacher_edit(self):
        DialogTeacher().exec()

    def class_edit(self):
        DialogClass().exec()

    def show_autor(self):
        DialogAuthor().exec()

    def configure(self):
        DialogConfig().exec()

    def produce(self):
        compose(container.get_classes(), container.get_teachers())
        save(QtWidgets.QFileDialog.getExistingDirectory(self, "Выберите папку"),container.get_classes(),container.get_teachers())


class DialogLesson(QtWidgets.QDialog, design_lesson.Ui_DialogLesson):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushAdd.clicked.connect(self.add_lesson)
        self.pushRemove.clicked.connect(self.remove_lesson)
        self.print_list_lesson()

    def print_list_lesson(self):
        self.listView.clear()
        for tmp in container.get_lessons():
            self.listView.addItem(tmp.get_name())

    def add_lesson(self):
        if not self.lineEdit.text() in [tmp.get_name() for tmp in container.get_lessons()]:
            container.get_lessons().append(Lesson(self.lineEdit.text()))
            self.print_list_lesson()
        self.lineEdit.clear()

    def remove_lesson(self):
        if self.listView.currentItem() is not None:
            del container.get_lessons()[self.listView.currentIndex().row()]
            self.lineEdit.clear()
            self.print_list_lesson()


class DialogTeacher(QtWidgets.QDialog,design_teacher.Ui_DialogTeacher):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.print_list_lesson()
        self.print_list_teacher()
        self.pushAdd.clicked.connect(self.add_teacher)
        self.pushRemove.clicked.connect(self.remove_teacher)

    def print_list_lesson(self):
        for tmp in container.get_lessons():
            self.comboBox.addItem(tmp.get_name())

    def print_list_teacher(self):
        self.listView.clear()
        for tmp in container.get_teachers():
            self.listView.addItem(f'{tmp.get_name()}: {"; ".join([tmp2.get_name() for tmp2 in tmp.get_lesson_list()])}')

    def add_teacher(self):
        if self.comboBox.currentText() is None: return
        if not self.lineEdit.text():
            if self.listView.currentItem() is None: return
            tmp_teacher = container.get_teachers()[self.listView.currentIndex().row()]
            if self.comboBox.currentText() not in [tmp.get_name() for tmp in tmp_teacher.get_lesson_list()]:
                tmp_teacher.get_lesson_list().append(container.get_lessons()[self.comboBox.currentIndex()])
        elif self.lineEdit.text() not in [tmp.get_name() for tmp in container.get_teachers()]:
            container.get_teachers().append(Teacher(self.lineEdit.text(), [container.get_lessons()[self.comboBox.currentIndex()]]))
        else:
            tmp_teacher = list(filter(lambda tmp: tmp.get_name() == self.lineEdit.text(), container.get_teachers()))[0]
            if self.comboBox.currentText() not in [tmp.get_name() for tmp in tmp_teacher.get_lesson_list()]:
                tmp_teacher.get_lesson_list().append(container.get_lessons()[self.comboBox.currentIndex()])
        self.lineEdit.clear()
        self.print_list_teacher()

    def remove_teacher(self):
        if self.listView.currentItem() is not None:
            del container.get_teachers()[self.listView.currentIndex().row()]
            self.print_list_teacher()


class DialogClass(QtWidgets.QDialog,design_class.Ui_DialogClass):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.update_teacher()
        self.update_lesson()
        self.update_import()
        self.update_delete()
        self.pushOk.clicked.connect(self.add_lesson)
        self.comboTeacher.currentIndexChanged.connect(self.update_lesson)
        self.pushImport.clicked.connect(self.import_class)
        self.pushSave.clicked.connect(self.save_class)
        self.pushDelete.clicked.connect(self.delete_class)
        self.lessons = []

    def print_lesson(self):
        self.listView.clear()
        for tmp in self.lessons:
            self.listView.addItem(f'{tmp.get_lesson().get_name()}    Учитель: {tmp.get_teacher().get_name()} Количество: {str(tmp.get_number_per_week())}')

    def add_lesson(self):
        if not self.comboTeacher.currentText(): return
        if self.comboLesson.currentText() in [tmp.get_lesson().get_name() for tmp in self.lessons]:
            self.lessons.remove(list(filter(lambda tmp: tmp.get_lesson().get_name() == self.comboLesson.currentText(), self.lessons))[0])
        if not self.spinLesson.value(): return
        self.lessons.append(ClassLesson(list(filter(lambda tmp: tmp.get_name() == self.comboLesson.currentText(), container.get_lessons()))[0], self.spinLesson.value(), container.get_teachers()[self.comboTeacher.currentIndex()]))
        self.print_lesson()

    def update_teacher(self):
        self.comboTeacher.clear()
        for tmp in container.get_teachers():
            self.comboTeacher.addItem(tmp.get_name())

    def update_lesson(self):
        self.comboLesson.clear()
        if self.comboTeacher.currentText():
            for tmp in container.get_teachers()[self.comboTeacher.currentIndex()].get_lesson_list():
                self.comboLesson.addItem(tmp.get_name())

    def update_import(self):
        self.comboImport.clear()
        for tmp in container.get_classes():
            self.comboImport.addItem(tmp.get_name())

    def import_class(self):
        if self.comboImport.currentText():
            for tmp in container.get_classes()[self.comboImport.currentIndex()].get_lesson_list():
                self.lessons.append(copy(tmp))
            self.print_lesson()

    def save_class(self):
        if not (len(self.lessons) and self.nameEdit.text() and self.spinDays.value()):
            return
        container.get_classes().append(Class(self.nameEdit.text(), copy(self.lessons), self.spinDays.value(), self.checkShift.checkState()))
        self.lessons.clear()
        self.print_lesson()
        self.update_import()
        self.update_delete()
        self.nameEdit.clear()

    def update_delete(self):
        self.comboDelete.clear()
        for tmp in container.get_classes():
            self.comboDelete.addItem(tmp.get_name())

    def delete_class(self):
        if not self.comboDelete.currentText(): return
        del container.get_classes()[self.comboDelete.currentIndex()]
        self.update_import()
        self.update_delete()


class DialogConfig(QtWidgets.QDialog,design_config.Ui_DialogConfig):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushSave.clicked.connect(self.save_config)
        self.spinLesson.setValue(Configuration.number_of_lessons_before_second_shift)

    def save_config(self):
        if self.spinLesson.value():
            Configuration.number_of_lessons_before_second_shift = self.spinLesson.value()
            self.close()


class DialogAuthor(QtWidgets.QDialog,design_author.Ui_DialogAuthor):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()
