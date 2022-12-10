# TODO Написать 3 класса с документацией и аннотацией типов
import doctest
class chair:
    def __int__(self, arg1: int, arg2: float):
        """
        Создаем стул

        :param arg1: int принадлежащий [1, 10] - критерий комфортности
        :param arg2: высота стула. Величина больше нуля
        Примеры:
        >>> chair0 = chair(7, 60) #Инициализация экзепляра класса
        """
        self.comfortability = arg1
        self.height = arg2
    def get_more_comfortable(self):
        """
        Усесться поудобнее
        :return: -
        Примеры:
        >>> chair0 = chair(7, 60)
        >>>chair0.get_more_comfortable()
        """
        self.comfortability += 1
    def cut_down_legs(self, scale: float): # scale - положительное число
        """
        Уменьшаем высоту стула
        :param scale: Величина, на которую урежется высота стула, положительное число
        Примеры:
        >>> chair0 = chair(7, 60)
        >>>chair0.cut_down_legs(50)
        >>>chair0.cut_down_legs(150) #На 150 единиц не получится, атрибут высота уменьшится до 0
        """
        if self.height > 0 and (self.height - scale) > 0:
            self.height -= scale
        else:
            self.height = 0
class paper:
    def __int__(self, arg1: str, arg2: str): #arg1 - это цвет бумаги, он может быть любой из набора радуги
        """
        Инициализация экземпляра
        :param arg1: Цвет (red or blue)
        :param arg2: Строка, которую запишем
        :raise TypeError: если неправильно передали цвет
        Примеры:
        >>>paper0 = paper("red", "Hello, world!")
        >>>paper1 = paper("green", "Bye, world") #Неправильный цвет
        """
        if arg1 == 'red' or arg1 == 'blue':
            self.paper_color: int = arg1
        else:
            raise TypeError("Цвет либо red, либо blue")
        self.writing: str = arg2
    def write(self, write: str):
        """
        Записываем на бумагу какой-то str
        :param write: То, что записываем
        Примеры:
        >>>paper0 = paper("red", "Hello, world!")
        >>>paper0.write("Feeling good today")
        """
        self.writing = self.writing + write
    def paint(self, color: str):
        """
        Меняем цвет бумаги, при этом теряя информацию
        :param color: Цвет, в который окрасим бумагу
        Примеры:
        >>>paper0 = paper("red", "Hello, world!")
        >>>paper0.paint("blue")
        """
        self.paper_color = color #self.paper_color - это цвет бумаги, он может быть любой из набора радуги
        self.writing = ""
    def read(self):
        """
        Читаем с бумаги
        :return: то, что было записано в бумаге
        Примеры:
        >>>paper0 = paper("red", "Hello, world!")
        >>>paper0.write("Feeling good today")
        """
        return self.writing
class dogo:
    def __init__(self, arg1: int, arg2: bool):
        """
        Инициализируем экзепляр класса
        :param arg1: настроение собаки по шкале от 1 до 10
        :param arg2: здоровье собаки - либо ей хорошо, либо плохо
        :raise ValueError: если передали настроение собаки не по шкале от 1 до 10
        Примеры:
        >>>dogo0 = dogo(7, True)
        >>>dogo0 = dogo(11, False)
        """
        if arg1 > 0 and arg1 < 11:
            self.mood = arg1 #Настроение по шкале от 1 до 10, недопускаются аргументы, не принадлежащие интервалу
        else:
            raise ValueError("Настроение собаки оценивается по шкале от 1 до 10")
        self.health = arg2 #Здесь, понятное дело, здоровью собаки либо хорошо, либо плохо, поэтому bool
    def pet_dogo(self):
        """
        Гладим собаку, инткрементируя ее настроение
        """
        self.mood += 1
    def brush_dogo(self):
        """
        Вычёсываем собаку, излечивая её от всех недугов
        """
        self.health = True

if __name__ == "__main__":
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    doctest.testmod()
    pass
