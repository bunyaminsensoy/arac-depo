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

    def addRecord(self):
        plaka = input("Aracin plakasini giriniz: ").strip().upper()
        while not (plaka.isalnum()):
            print("Plaka sadece harf ve sayilardan olusabilir!!")
            plaka = input("Gecerli bir plaka giriniz: ").strip().upper()
        arac = Vehicle(plaka)
        if self.kayitliMi(plaka):
            self.vehicleList[plaka] = arac
            print("\n"+plaka+" plakali arac sisteme kaydedildi.", end='\n')
        else:
            print("\n"+plaka+" plakali arac sistemde zaten kayitli!", end='\n')
   
   
    def searchRecord(self, plaka):
        for i in self.vehicleList.keys():
            if i == plaka:
                return True, self.vehicleList.get(i)
        return False, None
    
    
    def getVehicle(self):
        cycleControl = True
        while cycleControl:
            plaka = input("Aracinizin plakasini giriniz: ").strip().upper()
            control, record = self.searchRecord(plaka)
            if plaka == '-1':
                break
            elif control:
                print(record)
                cycleControl = False
            else:
                print("\nBu plakayla ilgili bir kayit bulunamadi.!\n")
                print("Menuye donmek icin : -1")
    
    
    def kayitliMi(self, plaka):
        if plaka in self.vehicleList.keys():
            return False
        return True
