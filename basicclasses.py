class Cars:
    def __init__(self, brand, year, color):
        self.brand = brand
        self.year = year
        self.color = color

    def get_info(self):
        print('Brand:', self.brand, 'Years:', self.year, 'Color:', self.color)

    def __repr__(self):
        return (f'{self.__class__.__name__},{self.brand},{self.year},{self.color}')

class PassCar(Cars):
    pass

class BusCar(Cars):
    def __init__(self, passengers, brand, year, color):
        super(BusCar, self).__init__(brand, year, color)
        self.passengers = passengers

    def get_info(self):
        super().get_info()
        print('passengers:', self.passengers)
    

class CargoCar(Cars):
    def __init__(self, tonnage, brand, year, color):
        super(CargoCar, self).__init__(brand, year, color)
        self.tonnage = tonnage

    def get_info(self):
        super().get_info()
        print('tonnage:', self.tonnage)
    



car1 = Cars('Renault', 2023, 'black')
car1.get_info()
car2 = BusCar(40, 'Mers', 2000, 'white')
car2.get_info()
car3 = CargoCar(25, 'Volvo', 2018, 'Red')
car3.get_info()


