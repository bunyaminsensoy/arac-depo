from datetime import date
from tabnanny import verbose

class Vehicle:
    
    def __init__(self, plaka="None"):
        self.__plaka = plaka

        self.__aracModeli = input("Aracinizin modelini giriniz: ").strip().upper()
        while not(self.aracModeli.isalpha()):
            print("Arac modeli sadece alfabeden olusabilir!!")
            self.__aracModeli = input("Aracinizin modelini giriniz: ").strip().upper()
                 
        self.__fuelType = input("Benzin tipini giriniz: ").strip().upper()
        while not (self.fuelType.isalpha()):
            print("Benzin tipi sadece alfabeden olusabilir!!")
            self.__fuelType = input("Benzin tipini giriniz: ").strip().upper()