
class Vehicle:
    def _init_(self, plaka="None"):
        self.__plaka = plaka

        self.__aracModeli = input("Aracinizin modelini giriniz: ").strip()
        while not(self.aracModeli.isalpha()):
            print("Arac modeli sadece alfabeden olusabilir!!")
            self.aracModeli = input("Aracinizin modelini giriniz: ").strip()

        self.__fuelType = input("Benzin tipini giriniz: ").strip()
        while not (self.fuelType.isalpha()):
            print("Benzin tipi sadece alfabeden olusabilir!!")
            self.fuelType = input("Benzin tipini giriniz: ").strip()

        self.__muayeneTarihi = input("Muayene tarihini giriniz : ").strip()
        while not (self.muayeneTarihi.isnumeric()):
            print("Muayene tarihi sayilardan olusmalidir!")
            self.muayeneTarihi = input("Muayene tarihi giriniz: ").strip()


    def _str_(self):
        print()
        return "Arac plakasi : "+self.plaka +"\nArac modeli : "+self.aracModeli + "\nBenzin tipi : "+self.fuelType+ "\nMuayene tarihi : " +self.muayeneTarihi


#-------------------------------GETTER SETTER METHODS-----------------------------------------#
    
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
    def muayeneTarihi(self):
        return self.__muayeneTarihi

    @muayeneTarihi.setter
    def muayeneTarihi(self, value):
        self.__muayeneTarihi = value

    @property
    def aracModeli(self):
        return self.__aracModeli

    @aracModeli.setter
    def aracModeli(self, value):
        return self.__aracModeli