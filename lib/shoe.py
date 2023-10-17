#!/usr/bin/env python3

class Shoe:
    def __init__(self, brand = "Adidas", size = 9):
        self._brand = brand
        self._size = size
        self._condition = "New"
    
    def brand(self):
        return self._brand
    
    def set_brand(self, brand):
        self._brand = brand
    brand = property(brand, set_brand)
    
    def get_size(self):
        return self._size
    
    def set_size(self, size):
        if type(size) != int:
            print("size must be an integer")
        self._size = size
    size = property(get_size, set_size)

    def cobble(self):
        self._condition = "New"
        print("Your shoe is as good as new!")

    def get_condition(self):
        return self._condition

    def set_condition(self, condition):
        self._condition = condition
    condition = property(get_condition, set_condition)
pass


    
    
