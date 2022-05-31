from Vehicle import Vehicle
import pandas as pd

class Menu:
    def __init__(self):
        print("Menuye hosgeldiniz diyelim ")
        self.vehicleList = {}
        self.printRecord = []

    def menu(self):
        cycle = True
        print("Kayit eklemek icin :1\n""Tüm kayıtları görmek için :2\n"
              "Arac bilgilerini gormek icin :3\n" "Programi sonlandirmak icin :4\n")

        while( cycle ):      # Degisken kontrollu bir dongu yaptim. Cikmak istedigim zaman bu degiskeni false yapip donguyu sonlandiriyorum
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

         # Kayit ekleme fonksiyonu 
    """ Kullanicidan arac plakasi alan bunu sistemde kayitli degilse sisteme ekleyen 
        ayrica eklenip eklenmedigini ekrana yazdiran bir fonksiyon yazdim. Bunu yazarken bosluk duyarlikli
        ve girilen inputu upperCase formuna ceviren static methodlarida kullandim.
        Dictinory'e ekledigim deger {plaka:arac nesnesi } seklinde oldugunu belirtmek isterim. 
    """

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
            
    # Girilen plakayi dic'te ariyorum varsa geriye False ve none tupple'i donduruyorum
    # Yoksa plakanin eklenebilir oldugunu soyluyorum ve geriye dict'i gonderiyorum
   
    def searchRecord(self, plaka):
        for i in self.vehicleList.keys():
            if i == plaka:
                return True, self.vehicleList.get(i)
        return False, None
    
    #Sistemde girilen araclari aramaya yonelik bir fonksiyon
    #Bu fonksiyon girilen plakanin sistemde varolup olmadigini tespit edip;
    # Eger varsa arac bilgilerini ekrana yazdiran yoksa bilgilendirme mesaji ekrana yazdiran bir fonksiyon yazdim
    
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
    
    # Girilen plakanin sistemde kayitli olup olmadigini sorgulayan fonksiyon
    # Return olarak boolean bir ifade dondurur.
    
    def kayitliMi(self, plaka):
        if plaka in self.vehicleList.keys():
            return False
        return True

# Girilen tum kayitlari pandas kutuphanesiyle ekrana yazdiriyorum

    def readRecords(self):
        print()
        self.objectToList()  # Fonksiyon hakkindaki gerekli aciklamalari yaptim
 # Pandas modulunun dataFrame methoduyla sisteme girilen araclarin listelenmesi ve kategorize edilmesini sagladim

        df = pd.DataFrame(self.printRecord, columns=[' Plaka ', ' \nArac Modeli ', '\n Benzin Turu ', '\n Muayene Tarihi ', '\n Arac yasi ', '\n Motor hacmi ', ])
        print(df.to_string())
 
 # Basta dictinory'de tuttugum kayitlari Vehicle'da halihazirda yazilmis olan returnPropertiesList() methoduyla  
 # obje hakkindaki verileri burada printRecordList degiskenine ekliyorum (Yani double list yapiyorum dataFrame kullanabilmek icin)
   
    def objectToList(self):
        for i in self.vehicleList.keys():
            temp = self.vehicleList.get(i)
            self.printRecord.append(temp.returnPropertiesList())
