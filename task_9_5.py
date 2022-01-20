#5. Реализовать класс Stationery (канцелярская принадлежность).

class Stationary:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print('запуск отрисовки')


class Pen(Stationary):
    def draw(self):
         print('рисуем ручкой', self.title)


class Pencil(Stationary):
    def draw(self):
        print('рисуем карандашом', self.title)


class Handle(Stationary):
    def draw(self):
        print('рисуем маркером', self.title)



pn = Pen('Bic')
pl = Pencil('Сакко и Ванцетти')
hl = Handle('Flip Chart')

pn.draw()
pl.draw()
hl.draw()