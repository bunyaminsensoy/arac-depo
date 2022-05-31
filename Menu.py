from Vehicle import Vehicle
import pandas as pd

class Menu:
    def __init__(self):
        print("Menuye hosgeldiniz diyelim ")
        self.vehicleList = {}
        self.printRecord = []

    def menu(self):
        cycle = True
        print("Kayit eklemek icin :1\n""Kayit okumak icin :2\n"
              "Arac bilgilerini gormek icin :3\n" "Programi sonlandirmak icin :4\n")