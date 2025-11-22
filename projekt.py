class car:
    def __init__(self, marka, color, maxspeed):
        self.marka = marka
        self.color = color
        self.maxspeed = maxspeed
        
    def changeColor(self, color):
        self.color = color
        print(f"your car have color - {color}")
        
    def printInfo(self):
        print(f"your car {self.marka} color {self.color} crashed at speed {self.maxspeed} km per hour")
        
car1 = car("Tesla", "wiht", 150)
car1.changeColor("black")
car1.printInfo()






# Клас - квартира

# продумати одразу приватність/публічніть атрибутів 

# 1. Атрибути (параметри): ціна, квадратура квартири, поверх, наявність балкону, кількість кімнат, район
# 2. Функціїї(яка взаємодія): купити/продати, ремонт, вивести інформацію повну про квартиру 
# 3. реалізація

# під час реалізації користувач сам заповнює параметри і створює із нього обʼєкт



class apartment:
    def __init__(self, price, square, hight, balcony, rooms, district, survival, sell, repair, information_about_the_apartment):
        self.__price = price
        self.__square = square
        self.__hight = hight
        self.__balcony = balcony
        self.__rooms = rooms
        self.__district = district
        self.__survival = survival
        self.__sell = sell
        self.__repair = repair
        self.__information_about_the_apartment = information_about_the_apartment

    def setprice(self, price):
        self.__price = price

    def repair(self):
        self.__price = self.__price + 10000    