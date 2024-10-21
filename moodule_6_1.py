"""Задача "Съедобное, несъедобное":
Создайте:
2 класса родителя: Animal, Plant
Для класса Animal атрибуты alive = True(живой) и fed = False(накормленный), name - индивидуальное название каждого животного.
Для класса Plant атрибут edible = False(съедобность), name - индивидуальное название каждого растения

4 класса наследника:
Mammal, Predator для Animal.
Flower, Fruit для Plant.

У каждого из объектов класса Mammal и Predator должны быть атрибуты и методы:
eat(self, food) - метод, где food - это параметр, принимающий объекты классов растений.

Метод eat должен работать следующим образом:
Если переданное растение (food) съедобное - выводит на экран "<self.name> съел <food.name>", меняется атрибут fed на True.
Если переданное растение (food) не съедобное - выводит на экран "<self.name> не стал есть <food.name>", меняется атрибут alive на False.
Т.е если животному дать съедобное растение, то животное насытится, если не съедобное - погибнет.

У каждого объекта Fruit должен быть атрибут edible = True (переопределить при наследовании)

Создайте объекты классов и проделайте действия затронутые в примере результата работы программы.
"""


class Animal:

    alive = True #(живой)
    fed = False #(накормленный)

    def __init__(self, name):
        self.name = name


    def eat(self, food):
        if food.edible:
            print(f"{self.name} съел {food.name}")
            self.fed = True
        else:
            print(f"{self.name} не стал есть {food.name}")
            self.alive = False



class Plant:
    edible = False

    def __init__(self, name):
        self.name = name


class Mammale (Animal):
    pass

class Predator (Animal) :
    pass

class Flower (Plant):

    pass

class Fruit (Plant):
    edible = True





animal_1 = Predator('Волк')
animal_2 = Mammale('Мартышка')
plant_1 = Flower('Цветок')
plant_2 = Fruit('Апельсин')

print("Животное 1 - ", animal_1.name)
print("Растение 1 - ", plant_1.name)

print('Животное', animal_1.name, 'живо: ', animal_1.alive)
print('Животное', animal_2.name, 'живо: ', animal_2.alive)
print('Животное', animal_1.name, 'накормлено: ', animal_1.fed)
print('Животное', animal_2.name, 'накормлено: ', animal_2.fed)

animal_1.eat(plant_1)
animal_2.eat(plant_2)
print('Животное', animal_1.name, 'живо: ', animal_1.alive)
print('Животное', animal_2.name, 'живо: ', animal_2.alive)
print('Животное', animal_1.name, 'накормлено: ', animal_1.fed)
print('Животное', animal_2.name, 'накормлено: ', animal_2.fed)

# Что произошло: Хищник попытался съесть цветок и погиб, млекопитающее съело фрукт и насытилось.