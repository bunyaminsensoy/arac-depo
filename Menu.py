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

        while( cycle ):     
            try:
                choose = input("Lutfen yapmak istediginiz islemi secin: ").strip()
                while not(choose.isnumeric()):
                    choose = input("Gecersiz bir komut girildi, tekrar deneyin: ")
            except Exception as e:
                print("Oops! ", e.__class__, " hatasi meydana geldi!")
            if choose == '1':
                self.addRecord()
            if choose == '2':
                self.readRecords()
            if choose == '3':
                self.getVehicle()
            if choose == '4':
                print("Programdan cikiliyor..")
                cycle = False
            print()