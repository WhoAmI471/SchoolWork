class Box():

    def box(self, size, weight, contains):
        self.size = size
        self.weight = weight
        self.contains = contains

    # def size(self):
    #     pass

    # def weight(self):
    #     pass

    # def contains(self):
    #     pass

    def observe(self):
        return f'Это похоже на ящик размером {self.size}x{self.weight} и весом {self.contains}кг'


class Container(Box):
    def open():
        pass

box_1 = Box(30, 30, 1, "15 золотых монет")

container_1 = Container(1, 1, 1)

# Код проверки, не удаляйте его

try: Box
except:print("Класс Box не задан")
try: Container
except:print("Класс Container не задан")
try: Container.open
except:print("Метод open у Container не задан или с ошибкой")
try: Container.observe
except:print("Метод observe у Container не наследуется или с ошибкой")
try: box_1
except:print("Экземпляр box_1 не существует")
try: container_1
except:print("Экземпляр container_1 не существует")

print(container_1.observe())
print(container_1.open())



