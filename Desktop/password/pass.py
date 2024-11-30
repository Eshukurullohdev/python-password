import string
import random

katta = list(string.ascii_lowercase)
kichik = list(string.ascii_uppercase)
harf = katta + kichik
sumbols = list(string.punctuation)
raqamlar = []

for x in range(0, 10):
    raqamlar.append(x)


sorov_harf  = int(input("nechta harf qatnashsin Iltimos harfni kiriti: "))
sorov_raqam  = int(input("nechta raqam qatnashsin Iltimos raqamni kiriti: "))
sorov_symbol  = int(input("nechta symbol qatnashsin Iltimos symbolni kiriti: "))
print(sorov_harf)
boshqolsa = ""

for h in range(0, sorov_harf):
    random_harf = random.choice(harf)
    boshqolsa += random_harf

for r in range(0, sorov_raqam):
     random_raqam = random.choice(raqamlar)
     boshqolsa += str(random_raqam)


for s in range(0, sorov_symbol):
    random_symbol = random.choice(sumbols)
    boshqolsa += random_symbol

password =[]

for p in boshqolsa:
    password.append(p)

random.shuffle(password)

real_password = ""

for a in password:
    real_password += a


print(real_password)






