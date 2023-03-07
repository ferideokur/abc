import random

print("Merhaba! Benim adım ChatGPT. Senin adın ne?")

name = input()

print("Merhaba " + name + "! Benim bir sayı tuttum. Bakalım tahmin edebilecek misin?")

number = random.randint(1, 20)

for guessesTaken in range(1, 7):
    print("Tahmin ettiğin sayı nedir?")
    guess = int(input())

    if guess < number:
        print("Tuttuğum sayı daha büyük.")
    elif guess > number:
        print("Tuttuğum sayı daha küçük.")
    else:
        break

if guess == number:
    print("Tebrikler, " + name + "! " + str(guessesTaken) + " tahminde sayımı buldun.")
else:
    print("Maalesef, sayım " + str(number) + " idi.")