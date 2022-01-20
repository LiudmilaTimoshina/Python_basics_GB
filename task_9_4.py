#4. Реализуйте базовый класс Car.

class Car:
    def __init__(self, speed, color, name, is_police=False):
        self.speed, self.color, self.name, self.is_police = speed, color, name, is_police

    def go(self):
        print(f"машина {self.color} {self.name} поехала")

    def stop(self):
        print(f"машина {self.color} {self.name} остановилась")

    def turn(self, direction):
        self.direction = direction
        print(f"машина {self.color} {self.name} повернула на {self.direction}")

    def show_speed(self):
        print(f"скорость: {self.speed}")

    def check_police(self):
        print(f"полицейская: {self.is_police}")


class TownCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)

    def show_speed(self):
        print(f"скорость: {self.speed}") if self.speed <= 60 else print("превышена допустимая скорость")

    def check_police(self):
        print(self.is_police)


class SportCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)


class WorkCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)

    def show_speed(self):
        print(f"скорость: {self.speed}") if self.speed <= 40 else print("превышена допустимая скорость")


class PoliceCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, True)

    def check_police(self):
        print(f"полицейская: {self.is_police}")


c, t, s, w, p = Car(40, "белая", "Audi"), TownCar(70, "черный", "BMW"), SportCar(40, "красная", "Ferrari"),\
                WorkCar(40, "синяя", "Lada"), PoliceCar(40, "серый", "Ford Focus")

t.go(), t.turn("налево"), t.stop()
t.show_speed(), t.check_police()
print(f"марка: {c.name}, цвет: {c.color}, скорость: {c.speed}, полицейская: {c.is_police} \n")