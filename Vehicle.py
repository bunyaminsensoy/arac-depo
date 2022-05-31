from datetime import date
from tabnanny import verbose

class Vehicle:

    # Vehicle sinifinin constructor'i kullanicidan alinan plakayi buradaki plaka ozelligine atar.
    def __init__(self, plaka="None"):
        self.__plaka = plaka
        
     #Alttaki 4 method icin ayni prensip gecerli
        """Kullanicidan arac ozellikleriyle ilgili input aliyoruz 
        bunlari basta ve sondaki bosluk karakterlerinden kurtariyoruz. Ve hepsini buyuk harf olarak degistriyoruz
        Eger istenen formatta girilmezse sonsuz bir donguye sokuyoruz istenen format girilene kadar.   
        """
        self.__aracModeli = input("Aracinizin modelini giriniz: ").strip().upper()
        while not(self.aracModeli.isalpha()):
            print("Arac modeli sadece alfabeden olusabilir!!")
            self.__aracModeli = input("Aracinizin modelini giriniz: ").strip().upper()
                 
        self.__fuelType = input("Benzin tipini giriniz: ").strip().upper()
        while not (self.fuelType.isalpha()):
            print("Benzin tipi sadece alfabeden olusabilir!!")
            self.__fuelType = input("Benzin tipini giriniz: ").strip().upper()
       
        self.__aracYasi = input("Arac yasini giriniz: ").strip().upper()
        while not (self.aracYasi.isnumeric()):
            print("Arac yasi sadece sayılardan olusabilir!!")
            self.__aracYasi = input("Arac yasini giriniz: ").strip().upper()

        self.__motorHacmi = input("Motor hacmini giriniz: ").strip().upper()
        while not (self.motorHacmi.isnumeric()):
            print("Motor hacmi sadece sayılardan olusabilir!!")
            self.__motorHacmi = input("Motor hacmini giriniz: ").strip().upper()

        
        self.__vergiUcreti = int(self.__aracYasi) * int(self.__motorHacmi)              

        #Kullanicidan Yil-Ay-Gun seklinde bir input aliyoruz (1 bosluk birakarak) 
        #Eger istenen formatta girilmezse sonsuz bir donguye sokuyoruz dogru bir format girildiginde;
        # String methodlarından olan strip methoduyla yil ay gun degiskenlerine bu degerleri atıyoruz
        # Pythonun date modulunu kullanarak muayene tarihine bunu atiyoruz.
        
        self.tarih = input("Muayene tarihini Yil-Ay-Gun seklinde 1 bosluk birakarak giriniz : ").strip()
        while (len(self.tarih) != 10) or (self.whiteSpaceCount(self.tarih) != 2):
            print("Lutfen istenen formatta giris yapiniz!")
            self.tarih = input("Muayene tarihi giriniz: ").strip()
        yil, ay, gun = self.tarih.split()
        self.muayeneTarihi = date(int(yil), int(ay), int(gun))
      
    # Constructorda tarih inputu alirken inputtaki bosluk karakterlerinin sayisini hesaplayan fonksiyon
    
    def whiteSpaceCount(self, string):
        count = 0
        for a in string:
            if a.isspace():
                count += 1
        return count

    def returnPropertiesList(self):
        returnList = []
        returnList.append(self.plaka)
        returnList.append(self.aracModeli)
        returnList.append(self.fuelType)
        returnList.append(self.muayeneTarihi)
        returnList.append(self.aracYasi)
        returnList.append(self.motorHacmi)
        return returnList

    def __str__(self):
        print()
        suankiTarih = date.today()
        return "Arac plakasi : "+self.plaka +"\nArac modeli : "+self.aracModeli + "\nBenzin tipi : "+self.fuelType \
        + "\nArac yasi : "+self.aracYasi + "\nMotor hacmi : "+self.motorHacmi + "\nVergi ucreti : "+str(self.vergiUcreti) \
              + "\nMuayene tarihi : " +str(self.muayeneTarihi) +"\nMuayene gunune : " + str(self.muayeneTarihi-suankiTarih) + " var"

   
   #-------------------------------------- GETTER SETTER Methods----------------------------------------------#

    @property
    def plaka(self):
        return self.__plaka

    @plaka.setter
    def plaka(self, value):
        self.__plaka = value

    @property
    def fuelType(self):
        return self.__fuelType

    @fuelType.setter
    def fuelType(self, value):
        self.__fuelType = value

    @property
    def aracModeli(self):
        return self.__aracModeli

    @aracModeli.setter
    def aracModeli(self, value):
        return self.__aracModeli

    @property
    def aracYasi(self):
        return self.__aracYasi

    @aracYasi.setter
    def aracYasi(self, value):
        self.__aracYasi = value
    
    @property
    def motorHacmi(self):
        return self.__motorHacmi

    @motorHacmi.setter
    def motorHacmi(self, value):
        self.__motorHacmi = value

    @property
    def vergiUcreti(self):
        return self.__vergiUcreti

    @vergiUcreti.setter
    def vergiUcreti(self, value):
        self.__vergiUcreti = value

