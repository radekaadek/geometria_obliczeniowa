import matplotlib.pyplot as plt
import math
import itertools

def punkt_na_odcinku(punkt: tuple, odcinek: list[tuple]) -> bool:
    if min(odcinek[0][0], odcinek[1][0]) <= punkt[0] <= max(odcinek[0][0], odcinek[1][0]):
        if min(odcinek[0][1], odcinek[1][1]) <= punkt[1] <= max(odcinek[0][1], odcinek[1][1]):
            # Oblicz nachylenie odcinka
            if odcinek[0][0] != odcinek[1][0]:
                nachylenie = (odcinek[1][1] - odcinek[0][1]) / (odcinek[1][0] - odcinek[0][0])
            else:
                if odcinek[0][0] == odcinek[1][0] and punkt[0] == odcinek[0][0]:
                    return True
            
            # Oblicz przesunięcie (b) równania prostej y = mx + b
            przesuniecie = odcinek[0][1] - nachylenie * odcinek[0][0]

            # Sprawdź, czy punkt leży na odcinku, korzystając z równania prostej
            if punkt[1] == nachylenie * punkt[0] + przesuniecie:
                return True
    
    return False

def wewnatrz(wielokat: list[tuple], punkt: tuple) -> bool:
    """Sprawdza czy punkt jest wewnątrz wielokąta.

    Args:
        wielokat (list[tuple]): Wielokąt w postaci listy krotek.
        punkt (tuple): Punkt w postaci krotki.

    Returns:
        bool: True jeśli punkt jest wewnątrz wielokąta, False w przeciwnym wypadku.
    """

    # sprawdzanie czy znajduje sie wewnatrz prostokata
    min_x = min([punkt[0] for punkt in wielokat])
    max_x = max([punkt[0] for punkt in wielokat])
    min_y = min([punkt[1] for punkt in wielokat])
    max_y = max([punkt[1] for punkt in wielokat])
    if punkt[0] < min_x or punkt[0] > max_x or punkt[1] < min_y or punkt[1] > max_y:
        return False

    # inicjalizacja zmiennej przechowującej liczbę przecięć
    liczba_przeciec = 0
    
    # iteracja po bokach wielokąta
    for i in range(len(wielokat)):
        # punkty definiujące bok
        p1 = wielokat[i]
        p2 = wielokat[(i+1) % len(wielokat)]

        # sprawdzenie czy punkt leży na boku wielokąta
        if punkt_na_odcinku(punkt, [p1, p2]):
            return True
        
        # sprawdzenie czy odcinek p1-p2 przecina odcinek pionowy przechodzący przez punkt
        if (p1[1] > punkt[1]) != (p2[1] > punkt[1]) and punkt[0] < (p2[0] - p1[0]) * (punkt[1] - p1[1]) / (p2[1] - p1[1]) + p1[0]:
            liczba_przeciec += 1
        
            
    # zwrócenie True jeśli liczba przecięć jest nieparzysta, False w przeciwnym wypadku
    return liczba_przeciec % 2 == 1

plt.figure(figsize=(10, 10))

with open("Wielokat2.txt") as f:
    wielokat = [tuple(map(float, line.split())) for line in f]

plt.plot([punkt[0] for punkt in wielokat], [punkt[1] for punkt in wielokat], "b-")
# plot last line
plt.plot([wielokat[-1][0], wielokat[0][0]], [wielokat[-1][1], wielokat[0][1]], "b-")

with open("PunktyDoKontroli.txt") as f:
    punkty = [tuple(map(float, line.split())) for line in f]

with open("Wyniki.txt", "w") as f:
    for punkt in punkty:
        if wewnatrz(wielokat, punkt):
            plt.plot(punkt[0], punkt[1], "ro")
        f.write(wewnatrz(wielokat, punkt).__str__() + "\n")

plt.show()