import sys
import csv
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QMainWindow
from all_classes import Ui_MainWindow_livingroom, Ui_MainWindow_bathroom, Ui_MainWindow_hallway,\
    Ui_MainWindow_calculations, Ui_MainWindow_calculations_floor, Ui_MainWindow_calculations2,\
    Ui_MainWindow_calculations3, Ui_MainWindow_jar, Ui_MainWindow_calculations_wall, Ui_MainWindow_calculations_list_3,\
    Ui_MainWindow_calculations_list_2, Ui_MainWindow_choose_type_kle, Ui_MainWindow_calculations_germe,\
    Ui_MainWindow_calculations_lak, Ui_MainWindow_calculations_lami, Ui_MainWindow_calculations_park,\
    Ui_MainWindow_calculations_tile_floor, Ui_MainWindow_calculations_tile_wall, Ui_MainWindow_pravila


def open_csv(name):
    with open(f'tables/{name}.csv', encoding="utf8") as csvfile:
        reader = csv.reader(csvfile, delimiter=';', quotechar='"')
        d = {}
        for el in reader:
            d[el[0]] = float(el[1].replace(',', '.'))
        return d


def open_csv_2(name):
    with open(f'tables/{name}.csv') as csvfile:
        reader = csv.reader(csvfile, delimiter=';', quotechar='"')
        d = {}
        for el in reader:
            d[el[0]] = float(el[1].replace(',', '.'))
        return d


class Hallway(QMainWindow, Ui_MainWindow_hallway):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle('Коридор')
        self.btn_livingroom.clicked.connect(self.run_livingroom)
        self.btn_bathroom.clicked.connect(self.run_bathroom)
        self.btn_pravila.clicked.connect(self.run_pravila)

    def run_livingroom(self):
        self.hide()
        room_l.show()

    def run_bathroom(self):
        self.hide()
        room_b.show()

    def run_pravila(self):
        prav.show()


class Bathroom(QMainWindow, Ui_MainWindow_bathroom):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle('Ванная')
        for i in range(1, 15):
            eval(f"self.btn_wall_{i}.clicked.connect(self.run_calculations_wall)")
        self.btn_return.clicked.connect(self.back)
        pixmap = QPixmap('images/strelka.png')
        self.label_return.setPixmap(pixmap)
        self.label_return.setScaledContents(True)

    def run_calculations_wall(self):
        cal_wall.show()

    def back(self):
        self.hide()
        h.show()


class Livingroom(QMainWindow, Ui_MainWindow_livingroom):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle('Гостиная')
        pixmap = QPixmap('images/strelka.png')
        self.label_return.setPixmap(pixmap)
        self.label_return.setScaledContents(True)
        for el in range(1, 9):
            eval(f"self.btn_wall_{el}.clicked.connect(self.run_calculations)")
        for el in range(1, 4):
            eval(f"self.btn_jar_{el}.clicked.connect(self.run_calculations_jar)")
        for el in range(1, 12):
            eval(f"self.btn_floor_{el}.clicked.connect(self.run_calculations_floor)")
        self.btn_return.clicked.connect(self.back)

    def run_calculations(self):
        cal.show()

    def run_calculations_jar(self):
        cal_jar.show()

    def run_calculations_floor(self):
        cal_floor.show()

    def back(self):
        self.hide()
        h.show()


class Calculation(QMainWindow, Ui_MainWindow_calculations):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle('Расчёты для стен')
        self.names = ['ale', 'color_sme', 'emal', 'grun', 'kle', 'pob', 'shpa', 'shtu']
        self.btn_ale.setStyleSheet('border-image: url("images/ale.png");')
        self.btn_color_sme.setStyleSheet('border-image: url("images/color_sme.png");')
        self.btn_emal.setStyleSheet('border-image: url("images/emal.png");')
        self.btn_grun.setStyleSheet('border-image: url("images/grun.png");')
        self.btn_kle.setStyleSheet('border-image: url("images/kle.png");')
        self.btn_pob.setStyleSheet('border-image: url("images/pob.png");')
        self.btn_shpa.setStyleSheet('border-image: url("images/shpa.png");')
        self.btn_shtu.setStyleSheet('border-image: url("images/shtu.png");')
        for el in self.names:
            eval(f'self.btn_{el}.clicked.connect(self.calculations)')

    def calculations(self):
        if self.sender() == self.btn_pob:
            cal_2.name = 'pob'
            cal_2.area_inp.setText("")
            cal_2.width_inp.setText("")
            cal_2.result_label.setText('')
            cal_2.result.setText('Результат, кг')
            cal_2.show()
        elif self.sender() == self.btn_shpa:
            cal_2.name = 'shpa'
            cal_2.area_inp.setText("")
            cal_2.width_inp.setText("")
            cal_2.result_label.setText('')
            cal_2.result.setText('Результат, кг')
            cal_2.show()
        elif self.sender() == self.btn_ale:
            cal_3.name = 'ale'
            cal_3.area_inp.setText("")
            cal_3.width_inp.setText("")
            cal_3.layers_inp.setText("")
            cal_3.result_label.setText("")
            cal_3.result.setText('Результат, кг')
            cal_3.show()
        elif self.sender() == self.btn_color_sme:
            cal_3.name = 'color_sme'
            cal_3.area_inp.setText("")
            cal_3.width_inp.setText("")
            cal_3.layers_inp.setText("")
            cal_3.result_label.setText("")
            cal_3.result.setText('Результат, кг')
            cal_3.show()
        elif self.sender() == self.btn_grun:
            cal_list_3.name = 'grun'
            cal_list_3.area_inp.setText("")
            cal_list_3.width_inp.setText("")
            cal_list_3.layers_inp.setText("")
            cal_list_3.result_label.setText("")
            cal_list_3.data = open_csv('грунтовка')
            cal_list_3.result.setText('Результат, л')
            cal_list_3.spisok.clear()
            for el in cal_list_3.data.keys():
                cal_list_3.spisok.addItem(el)
            cal_list_3.show()
        elif self.sender() == self.btn_shtu:
            cal_list_3.name = 'shtu'
            cal_list_3.area_inp.setText("")
            cal_list_3.width_inp.setText("")
            cal_list_3.layers_inp.setText("")
            cal_list_3.result_label.setText("")
            cal_list_3.data = open_csv_2('штукатурка')
            cal_list_3.result.setText('Результат, кг')
            cal_list_3.spisok.clear()
            for el in cal_list_3.data.keys():
                cal_list_3.spisok.addItem(el)
            cal_list_3.show()
        elif self.sender() == self.btn_emal:
            cal_list_3.name = 'emal'
            cal_list_3.area_inp.setText("")
            cal_list_3.width_inp.setText("")
            cal_list_3.layers_inp.setText("")
            cal_list_3.result_label.setText("")
            cal_list_3.data = open_csv('эмаль')
            cal_list_3.result.setText('Результат, кг')
            cal_list_3.spisok.clear()
            for el in cal_list_3.data.keys():
                cal_list_3.spisok.addItem(el)
            cal_list_3.show()
        elif self.sender() == self.btn_kle:
            choose_kle.show()


class CalculationsFloor(QMainWindow, Ui_MainWindow_calculations_floor):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle('Расчёты для пола')
        self.btn_gydro.setStyleSheet('border-image: url("images/gydro.png");')
        self.btn_kle_3.setStyleSheet('border-image: url("images/kle_3.png");')
        self.btn_lami.setStyleSheet('border-image: url("images/lami.png");')
        self.btn_naliv.setStyleSheet('border-image: url("images/naliv.png");')
        self.btn_ochi.setStyleSheet('border-image: url("images/ochi.png");')
        self.btn_park.setStyleSheet('border-image: url("images/park.png");')
        self.btn_praim.setStyleSheet('border-image: url("images/praim.png");')
        self.btn_sta.setStyleSheet('border-image: url("images/sta.png");')
        for el in ['gydro', 'kle_3', 'lami', 'naliv', 'ochi', 'park', 'praim', 'sta']:
            eval(f'self.btn_{el}.clicked.connect(self.calculations)')

    def calculations(self):
        if self.sender() == self.btn_kle_3:
            cal_2.name = 'kle_3'
            cal_2.area_inp.setText("")
            cal_2.width_inp.setText("")
            cal_2.result_label.setText('')
            cal_2.result.setText('Результат, кг')
            cal_2.show()
        elif self.sender() == self.btn_naliv:
            cal_2.name = 'naliv'
            cal_2.area_inp.setText("")
            cal_2.width_inp.setText("")
            cal_2.result_label.setText('')
            cal_2.result.setText('Результат, кг')
            cal_2.show()
        elif self.sender() == self.btn_praim:
            cal_3.name = 'praim'
            cal_3.area_inp.setText("")
            cal_3.width_inp.setText("")
            cal_3.layers_inp.setText("")
            cal_3.result_label.setText("")
            cal_3.result.setText('Результат, л')
            cal_3.show()
        elif self.sender() == self.btn_gydro:
            cal_3.name = 'gydro'
            cal_3.area_inp.setText("")
            cal_3.width_inp.setText("")
            cal_3.layers_inp.setText("")
            cal_3.result_label.setText("")
            cal_3.result.setText('Результат, л')
            cal_3.show()
        elif self.sender() == self.btn_ochi:
            cal_3.name = 'ochi'
            cal_3.area_inp.setText("")
            cal_3.width_inp.setText("")
            cal_3.layers_inp.setText("")
            cal_3.result_label.setText("")
            cal_3.result.setText('Результат, л')
            cal_3.show()
        elif self.sender() == self.btn_sta:
            cal_list_2.name = 'sta'
            cal_list_2.area_inp.setText("")
            cal_list_2.width_inp.setText("")
            cal_list_2.result_label.setText("")
            cal_list_2.spisok.clear()
            cal_list_2.result.setText('Результат, кг')
            cal_list_2.data = open_csv_2('стяжка пола')
            for el in cal_list_2.data.keys():
                cal_list_2.spisok.addItem(el)
            cal_list_2.show()
        elif self.sender() == self.btn_lami:
            cal_3.name = 'lami'
            cal_lami.area_inp.setText("")
            cal_lami.width_inp.setText("")
            cal_lami.layers_inp.setText("")
            cal_lami.metr_inp.setText("")
            cal_lami.result_label.setText("")
            cal_lami.result.setText('Результат, штук')
            cal_lami.show()
        elif self.sender() == self.btn_park:
            cal_park.name = 'park'
            cal_park.result.setText('Результат, штук')
            cal_park.area_inp.setText("")
            cal_park.width_inp.setText("")
            cal_park.result_label.setText('')
            cal_park.show()


class CalculationsJar(QMainWindow, Ui_MainWindow_jar):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle('Расчёты прочего')
        self.btn_propit.setStyleSheet('border-image: url("images/propit.png");')
        self.btn_lak.setStyleSheet('border-image: url("images/lak.png");')
        self.btn_kle_2.setStyleSheet('border-image: url("images/kle_2.png");')
        self.btn_germe.setStyleSheet('border-image: url("images/germe.png");')
        self.btn_remso.setStyleSheet('border-image: url("images/remso.png");')
        self.btn_cont.setStyleSheet('border-image: url("images/cont.png");')
        for el in ['propit', 'lak', 'kle_2', 'germe', 'remso', 'cont']:
            eval(f'self.btn_{el}.clicked.connect(self.calculations)')

    def calculations(self):
        if self.sender() == self.btn_kle_2:
            cal_2.name = 'kle_2'
            cal_2.result.setText('Результат, кг')
            cal_2.area_inp.setText("")
            cal_2.width_inp.setText("")
            cal_2.result_label.setText('')
            cal_2.show()
        if self.sender() == self.btn_remso:
            cal_2.result.setText('Результат, кг')
            cal_2.name = 'remso'
            cal_2.area_inp.setText("")
            cal_2.width_inp.setText("")
            cal_2.result_label.setText('')
            cal_2.show()
        elif self.sender() == self.btn_cont:
            cal_2.result.setText('Результат, л')
            cal_2.name = 'cont'
            cal_2.area_inp.setText("")
            cal_2.width_inp.setText("")
            cal_2.result_label.setText('')
            cal_2.show()
        elif self.sender() == self.btn_propit:
            cal_3.result.setText('Результат, л')
            cal_3.name = 'propit'
            cal_3.area_inp.setText("")
            cal_3.width_inp.setText("")
            cal_3.layers_inp.setText("")
            cal_3.result_label.setText("")
            cal_3.show()
        elif self.sender() == self.btn_germe:
            cal_germe.name = 'germe'
            cal_germe.area_inp.setText("")
            cal_germe.width_inp.setText("")
            cal_germe.result_label.setText("")
            cal_germe.result.setText('Результат, кг')
            cal_germe.show()
        elif self.sender() == self.btn_lak:
            cal_lak.name = 'lak'
            cal_lak.area_inp.setText("")
            cal_lak.width_inp.setText("")
            cal_lak.result_label.setText("")
            cal_lak.spisok.clear()
            cal_lak.result.setText('Результат, л')
            cal_lak.data = open_csv('лак')
            for el in cal_lak.data.keys():
                cal_lak.spisok.addItem(el)
            cal_lak.show()


class CalculationsWall(QMainWindow, Ui_MainWindow_calculations_wall):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle('Расчёты для ванны')
        self.btn_antip.setStyleSheet('border-image: url("images/antip.png");')
        self.btn_mastic.setStyleSheet('border-image: url("images/mastic.png");')
        self.btn_tile_floor.setStyleSheet('border-image: url("images/tile_floor.png");')
        self.btn_tile_wall.setStyleSheet('border-image: url("images/tile_wall.png");')
        for el in ['antip', 'mastic', 'tile_floor', 'tile_wall']:
            eval(f'self.btn_{el}.clicked.connect(self.calculations)')

    def calculations(self):
        if self.sender() == self.btn_antip:
            cal_3.name = 'antip'
            cal_3.result.setText('Результат, л')
            cal_3.area_inp.setText("")
            cal_3.width_inp.setText("")
            cal_3.layers_inp.setText("")
            cal_3.result_label.setText("")
            cal_3.show()
        if self.sender() == self.btn_mastic:
            cal_3.name = 'mastic'
            cal_3.result.setText('Результат, кг')
            cal_3.area_inp.setText("")
            cal_3.width_inp.setText("")
            cal_3.layers_inp.setText("")
            cal_3.result_label.setText("")
            cal_3.show()
        if self.sender() == self.btn_tile_floor:
            cal_tile_floor.result.setText('Результат, штук')
            cal_tile_floor.name = 'tile_floor'
            cal_tile_floor.area_inp.setText("")
            cal_tile_floor.width_inp.setText("")
            cal_tile_floor.result_label.setText('')
            cal_tile_floor.show()
        if self.sender() == self.btn_tile_wall:
            cal_tile_wall.result_2.setText('Результат, штук')
            cal_tile_wall.name = 'tile_wall'
            cal_tile_wall.area_inp_2.setText("")
            cal_tile_wall.width_inp_2.setText("0")
            cal_tile_wall.layers_inp.setText("")
            cal_tile_wall.result_label_2.setText('')
            cal_tile_wall.show()


class Calculations2(QMainWindow, Ui_MainWindow_calculations2):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle('Расчёты')
        self.name = ''
        self.calculate.clicked.connect(self.raschitat)

    def raschitat(self):
        if self.name == 'pob':
            self.result_label.setText(format(float(self.area_inp.text()) * float(self.width_inp.text()) * 0.25, '.3f'))
        if self.name == 'shpa':
            self.result_label.setText(format(float(self.area_inp.text()) * float(self.width_inp.text()) * 1.2, '.3f'))
        if self.name == 'kle_2':
            self.result_label.setText(format(float(self.area_inp.text()) * float(self.width_inp.text()) * 0.05, '.3f'))
        if self.name == 'remso':
            self.result_label.setText(format(float(self.area_inp.text()) * float(self.width_inp.text()) * 2.04, '.3f'))
        if self.name == 'cont' or self.name == 'kle_3':
            self.result_label.setText(format(float(self.area_inp.text()) * float(self.width_inp.text()) * 0.3, '.3f'))
        if self.name == 'naliv':
            self.result_label.setText(format(float(self.area_inp.text()) * float(self.width_inp.text()) * 1.9, '.3f'))


class Calculations3(QMainWindow, Ui_MainWindow_calculations3):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle('Расчёты')
        self.name = ''
        self.calculate.clicked.connect(self.raschitat)

    def raschitat(self):
        if self.name == 'propit':
            self.result_label.setText(format(float(self.area_inp.text()) * float(self.width_inp.text()) *
                                             float(self.layers_inp.text()) * 0.4, '.3f'))
        elif self.name == 'ale' or self.name == 'color_sme':
            self.result_label.setText(format(float(self.area_inp.text()) * float(self.width_inp.text()) *
                                             float(self.layers_inp.text()) * 1.5, '.3f'))
        elif self.name == 'antip':
            self.result_label.setText(format(float(self.area_inp.text()) * float(self.width_inp.text()) *
                                             float(self.layers_inp.text()) * 0.5, '.3f'))
        elif self.name == 'mastic':
            self.result_label.setText(format(float(self.area_inp.text()) * float(self.width_inp.text()) *
                                             float(self.layers_inp.text()) * 2.5, '.3f'))
        elif self.name == 'praim':
            self.result_label.setText(format(float(self.area_inp.text()) * float(self.width_inp.text()) *
                                             float(self.layers_inp.text()) * 0.25, '.3f'))
        elif self.name == 'mastic':
            self.result_label.setText(format(float(self.area_inp.text()) * float(self.width_inp.text()) *
                                             float(self.layers_inp.text()) * 2.5, '.3f'))
        elif self.name == 'gydro' or self.name == 'ochi':
            self.result_label.setText(format(float(self.area_inp.text()) * float(self.width_inp.text()) *
                                             float(self.layers_inp.text()) * 0.1, '.3f'))


class CalculationsList3(QMainWindow, Ui_MainWindow_calculations_list_3):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle('Расчёты')
        self.name = ''
        self.data = {}
        self.calculate.clicked.connect(self.raschitat)

    def raschitat(self):
        self.result_label.setText(format(float(self.area_inp.text()) * float(self.width_inp.text()) *
                                         float(self.layers_inp.text()) * self.data[self.spisok.currentText()], '.3f'))


class CalculationsList2(QMainWindow, Ui_MainWindow_calculations_list_2):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle('Расчёты')
        self.name = ''
        self.data = {}
        self.calculate.clicked.connect(self.raschitat)

    def raschitat(self):
        self.result_label.setText(format(float(self.area_inp.text()) * float(self.width_inp.text()) *
                                         self.data[self.spisok.currentText()], '.3f'))


class ChooseKLe(QMainWindow, Ui_MainWindow_choose_type_kle):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.fliz.clicked.connect(self.choose)
        self.glass.clicked.connect(self.choose)
        self.paper.clicked.connect(self.choose)
        self.vinil.clicked.connect(self.choose)

    def choose(self):
        cal_list_2.name = 'kle'
        cal_list_2.area_inp.setText("")
        cal_list_2.width_inp.setText("")
        cal_list_2.result_label.setText("")
        cal_list_2.result.setText('Результат, кг')
        cal_list_2.spisok.clear()
        if self.sender() == self.paper:
            cal_list_2.data = open_csv('клей для обоев бумажные')
        elif self.sender() == self.fliz:
            cal_list_2.data = open_csv('клей для обоев флизелиновые')
        elif self.sender() == self.vinil:
            cal_list_2.data = open_csv('клей для обоев виниловые')
        elif self.sender() == self.glass:
            cal_list_2.data = open_csv('клей для обоев стеклообои')
        for el in cal_list_2.data.keys():
            cal_list_2.spisok.addItem(el)
        cal_list_2.show()
        self.hide()


class CalculationsGerme(QMainWindow, Ui_MainWindow_calculations_germe):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle('Расчёты')
        self.name = ''
        self.data = {}
        self.calculate.clicked.connect(self.raschitat)

    def raschitat(self):
        self.result_label.setText(format(float(self.area_inp.text()) * float(self.width_inp.text()) /
                                         1000, '.3f'))


class CalculationsLak(QMainWindow, Ui_MainWindow_calculations_lak):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.name = ''
        self.data = {}
        self.calculate.clicked.connect(self.raschitat)

    def raschitat(self):
        self.result_label.setText(format(float(self.area_inp.text()) * float(self.width_inp.text()) *
                                         self.data[self.spisok.currentText()], '.3f'))


class CalculationsLami(QMainWindow, Ui_MainWindow_calculations_lami):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle('Расчёты')
        self.name = ''
        self.calculate.clicked.connect(self.raschitat)

    def raschitat(self):
        self.result_label.setText(format((float(self.area_inp.text()) - float(self.layers_inp.text())) *
                                         (float(self.width_inp.text()) - float(self.layers_inp.text())) /
                                         float(self.metr_inp.text()), '.3f'))


class CalculationsPark(QMainWindow, Ui_MainWindow_calculations_park):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle('Расчёты')
        self.name = ''
        self.calculate.clicked.connect(self.raschitat)

    def raschitat(self):
        self.result_label.setText(format((float(self.area_inp.text()) + (float(self.area_inp.text()) * 0.05))
                                         / float(self.width_inp.text()), '.3f'))


class CalculationsTileFloor(QMainWindow, Ui_MainWindow_calculations_tile_floor):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle('Расчёты')
        self.name = ''
        self.calculate.clicked.connect(self.raschitat)

    def raschitat(self):
        self.result_label.setText(format(float(self.area_inp.text()) / float(self.width_inp.text()), '.3f'))


class CalculationsTileWall(QMainWindow, Ui_MainWindow_calculations_tile_wall):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.name = ''
        self.calculate_2.clicked.connect(self.raschitat)

    def raschitat(self):
        self.result_label_2.setText(format((float(self.area_inp_2.text()) - float(self.width_inp_2.text()))
                                           / float(self.layers_inp.text()), '.3f'))


class Pravila(QMainWindow, Ui_MainWindow_pravila):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle('Инструкция')


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    h = Hallway()
    room_l = Livingroom()
    cal = Calculation()
    cal_2 = Calculations2()
    cal_3 = Calculations3()
    cal_list_3 = CalculationsList3()
    cal_list_2 = CalculationsList2()
    choose_kle = ChooseKLe()
    cal_jar = CalculationsJar()
    cal_germe = CalculationsGerme()
    cal_lak = CalculationsLak()
    cal_floor = CalculationsFloor()
    room_b = Bathroom()
    cal_wall = CalculationsWall()
    cal_tile_floor = CalculationsTileFloor()
    cal_lami = CalculationsLami()
    cal_park = CalculationsPark()
    cal_tile_wall = CalculationsTileWall()
    prav = Pravila()

    all_names = ['h', 'room_l', 'cal', 'cal_2', 'cal_3', 'cal_list_3', 'cal_list_2', 'choose_kle', 'cal_jar',
                 'cal_germe', 'cal_lak', 'cal_floor', 'room_b', 'cal_wall', 'cal_tile_floor', 'cal_lami',
                 'cal_park', 'cal_tile_wall', 'prav']
    for i in range(19):
        eval(f'{all_names[i]}.setFixedSize({all_names[i]}.size())')

    h.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())
