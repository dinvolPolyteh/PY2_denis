class Clothes:
    """Базовый класс одежды"""
    def __init__(self, material: str, size: str, country: str, puttin_on = 0):
        """
        :param material: Из какого материала сделано 
        :param size: Какой размер S,M,L,XL ...
        :param country: В какой стране произведено
        :param puttin_on: Сколько раз надевали (использовали), по-умолчанию 0
        Материал из которого сделана одежда не изменяется, также как и страну изготовления а размер можно подшить
        """
        self._material = material
        self.size = size
        self._country = country
        self.puttin_on = puttin_on


    @property
    def material(self) -> str:
        return self._material

    @property
    def country(self) -> str:
        return self._country

    @property
    def puttin_on(self) -> int:
        return self._puttin_on

    @puttin_on.setter
    def puttin_on(self, new_put_on: int) -> None:
        if not isinstance(new_put_on, int):
            raise TypeError("Сколько раз надели должно быть типа int")
        if new_put_on < 0:
            raise ValueError("Сколько раз надели не может быть меньше 0")
        self._puttin_on = new_put_on




    def put_on(self) ->list:
        """
        Меняет количество использований на 1, на выход выдает параметры для другого объекта, чтобы надеть его
        """
        pass

    def was_put_on(self) -> int:
        """
        :return Количество использований
        """
        return self.puttin_on

    def __str__(self):
        return f"Сделана из  {self._material}. Страна производства {self._country}. Размер {self.size}"

    def __repr__(self):
        return f"{self.__class__.__name__}(material={self._material!r}, size={self.size!r}, country={self._country!r}, puttin_on={self.puttin_on})"


class T_short(Clothes):
    """Дочерний класс футболка"""
    def __init__(self, material: str, size: str, country: str, sleeves: str, puttin_on = 0, ):
        """
        :param material: Из какого материала сделано
        :param size: Какой размер S,M,L,XL ...
        :param country: В какой стране произведено
        :param sleeves:
        :param puttin_on: Сколько раз надевали (использовали), по-умолчанию 0
        """
        super().__init__(material, size, country,puttin_on)
        self.sleeves = sleeves

    @property
    def sleeves(self) -> str:
        return self._sleeves

    @sleeves.setter
    def sleeves(self,new_sleeves:str) -> None:
        if not isinstance(new_sleeves,str) :
            raise TypeError("Рукава должно быть типа str")
        if new_sleeves.lower() != "short" and new_sleeves.lower() != "long":
            raise ValueError("Рукава могут быть либо long либо short")
        self._sleeves = new_sleeves.lower()

    def put_on(self) ->list:
        """
        Меняет количество использований на 1, на выход выдает параметры для другого объекта, чтобы надеть его. Параметры другие, и не на все части тела можно
        """
        pass
    
    def __repr__(self):
        return f"{self.__class__.__name__}(material={self._material!r}, size={self.size!r}, country={self._country!r},sleeves = {self.sleeves!r}, puttin_on={self.puttin_on})"


if __name__ == "__main__":
    # Write your solution here
    pass
