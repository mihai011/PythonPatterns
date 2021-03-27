from abc import ABC, abstractmethod
from unittest import TestCase

class TestFlyWeight(TestCase):

    def test_some(self):
        
        d1 = CarDealer()
        d2 = CarDealer()

        d1.stock_cars("Brand", 12)
        d2.stock_cars("Control", 23)

        d1.sell("Control", 2)
        d2.sell("Brand", 4)

        self.assertEqual(d1.total_income(), 23*2)
        self.assertEqual(d2.total_income(), 12*4)

class Car():

    def __init__(self, brand, cost):

        self.brand = brand
        self.cost = cost


class CarDealer():

    stock = {}

    def __init__(self):

        self.orders = {}

    def sell(self, brand, units):

        self.orders.setdefault(brand, 0)

        self.orders[brand] += units

    def stock_cars(self, brand, cost):

        self.stock[brand] = Car(brand, cost)

    def total_sold_units(self):

        return sum(self.orders.values)

    def total_income(self):

        income = 0 
        for brand, units in self.orders.items():
            income += self.stock[brand].cost * units

        return income


    

    
