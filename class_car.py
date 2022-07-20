class Car():
    '''описание автомобиля'''
    def __init__(self, color, view, brand, drive):
        '''свойства автомобиля'''
        self.color = color
        self.view = view
        self.brand = brand
        self.drive = drive

    def creation(self):
        '''создание автомобиля'''
        print('''цвет авто''' + self.color + '''привод авто''' + self.drive + '''марка авто''' + self.brand + '''вид авто''' + self.view + """создан""")

Car1 = Car("синего цвета","передний привод","Hyundai",  "легковой")
Car2 = Car("красный", "задний привод авто", "BMW", "микроавтобус")
print(Car2.brand)