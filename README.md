#  EKSPEDYCJA W PODZIEMIACH 

Gra labiryntowa stworzona w Pythonie z wykorzystaniem biblioteki Turtle.

# Opis gry

GGracz wciela się w małą myszkę która trafiła do podziemnego labiryntu. Jej celem jest wydostanie się z niego a przy okazji zebranie odpowiedniej ilości serów potrzebnych do użycia portalu.

Podczas eksploracji gracz musi uważać na:
- ściany (dotknięcie ściany powoduje utratę życia), 
- utratę energii (każdy krok powoduje zmniejszenie się energii o jeden ), 
- losowe zdarzenia(są to ukryte sery, które mogą losowo pojawić się w korytarzu albo szczury które zmniejszają życia o jeden), 

Gra zawiera elementy fabularne, system punktów, energii oraz życia bohatera.
---
#  Funkcje gry 

Przed rozpoczęciem gry gracz wybiera:
- imię myszy,
- poziom trudności,
- tryb wyprawy,
- warunki w tunelach,
- kierunek startowy.

---

Na mapie rozmieszczone są kawałki sera:
- zwiększają energię,
- dodają punkty,
- są wymagane do aktywacji portalu.

Po zebraniu ser znika z mapy.

---

#  Losowe zdarzenia

W trakcie poruszania się mogą wystąpić:
- ukryty zapas sera,
- atak szczura.

Zdarzenia wpływają na:
- energię,
- punkty,
- liczbę żyć.

---

# System życia i energii

Gracz posiada:
- określoną liczbę żyć,
- energię zmniejszającą się podczas ruchu.

utratę życia powoduje uderzenie w ścianę lub atak szczura .

Po utracie wszystkich żyć lub energii następuje GAME OVER.

---

# Portal

Portal otwiera możliwość ukończenia gry.

Aby aktywować portal, gracz musi zebrać minimum 3 sery.

---

# Dźwięki

Gra wykorzystuje prosty dźwięk systemowy:
- dźwięk przy uderzeniu w ścianę,

Dźwięki zostały wykonane za pomocą biblioteki:
- winsound

---

# Sterowanie

| Klawisz | Ruch |
|---|---|
| ↑ | góra |
| ↓ | dół |
| ← | lewo |
| → | prawo |

---
# Wymagane pliki

Program wymaga plików GIF:
- mysz2.gif
- sciana.gif
- ser.gif
- portal.gif

---

# Uruchomienie gry
1. Uruchom plik `main.py`
2. Wprowadź parametry wyprawy
3. Rozpocznij eksplorację labiryntu

---

# Autor projektu

Autor: [Diana Pupina]
