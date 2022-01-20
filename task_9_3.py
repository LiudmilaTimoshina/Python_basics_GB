#3. Реализовать базовый класс Worker (работник).

class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name, self.surname, self.position, self._income = name, surname, position, {"wage": wage, "bonus": bonus}


class Position(Worker):
    def __init__(self, name, surname, position, wage, bonus):
        super().__init__(name, surname, position, wage, bonus)

    def get_full_name(self):
        return f"{self.name} {self.surname}"

    def get_total_income(self):
        return f"{self._income['wage'] + self._income['bonus']}"


data_work = Position("Михаил", "Фролов", "менеджер", 500, 100)
print(data_work.get_full_name())
print(data_work.get_total_income())