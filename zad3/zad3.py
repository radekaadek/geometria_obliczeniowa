import matplotlib.pyplot as plt

def wewnatrz(wielokat: list[tuple], punkt: tuple) -> bool:
    """Sprawdza czy punkt jest wewnątrz wielokąta.

    Args:
        wielokat (list[tuple]): Wielokąt w postaci listy krotek.
        punkt (tuple): Punkt w postaci krotki.

    Returns:
        bool: True jeśli punkt jest wewnątrz wielokąta, False w przeciwnym wypadku.
    """
    # inicjalizacja zmiennej przechowującej liczbę przecięć
    liczba_przeciec = 0
    
    # iteracja po bokach wielokąta
    for i in range(len(wielokat)):
        # punkty definiujące bok
        p1 = wielokat[i]
        p2 = wielokat[(i+1) % len(wielokat)]
        
        # sprawdzenie czy odcinek p1-p2 przecina odcinek pionowy przechodzący przez punkt
        if (p1[1] > punkt[1]) != (p2[1] > punkt[1]) and punkt[0] < (p2[0] - p1[0]) * (punkt[1] - p1[1]) / (p2[1] - p1[1]) + p1[0]:
            liczba_przeciec += 1
    
    # zwrócenie True jeśli liczba przecięć jest nieparzysta, False w przeciwnym wypadku
    return liczba_przeciec % 2 == 1

plt.figure(figsize=(10, 10))

with open("Wielokat.txt") as f:
    wielokat = [tuple(map(float, line.split())) for line in f]

plt.plot([punkt[0] for punkt in wielokat], [punkt[1] for punkt in wielokat], "b-")

with open("PunktyDoKontroli.txt") as f:
    punkty = [tuple(map(float, line.split())) for line in f]

with open("Wyniki.txt", "w") as f:
    for punkt in punkty:
        if wewnatrz(wielokat, punkt):
            plt.plot(punkt[0], punkt[1], "ro")
        f.write(wewnatrz(wielokat, punkt).__str__() + "\n")

plt.show()