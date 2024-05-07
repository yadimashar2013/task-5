class Car:
    price = 1000000

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return 'Цена {}'.format(self.__class__.price)

    def horse_powers(self):
        print('Колличество лошадинных сил 150')


class Nissan(Car):
    price = 1100000

    def horse_powers(self):
        print('Колличество лошадинных сил 170')


class Kia(Car):
    price = 900000

    def horse_powers(self):
        print('Колличество лошадинных сил 180')


obj = Nissan(name=Nissan)
print(obj)
obj.horse_powers()
obj1 = Kia(name=Kia)
print(obj1)
obj1.horse_powers()
