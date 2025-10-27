from homework_05.base import Vehicle
from homework_05.engine import Engine

"""
 (Вопрос проверяющему) 
 Возможно лучше определить атрибут на уровне класса и не переопределять конструктор, 
 если входные параметры конструктора не изменяются?
 Но в таком случае можно определить базовое значение для самого класса и все его инстансы будут иметь это значение (не супер очевидное поведение)
 class Car(Vehicle):
     engine: Engine
"""

class Car(Vehicle):

    def __init__(self, weight=100, fuel=50, fuel_consumption=5):
        super().__init__(weight, fuel, fuel_consumption)
        self.engine = None 

    def set_engine(self, engine: Engine):
        """Set the engine with specified parametes to the car"""
        self.engine = engine
    