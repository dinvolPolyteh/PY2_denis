# TODO Написать 3 класса с документацией и аннотацией типов
from typing import Union


class Classical_Particle:
    def __init__(self, coords: list, velocity: list, force: list, charge: Union[float,int], mass: Union[float,int]):
        '''
        Создание объекта Частица
        :param coords: Начальные координаты частицы
        :param velocity: Начальные скорости частиыц
        :param charge: Заряд частицы
        :param mass: Масса частицы
        Пример:
        >>> Particle1 = Classical_Particle([0,0,0], [1,1,1],[0,0,0],1,100)
        '''
        if not isinstance(coords, list):
            raise TypeError("Координаты должны быть типа list")
        self.coords = coords

        if not isinstance(velocity, list):
            raise TypeError("Скорости должны быть типа list")
        if len(velocity) != len(coords):
            raise Exception("Скорости и координаты должны быть одной размерности")
        self.velocity = velocity

        if not isinstance(force, list):
            raise TypeError("Силы должны быть типа list")
        if len(force) != len(coords):
            raise Exception("Силы и координаты должны быть одной размерности")
        self.force = force

        if not isinstance(charge, (int, float)):
            raise TypeError("Заряд должен быть типа int или float")
        self.charge = charge

        if not isinstance(mass, (int, float)):
            raise TypeError("Масса должна быть int или float")
        if mass < 0:
            raise ValueError("Масса не может быть отрицательным числом")
        self.mass = mass

    def is_charged(self) -> bool:
        """
        Функция которая проверяет является ли частица заряженной
        :return: Является ли частица заряженной
        Примеры:
        >>> Particle1 = Classical_Particle([0,0,0], [1,1,1],[0,0,0],1,100)
        >>> Particle1.is_charged()
        """
        ...

    def new_coords(self, time: Union[float,int]):
        """
        Функция находит новые координатые через определенное время
        :param time: прошедшее время для смены координат
        Примеры:
        >>> Particle1 = Classical_Particle([0,0,0], [1,1,1],[0,0,0],1,100)
        >>> Particle1.new_coords(100)
        """
        if not isinstance(time,(int,float)):
            raise TypeError("Время должно быть типа int или float")
        if time < 0:
            raise ValueError("Промежуток времени должен быть положительным")
        ...



class Cat:
    def __init__(self, name: str, age: Union[int,float], tail: str, sex: str):
        """
        Создание объекта кота
        :param name: Имя кота
        :param age: возраст кота
        :param tail: Какой у кота хвост
        :param sex: Пол кота
        Примеры:
        >>> cat1 = Cat("Вася", 11,"up","male")
        >>> cat2 = Cat("Муся", 5,"down","female")
        """
        if not isinstance(name, str):
            raise TypeError("Имя должно быть типа str")
        self.name = name

        if not isinstance(age, (int, float)):
            raise TypeError("Возраст должен быть типа int или float")
        if age < 0:
            raise ValueError("Возраст не может быть отрицательным числом")
        self.age = age

        if not isinstance(tail, str):
            raise TypeError("Хвост должен быть типа str")
        if tail.lower() != "up" and tail.lower() != "down" and tail.lower() != "neutral":
            raise Exception("Хвост может быть только up, down или neutral")

        if not isinstance(sex, str):
            raise TypeError("Хвост должен быть типа str")
        if sex.lower() != "male" and sex.lower() != "female":
            raise Exception("Пол может быть только female или male")
        self.sex = sex

    def getting_older(self, time: Union[int,float]):
        """
        Рассчитывает новый возраст кота
        :param time: Сколько прошло времени
        >>> cat1 = Cat("Вася", 11,"up","male")
        >>> cat1.getting_older(123412)
        """
        if not isinstance(time,(int,float)):
            raise TypeError("Время должно быть типа int или float")
        if time < 0:
            raise ValueError("Промежуток времени должен быть положительным")
        ...

    def get_mood(self) ->str:
        """По хвосту определяет настроение
        :return: возвращает настроение кота
        >>> cat1 = Cat("Вася", 11,"up","male")
        >>> cat1.get_mood()
        """
        ...
    
    def get_human_age(self) -> Union[int,float]:
        """
        Из возраста кота рассчитывает его человеческий возраст
        :return: возвращает возраст кота в человеческих годах
        >>> cat1 = Cat("Вася", 11,"up","male")
        >>> cat1.get_human_age()
        """
        ...
    
    
    
class Chair:
    def __init__(self, material: str, age: Union[int,float], warranty: Union[int,float], legs: int):
        """
        Создание объекта Стул
        :param material: Материал из которого сделан стул
        :param age: Возраст стула
        :param warranty: Гарантийный срок
        :param legs: Количество ножек у стула
        >>> chair1 = Chair("wood", 11,3,124)
        """
        if not isinstance(material, str):
            raise TypeError("Материал должен быть типа str")
        if material.lower() != "wood" and material.lower() != "metal":
            raise Exception("Материал может быть только metal или wood")
        self.material = material

        if not isinstance(age, (int, float)):
            raise TypeError("Возраст должен быть типа int или float")
        if age < 0:
            raise ValueError("Возраст не может быть отрицательным числом")
        self.age = age

        if not isinstance(warranty, (int, float)):
            raise TypeError("Гарантия должна быть типа int или float")
        if warranty < 0:
            raise ValueError("Гарантия не может быть отрицательным числом")
        self.warranty = warranty

        if not isinstance(legs, int):
            raise TypeError("Число ножек должен быть типа int")
        if legs < 0:
            raise ValueError("Чсило ножек не может быть отрицательным числом")
        self.legs = legs

    def does_warranty_work(self) -> bool:
        """
        Функция проверяет из возраста и периода гарантии, работает ли она еще
        :return: Возвращает работает ли гарантия
        >>> chair1 = Chair("wood", 11,3,124)
        >>> chair1.does_warranty_work()
        """
        ...

    def remove_legs(self,num_of_legs):
        """
        Убирает заданное количество ног у стула
        :param num_of_legs: Количество убираемых ножек
        :raise ValueError: Если количество убираемых ног превышает количество существующих.
        >>> chair1 = Chair("wood", 11,3,124)
        >>> chair1.remove_legs(120)
        """
        ...



if __name__ == "__main__":
    import doctest
    doctest.testmod()
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    pass
