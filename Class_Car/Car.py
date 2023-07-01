# Make a class Car
class Car:
    def __init__(self, year_model, make):
        self.__year_model= year_model
        self.__make= make
        self.__speed= 0
    
    # Method for Acceleration
    def accelerate(self):
        self.__speed += 5

    # Method for Brake
    def brake(self):
        self.__speed -= 5
        if self.__speed < 0:
            self.__speed = 0
    # Getter Method for speed
    def get_speed(self):
        return self.__speed
    

