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
def battleSimulation():
    if request.method == "POST":
        character = int(request.form.get("character"))
        enemy = int(request.form.get("enemy"))
            
        melkor = Dusman("Melkor", 6000, 900, 10)
        sauron = Dusman("Sauron", 2000, 300, 10)
        nazgul = Dusman("Nazgul", 500, 100, 10)

        manwe = Dusman("Manwe", 6500, 1000, 10)
        gandalf = Dusman("Gandalf", 2500, 400, 10)
        elrond = Dusman("Elrond", 1500, 200, 10)

        if character == 1:
            character = manwe
        if character == 2:
            character = gandalf
        if character == 3:
            character = elrond
        if character == 4:
            character = melkor
        if character == 5:
            character = sauron
        if character == 6:
            character = nazgul
        if enemy == 1:
            enemy = manwe
        if enemy == 2:
            enemy = gandalf
        if enemy == 3:
            enemy = elrond
        if enemy == 4:
            enemy = melkor
        if enemy == 5:
            enemy = sauron
        if enemy == 6:
            enemy = nazgul
        donenDeger1 = character.saldir()
        enemy.saldiriyaUgra(donenDeger1[0], donenDeger1[1])
        enemy.buyuBittiMi()
        enemy.hayattaMi()
        donenDeger2 = enemy.saldir()
        character.saldiriyaUgra(donenDeger2[0], donenDeger2[1])
        character.buyuBittiMi()
        character.hayattaMi()
        if character.can > enemy.can:
            winner = character.isim
            loser = enemy.isim
            attack1 = character.saldiriGucu
            attack2 = enemy.saldiriGucu
            if enemy.can <= 0:
                enemy.can = 0
                return render_template("result.html", winner = winner, attack1 = attack1, winnerHealth = character.can, winnerMagic = character.buyu, loser = loser, attack2 = attack2, loserHealth = enemy.can, loserMagic = enemy.buyu)
        elif enemy.can > character.can:
            winner = enemy.isim
            loser = character.isim
            attack1 = enemy.saldiriGucu
            attack2 = character.saldiriGucu
            if character.can <= 0:
                character.can = 0
                return render_template("result.html", winner = winner, attack1 = attack1, winnerHealth = enemy.can, winnerMagic = enemy.buyu, loser = loser, attack2 = attack2, loserHealth = character.can, loserMagic = character.buyu)
        else:
            print("Savaş berabere bitti.")
    return render_template("index.html")    

if __name__ == "__main__":
    app.run(debug=True)
