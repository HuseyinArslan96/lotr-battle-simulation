import random
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

class Dusman:
    def __init__(self, isim = "Nazgul", can = 500, saldiriGucu = 100, buyu = 10):
        self.isim = isim
        self.can = can
        self.saldiriGucu = saldiriGucu
        self.buyu = buyu
    def saldir(self):
        print(f"{self.isim} saldırıyor...")
        print("Büyü gücü: ", self.saldiriGucu)
        harcananBuyu = random.randrange(3,10)
        print(f"Harcanan büyü sayısı: {harcananBuyu}")
        self.buyu-= harcananBuyu
        print(f"Kalan büyü sayısı: {self.buyu} ")
        verilenZarar = harcananBuyu * self.saldiriGucu
        print("Verilen zarar: ", verilenZarar)
        return (harcananBuyu, self.saldiriGucu, verilenZarar)
    def saldiriyaUgra(self, harcananBuyu, saldiriGucu):
        print(f"{self.isim}: Saldırıya uğruyorum...")
        print(f"Can: {self.can}")
        self.can -= harcananBuyu * saldiriGucu
    def buyuBittiMi(self):
        if self.buyu <= 0:
            print(str(self.isim) + " savaş meydanından çekiliyor.")
            return True
        return False
    def hayattaMi(self):
        if self.can <= 0:
            print(str(self.isim) + " öldü.")
        else:
            print("Kalan can: ", self.can)    
    def print(self):
        print("İsim:", self.isim, "\n" "Kalan Can:", self.can, "\n" "Saldırı Gücü:", self.saldiriGucu, "\n" "Kalan Büyü Sayısı:", self.buyu)

@app.route("/", methods=["GET", "POST"])
def savaş_simülasyonu():
    if request.method == "POST":
        karakter = int(request.form.get("karakter"))
            
        melkor = Dusman("Melkor", 6000, 900, 10)
        sauron = Dusman("Sauron", 2000, 300, 10)
        nazgul = Dusman("Nazgul", 500, 100, 10)

        manwe = Dusman("Manwe", 6500, 1000, 10)
        gandalf = Dusman("Gandalf", 2500, 400, 10)
        elrond = Dusman("Elrond", 1500, 200, 10)

        evil = [melkor, sauron, nazgul]
        good = [manwe, gandalf, elrond]
        if karakter == 1:
            karakter = manwe
        if karakter == 2:
            karakter = gandalf
        if karakter == 3:
            karakter = elrond
        if karakter == 4:
            karakter = melkor
        if karakter == 5:
            karakter = sauron
        if karakter == 6:
            karakter = nazgul
        if karakter in evil:
            rastgele = random.choice(good)
        if karakter in good:
            rastgele = random.choice(evil)    
        donenDeger1 = karakter.saldir()
        rastgele.saldiriyaUgra(donenDeger1[0], donenDeger1[1])
        rastgele.buyuBittiMi()
        rastgele.hayattaMi()
        donenDeger2 = rastgele.saldir()
        karakter.saldiriyaUgra(donenDeger2[0], donenDeger2[1])
        karakter.buyuBittiMi()
        karakter.hayattaMi()
        if karakter.can > rastgele.can:
            kazanan = karakter.isim
            kaybeden = rastgele.isim
            saldiri1 = karakter.saldiriGucu
            saldiri2 = rastgele.saldiriGucu
            if rastgele.can <= 0:
                rastgele.can = 0
                return render_template("result.html", kazanan = kazanan, saldiri1 = saldiri1, kalanCan = karakter.can, kalanBuyu = karakter.buyu, kaybeden = kaybeden, saldiri2 = saldiri2, kaybedenCan = rastgele.can, kaybedenBuyu = rastgele.buyu)
        elif rastgele.can > karakter.can:
            kazanan = rastgele.isim
            kaybeden = karakter.isim
            saldiri1 = rastgele.saldiriGucu
            saldiri2 = karakter.saldiriGucu
            if karakter.can <= 0:
                karakter.can = 0
                return render_template("result.html", kazanan = kazanan, saldiri1 = saldiri1, kalanCan = rastgele.can, kalanBuyu = rastgele.buyu, kaybeden = kaybeden, saldiri2 = saldiri2, kaybedenCan = karakter.can, kaybedenBuyu = karakter.buyu)
        else:
            print("Savaş berabere bitti.")
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
