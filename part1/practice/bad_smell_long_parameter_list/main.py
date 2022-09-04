# У нас есть какой-то юнит, которому мы в параметры передаем
# - наше игровое поле
# - х координату
# - у координату
# - направление смещения
# - летит ли он
# - крадется ли он
# - скорость
# В этом примере есть сразу несколько запахов плохого кода. Исправьте их
#   (длинный метод, длинный список параметров)


class Unit:
    """Тупо взял солюшн, но мне не нравится. Мы не прописали set_unit и state.
    Можно попробовать прописать, но для абстрактной задачи слишком замороченно получается.
    """

    def __init__(self):
        pass

    def move(self, direction):
        speed = self._get_speed()

        if direction == 'UP':
            self.field.set_unit(y=self.y + speed, x=self.x, unit=self)
        elif direction == 'DOWN':
            self.field.set_unit(y=self.y - speed, x=self.x, unit=self)
        elif direction == 'LEFT':
            self.field.set_unit(y=self.y, x=self.x - speed, unit=self)
        elif direction == 'RIGTH':
            self.field.set_unit(y=self.y, x=self.x + speed, unit=self)

    def _get_speed(self):
        """Для state надо метод писать, который будет принимать is_fly или crowl и сможет его менять.
        """
        if self.state == 'fly':
            return self.speed * 1.2
        elif self.state == 'crawl':
            return self.speed * 0.5
        else:
            raise ValueError('Эк тебя раскорячило')
