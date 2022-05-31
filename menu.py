from Vehicle import Vehicle
import pandas as pd




            
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

    def readRecords(self):
        print()
        copyList = pd.Series(self.vehicleList, name="Kayit Listesi")
        print(copyList)

    def objectToList(self):
        print(pd.Series(self.vehicleList))

