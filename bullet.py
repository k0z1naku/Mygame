from math import *

import pygame
from image import *
from constants import *
from general import *

class Bullet:
    def __init__(self, coords, angle, path):
        """
        Создание пули. Надо указать координаты стреляющего корабля, его скорость, путь до картинки с пулей, экран для рисования
        Атрибуты:
        __image - объект класса Image, создаваемый на основе BULLETIMG
        __coords - координаты пули (в начале совпадают с координатами корабля)
        __spd - скорость пули (высчитывается, как скорость относительно корабля + скорость корабля)
        __heatrad - радиус, на котором пуля видна
        __is_dead - уничтожена ли пуля
        """
        self.__image = Image(path)
        self.__coords = coords
        self.__spd1 = ed_vec(angle)*BULLET_SPD
        self.__spd2 = ed_vec(angle) * ROCKET_SPD
        self.__heatrad = self.__image.get_image().get_width() // 2 * SCALE * 1
        self.__is_dead = False
        self.last = pygame.time.get_ticks()
        self.__is_dead = False

     def movebullet(self, SCALE):
        """Перемещение пули за TIME_PERIOD
        При каждом вызове пуля сразу отрисовывается с помощь метода класса Image
        """

        self.__coords += self.__spd1 * TIME_PERIOD
        self.__image.draw(0, self.__coords, SCALE / 2)

    def moverocket(self, SCALE):
        new_rocket_spd = self.__spd2
        new_rocket_spd[1] -= 15
        self.__coords += new_rocket_spd * TIME_PERIOD
        self.__image.draw(0, self.__coords, SCALE / 2)


    def get_coord(self):
        """Получить координаты пули """
        return self.__coords

    def get_heatrad(self):
        """Получить 'радиус видимости' пули  """
        return self.__heatrad

    def get_dead(self):
        """Узнать, уничтожена ли пуля """
        return self.__is_dead

    def set_dead(self, bool_var):
        """Изменить статус пули """
        self.__is_dead = bool_var
