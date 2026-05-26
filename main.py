import turtle
import random
import winsound
imie_myszy = input("Podaj imię swojej myszy: ").strip()
zycia = 3
punkty = 0
zebrane_sery = 0
if imie_myszy == "":
    imie_myszy = "Mysia"
print("\n=== START WYPRAWY ===")
print("Bohater:", imie_myszy)
print("Cel wyprawy: odnaleźć wyjście z labiryntu")
print("Liczba żyć:", zycia)
print("======================\n")
print("\nPoziomy trudności:")
print("łatwy")
print("normalny")
print("trudny")

trudnosc = input("Wybierz poziom trudności: ").lower().strip()
if trudnosc not in ["łatwy", "normalny", "trudny"]:
    print("Niepoprawny poziom. Ustawiono normalny.")
    trudnosc = "normalny"
if trudnosc == "łatwy":
    zycia = 3
    energia = 100

elif trudnosc == "normalny":
    zycia = 3
    energia = 70

else:
    zycia = 3
    energia = 50
print("\nKierunek startowy myszy:")
print("góra")
print("dół")
print("lewo")
print("prawo")

kierunek_startowy = input("Wybierz kierunek: ").lower().strip()

if kierunek_startowy not in ["góra", "dół", "lewo", "prawo"]:
    print("Ustawiono kierunek: dół")
    kierunek_startowy = "dół"
    
print("\nTryby wyprawy:")
print("odkrywca")
print("przetrwanie")
print("eksploracja")

tryb = input("Wybierz tryb wyprawy: ").lower().strip()

if tryb not in ["odkrywca", "przetrwanie", "eksploracja"]:
    print("Niepoprawny tryb. Ustawiono eksploracja.")
    tryb = "eksploracja"
print("\nWarunki w tunelach:")
print("suche")
print("wilgotne")

warunki = input("Wybierz warunki: ").lower().strip()

if warunki not in ["suche", "wilgotne"]:
    print("Ustawiono: suche")
    warunki = "suche"

print("\n==============================")
print(" EKSPEDYCJA W PODZIEMIACH ")
print("==============================\n")

print("Mała mysz od dawna błąka się w ciemnych, zapomnianych tunelach pod ziemią.")
print("Nie pamięta już, jak trafiła do tego miejsca — wie tylko, że musi znaleźć wyjście.\n")
print("W głębi podziemi znajdują się kawałki sera — źródło energii do przetrwania i jedyna możliwość do udanego wyjścia z labiryntu.")
print("Legenda mówi, że w centrum podziemi istnieje ukryte wyjście...")
print("Ale niewiele myszy wróciło, by to potwierdzić.\n")
print("Teraz wszystko zależy od jednej myszy...\n")

print("=== PARAMETRY WYPRAWY ===")
print("Bohater:", imie_myszy)
print("Poziom trudności:", trudnosc)
print("Tryb wyprawy:", tryb)
print("Kierunek startowy:", kierunek_startowy)
print("Liczba żyć:", zycia)
print("Energia:", energia)
print("==========================\n")
print("Czas rozpocząć wyprawę...\n")

# EKRAN
BOK_KAFELKA = 35

okno = turtle.Screen()
okno.title("Labirynt")
okno.bgcolor("black")
okno.tracer(0)

# MAPA 
mapa_labiryntu = [
    "XXXXXXXXXXXXXXXXXXXXXX X",
    "X X XXX    S         X X",
    "X X     XXXXXXXXXXXX X X",
    "X XXXXXXX    X     X X X",
    "X         XX X XXX X X X",
    "X XXXXXXXXXX X XPX X X X",
    "X X            X X   X X",
    "X X XXXXXXXXXXXX XXXXX X",
    "X X     S         X  X X",
    "X XXXXXXXXXXXXXXXXXX X X",
    "X                    X X",
    "X XXXXXXXX XXXXXXXXXXX X",
    "X X      X XS        X X",
    "X X XXXXXX XXXXXXXX XX X",
    "X       SX             X",
    "XXXXXXXXXXXXXXXXXXXXXXXX",
]
okno.update()
# GIFY
okno.addshape("mysz2.gif")
okno.addshape("sciana.gif")
okno.addshape("ser.gif")
okno.addshape("portal.gif")
# MYSZKA
bohater = turtle.Turtle()
bohater.shape("mysz2.gif")
bohater.penup()
bohater.goto(350, 280)
if kierunek_startowy == "góra":
    bohater.setheading(90)

elif kierunek_startowy == "dół":
    bohater.setheading(270)

elif kierunek_startowy == "lewo":
    bohater.setheading(180)

else:
    bohater.setheading(0)
# KOMUNIKATY

napis = turtle.Turtle()

napis.hideturtle()

napis.penup()

napis.color("lightblue")

napis.goto(0, 320)


def pokaz_komunikat(tekst):

    napis.clear()

    napis.goto(0, 320)

    napis.write(
        tekst,
        align="center",
        font=("Arial", 18, "bold")
    )

    okno.update()


def pokaz_zycia():

    serca.clear()

    serca.write(
        "❤️ " * zycia,
        font=("Arial", 20, "bold")
    )

    okno.update()
# SERDUSZKA

serca = turtle.Turtle()

serca.hideturtle()

serca.penup()

serca.color("red")

serca.goto(-420, 320)

# WYLICZENIE MAPY
szerokosc = len(mapa_labiryntu[0]) * BOK_KAFELKA
wysokosc = len(mapa_labiryntu) * BOK_KAFELKA

start_x = -szerokosc / 2
start_y = wysokosc / 2

# ELEMENTY AKCJI
sery = []
def dodaj_ser(x, y):
    ser = turtle.Turtle()
    ser.shape("ser.gif")
    ser.penup()
    ser.goto(x, y)
    sery.append(ser)


def sprawdz_ser():
    global energia, punkty, zebrane_sery

    for ser in sery:

        if bohater.distance(ser) < 20:

            ser.hideturtle()
            sery.remove(ser)

            energia += 30
            punkty += 10
            zebrane_sery += 1
            
            pokaz_komunikat("ZNALEZIONO SER!")

            print("\n Mysz znalazła kawałek sera!")
            print("Energia +20")
            print("Punkty +10")
            print("Aktualna energia:", energia)
            print("Aktualne punkty:", punkty)
            print("Pozostałe sery:", len(sery))
            print("Zebrane sery:", zebrane_sery)
            break
portale = []

def dodaj_portal(x, y):
    portal = turtle.Turtle()
    portal.shape("portal.gif")
    portal.penup()
    portal.goto(x, y)

    portale.append(portal)
    
def sprawdz_portal():

    global zebrane_sery

    for portal in portale:

        if bohater.distance(portal) < 20:

            if zebrane_sery >= 3:

                wygrana()

            else:

                brak = 3 - zebrane_sery

                pokaz_komunikat("PORTAL ZAMKNIĘTY")

                print("\nPortal jest zamknięty!")
                print("Potrzebujesz jeszcze", brak, "ser/y.")
    
# ŚCIANY
sciany = []

for y, wiersz in enumerate(mapa_labiryntu):
    for x, pole in enumerate(wiersz):

        px = start_x + x * BOK_KAFELKA
        py = start_y - y * BOK_KAFELKA

        if pole == "X":
            blok = turtle.Turtle()
            blok.shape("sciana.gif")
            blok.penup()
            blok.goto(px, py)
            sciany.append(blok)
        elif pole == "S":
            dodaj_ser(px, py)
        elif pole == "P":
            dodaj_portal(px, py)    
# KOLIZJE
def czy_sciana(x, y):
    for s in sciany:
        if s.distance(x, y) < 20:
            return True
    return False

# RUCH
def losowe_zdarzenie():
    global energia, punkty, zycia

    liczba = random.randint(1, 25)

    # UKRYTY SER
    if liczba == 1:

        energia += 10
        punkty += 5

        pokaz_komunikat("UKRYTY SER!")

        print("\n Mysz znalazła ukryty zapas sera!")
        print("Energia +10")
        print("Punkty +5")
        print("Aktualna energia:", energia)
        print("Aktualne punkty:", punkty)

    # SZCZUR
    elif liczba == 2:

        zycia -= 1

        pokaz_komunikat("ATAK SZCZURA!")

        winsound.Beep(250, 300)

        print("\n Dziki szczur zaatakował mysz!")
        print("Życie -1")
        print("Pozostałe życia:", zycia)

        pokaz_zycia()

        if zycia <= 0:
            game_over()
krok = 0

def akcja_ruchu(opis, dx, dy):
    global krok, energia

    x = bohater.xcor()
    y = bohater.ycor()

    nowe_x = x + dx
    nowe_y = y + dy

    if czy_sciana(nowe_x, nowe_y):
        hit()
        print(" Mysz natrafiła na ścianę...")
        return

    bohater.goto(nowe_x, nowe_y)
    
    napis.clear()
    
    sprawdz_ser()
    
    losowe_zdarzenie()
    
    sprawdz_portal()
    
    krok += 1
    
    energia -= 1

    print("\n--- KROK", krok, "---")
    print("Akcja:", opis)
    print("Pozycja:", (x, y), "→", (nowe_x, nowe_y))
    print("Energia:", energia)
    print("Punkty:", punkty)
    print("Pozostałe życia:", zycia)
    print("Pozostałe sery:", len(sery))
    if energia <= 0:
        print("Mysz traci siły...")
        game_over()

def game_over():

    print("\n========== GAME OVER ==========")
    print("Bohater:", imie_myszy)
    print("Liczba kroków:", krok)
    print("Zdobyte punkty:", punkty)
    print("Pozostała energia:", energia)
    print("Pozostałe życia:", zycia)
    print("Zebrane sery:", zebrane_sery)
    print("Pozostałe sery:", len(sery))
    print("Labirynt okazał się silniejszy...")
    print("Wyprawa zakończona porażką.")
    print("================================\n")

    bohater.hideturtle()

    for s in sciany:
        s.hideturtle()

    for ser in sery:
        ser.hideturtle()
        
    for portal in portale:
        portal.hideturtle()
    
    serca.clear()
    serca.hideturtle()
    napis.clear()
    napis.goto(0, 0)
    napis.color("red")

    napis.write(
        "GAME OVER",
        align="center",
        font=("Arial", 50, "bold")
    )
    for s in sciany:
        s.hideturtle()
        
    for ser in sery:
        ser.hideturtle()
    
    napis.clear()
    napis.goto(0, 0)
    napis.color("red")
    napis.write(
        "GAME OVER",
        align="center",
        font=("Arial", 50, "bold")
    )

def wygrana():

    print("\n========== WYGRANA ==========")
    print("Bohater:", imie_myszy)
    print("Liczba kroków:", krok)
    print("Zdobyte punkty:", punkty)
    print("Pozostała energia:", energia)
    print("Zebrane sery:", zebrane_sery)
    print("Mysz odnalazła wyjście z labiryntu!")
    print("Wyprawa zakończona sukcesem!")
    print("================================\n")

    bohater.hideturtle()

    for s in sciany:
        s.hideturtle()

    for ser in sery:
        ser.hideturtle()

    for portal in portale:
        portal.hideturtle()

    serca.clear()

    napis.clear()
    napis.goto(0, 0)
    napis.color("lightgreen")

    napis.write(
        "WYGRANA!",
        align="center",
        font=("Arial", 50, "bold")
    )
def hit():
    global zycia

    winsound.Beep(400, 200)

    zycia -= 1
    pokaz_zycia()

    if zycia <= 0:
        game_over()
    else:
        pokaz_komunikat("ŚCIANA")


def gora():
    akcja_ruchu("ruch w górę", 0, BOK_KAFELKA)

def dol():
    akcja_ruchu("ruch w dół", 0, -BOK_KAFELKA)

def lewo():
    akcja_ruchu("ruch w lewo", -BOK_KAFELKA, 0)

def prawo():
    akcja_ruchu("ruch w prawo", BOK_KAFELKA, 0)

# KLAWISZE
okno.listen()
okno.onkey(gora, "Up")
okno.onkey(dol, "Down")
okno.onkey(lewo, "Left")
okno.onkey(prawo, "Right")

# START

pokaz_komunikat("Start!")

pokaz_zycia()

okno.update()

while True:
    okno.update()
