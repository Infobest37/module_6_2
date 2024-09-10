class Vehicle:
    def __init__(self, owner, __model, __engine_power, __color):
        self.owner = str(owner)
        self.__model = str(__model)
        self.__engine_power = int(__engine_power)
        self.__color = str(__color)
        self._COLOR_VARIANTS = ["Синий", "красный", "Желтый", "Оранжевый"]


    def get_model(self, __model):
       print(f"Модель: {self.__model}")
    def get_horsepower(self, __engine_power):
        print(f"Мощьнось двигателя: {self.__engine_power}")
    def get_color(self, __color):
        print(f"Цвет: {self.__color}")
    def info(self):
             self.get_model(str(self.__model))
             self.get_horsepower(str(self.__engine_power))
             self.get_color(str(self.__color))
             print(f"Выладелец: {self.owner}")

    def set_color(self, new_color):


        for color in self._COLOR_VARIANTS:
            if color.capitalize() == new_color.capitalize():
                print(f"Урааа мы на конец-то перекрасили машину с {self.__color} на {new_color}")
                self.__color = new_color
                return
        for color in self._COLOR_VARIANTS:
            if color.capitalize() != new_color.capitalize():
                print(f"{new_color} отсутвует в наличии")
                return




class Sedan(Vehicle):
    def __init__(self, owner, __model, __engine_power, __color, __PASSENGERS_LIMIT = 5):
        super().__init__(owner, __model, __engine_power, __color)
        self.__PASSENGERS_LIMIT = int(__PASSENGERS_LIMIT)





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