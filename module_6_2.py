class Vehicle:
    def __init__(self, owner, __model, __engine_power, __color):
        self.owner = str(owner)
        self.__model = str(__model)
        self.__engine_power = int(__engine_power)
        self.__color = str(__color)
        self._COLOR_VARIANTS = ["Синий", "Красный", "Желтый", "Оранжевый"]


    def get_model(self, __model):
       self.__model = str(__model)
       return self.__model
    def get_horsepower(self, __engine_power):
        self.__engine_power = int(__engine_power)
        return self.__engine_power
    def get_color(self, __color):
        self.__color = str(__color)
        return self.__color

    def info(self):
        print(f"Mодель: {self.__model}\nМощьность двигателя: {self.__engine_power}\nЦвет: {self.__color}\n"
              f"Владелец: {self.owner}")

    def set_color(self, new_color):
        self.__color = new_color.upper()
        if new_color.upper() in self._COLOR_VARIANTS:
            self._COLOR_VARIANTS.remove(new_color.upper())

        else:
            print(f"{new_color} цвет отсутствует в наличии")


class Sedan(Vehicle):
    def __init__(self, owner, __model, __engine_power, __color):
        super().__init__(owner, __model, __engine_power, __color)
        self._owner = str(owner)
        self.__model = str(__model)
        self.__engine_power = int(__engine_power)
        self.__color = str(__color)




# Текущие цвета __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']
vehicle1 = Sedan('Fedos', 'Toyota Mark II', 500, 'blue')

# Изначальные свойства
vehicle1.info()

# # Меняем свойства (в т.ч. вызывая методы)
vehicle1.set_color('Розовый')
vehicle1.set_color('КРАСНЫЙ')
vehicle1.owner = 'Vasyok'
#
# # Проверяем что поменялось
vehicle1.info()