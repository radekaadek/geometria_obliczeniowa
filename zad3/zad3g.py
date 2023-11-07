# 4 WYZNACZENIE POŁOŻENIA PUNKTU WZGLĘDEM WIELOKĄTA
# Ustalanie położenia punktu względem wielokąta podobnie jak obliczanie współrzędnych punktu
# przecięcia dwóch odcinków, jest jedną z najczęściej wykonywanych czynności w procesie analizy
# danych przestrzennych. Celem rozpatrywanego zadania jest ustalenie położenia punktu o zadanych
# współrzędnych P(x,y) względem wielokąta Q określonego ciągiem punktów. Zakładamy przy tym,
# że wielokąt jest wielokątem zwykłym, co oznacza, że jego boki się nie przecinają.
# Rysunek 8. Możliwe przypadki położenia punktu względem wielokąta
# Najbardziej znanymi algorytmami sprawdzania położenia punktu względem wielokąta są:
# algorytm sumy kątów oraz algorytm parzystości. Wymienione algorytmy różnią się między sobą
# dosyć znacznie. W obydwu przypadkach jednak badanie powinno się rozpoczynać od określenia
# położenia względem prostokąta ograniczającego. Wystarczy bowiem, że punkt leży poza tym
# prostokątem aby stwierdzić, że leży również poza wielokątem.
# Rysunek 9. Wstępne badanie położenia punktu wewnątrz wielokąta
# Warunkiem koniecznym, położenia punktu wewnątrz wielokąta jest jego położenie wewnątrz
# prostokąta ograniczającego, ale nie jest to warunek wystarczający, co widać na przykładzie
# punktu A, przedstawionego na powyższym rysunku.
# 9
# 4.1 ALGORYTM SUMY KĄTÓW
# Algorytm sumy kątów wykorzystuje, do ustalenia położenia punktu względem wielokąta, sumę
# kątów pomiędzy półprostymi poprowadzonymi z badanego punktu P przez wierzchołki wielokąta
# Pi. Obliczaną sumę kątów możemy zapisać jako:S i
# i
# n
# = =
# 
# 
# 1
# gdzie
# i jest kątem między półprostymi PPi a PPi+1.a) b)
# 4
# P
# 3
# P
# 1
# P 2
# P
# 6
# P 5P
# P
# P
# 3
# P
# 4
# P
# 6
# P
# 5P
# 1
# P 2
# P
# Rysunek 10. Testowanie położenia punktu względem wielokąta algorytmem sumy kątów: a) punkt wewnątrz wielokąta; b) punkt na
# zewnątrz wielokąta
# Jeśli punkt znajduje się wewnątrz wielokąta wtedy S=360 (rys. 10a) w przeciwnym wypadku
# S=0 (rys. 10b). Oczywiście podane wartości sumy kątów należy sprawdzać w pewnym przedziale
# dokładności numerycznej . Obliczane kąty
# i traktujemy jako dodatnie, jeśli uporządkowanie
# ramion jest zgodne z ruchem wskazówek zegara i jako ujemne jeśli jest kierunek uporządkowania
# jest przeciwny do ruchu wskazówek zegara.
# 4.2 ALGORYTM PARZYSTOŚCI
# Algorytm parzystości opiera się na założeniu, że jeżeli przyjmiemy dowolny punkt (Z) leżący na
# zewnątrz wielokąta i poprowadzimy od niego odcinek do punktu badanego (takiego, którego
# położenie względem wielokąta wyznaczamy) to zachodzą następujące przypadki:
# ▪ jeżeli punkt badany (A) leży wewnątrz wielokąta, to wtedy odcinek łączący te punkty przecina
# boki wielokąta nieparzystą liczbę razy,
# ▪ jeżeli punkt badany (B) leży na zewnątrz wielokąta odcinek łączący punkty albo nie przecina
# żadnego boku, albo przecina je parzystą liczbę boków.
# 10
# Ilustrację graficzna algorytmu parzystości przedstawiona jest na poniższym rysunku 11.punkt
# zewnętrzny Z
# punkt
# badany B
# punkt
# badany A
# Rysunek 11. Ogólna zasada działania algorytmu parzystości
# Praktyczne zastosowanie algorytmu będzie różniło się od przypadku ogólnego przedstawionego
# na rys. 11. Zalecane jest, aby badając położenie punktu przyjmować punkt o znanym położeniu (na
# zewnątrz wielokąta), tak aby odcinek był równoległy do jednej z osi układu współrzędnych, co
# znacznie skróci proces obliczania przecięć. Przyjmując zasadę, badania liczby przecięć wielokąta
# z odcinkiem równoległym do osi X, zwanym dalej odcinkiem pionowym (określonym punktem
# zewnętrznym położonym poza prostokątem zawierającym wielokąt i punktem badanym) mamy
# sytuację przedstawioną na rys. 12. W przypadku wystąpienia nieparzystej liczby przecięć
# stwierdzamy, że badany punkt leży wewnątrz wielokąta (punkt A na rys.12). Jeżeli liczba przecięć
# będzie parzysta (punkt B) lub jeśli przecięcia w ogóle nie wystąpią (punkt C) wtedy punkt leży na
# zewnątrz.A
# B
# C
# GF
# D
# E
# H
# Rysunek 12. Zasada działania algorytmu parzystości z odcinkiem pionowym
# Działanie algorytmu jest poprawne dla wszystkich punktów położonych wewnątrz i na zewnątrz
# wielokąta z wyjątkiem punktów pokrywających się z wierzchołkami wielokąta (punkt D i H) oraz
# w przypadku, kiedy odcinek przechodzi przez wierzchołki (punkt E i F) lub pokrywa się z jednym
# z boków wielokąta (punkt G).
# 11
# W przypadku pokrywania się badanego punktu z wierzchołkiem wielokąta należy postępowanie
# identyczne jak w algorytmie sumy kątów, polegające na porównywaniu współrzędnych kolejnych
# wierzchołków ze współrzędnymi badanego punktu. Przez opisane postępowanie wyeliminujemy
# wszystkie przypadki analogiczne do punktu D i H.
# Opisany powyżej przypadek jest jednak tylko jednym z przypadków szczególnych występujących
# w niniejszym algorytmie. Generalnie przypadki takie mają miejsce, kiedy odcinek pionowy
# poprowadzony przez badany punkt przechodzi przez wierzchołek wielokąta. Pojawia się wtedy
# problem, czy przecięcia liczyć, jako jednokrotne czy dwukrotne. W przypadku punktu E, aby
# algorytm dał poprawny wynik należy przecięcie potraktować, jako jednokrotne, natomiast
# w przypadku punktu F należy przecięcie traktować, jako dwukrotne. Problem rozwiązujemy przez
# przyjęcie następującej zasady. Jeżeli oba przecinane odcinki położone są po tej samej stronie
# odcinka pionowego, wtedy przecięcia traktujemy, jako dwukrotne, w przeciwnym wypadku, jako
# jednokrotne. Pozostaje jednak jeszcze inny szczególny przypadek, kiedy odcinek pionowy
# przechodzi przez jeden z boków wielokąta (punkt G).G
# Rysunek 13. Analiza przypadku szczególnego
# W takiej sytuacji mamy również, przy punkcie położonym wewnątrz, parzystą liczbę przecięć,
# a powinniśmy otrzymać liczbę nieparzystą. Rozwiązanie takiego przypadku jest możliwe, jeśli
# potraktujemy taki odcinek, jako pseudowierzchołek i zastosujemy do niego opisany wyżej sposób
# ustalania liczby przecięć. Wprowadzone dodatkowe sprawdzenia sprawiają również, że algorytm
# staje się odporny na przypadek, kiedy badany punkt pokrywa się z wierzchołkiem wielokąta. Jest
# tak w przypadku, kiedy oba wychodzące z tego wierzchołka boki leżą po różnych stronach odcinka
# testującego, gdyż wtedy przecięcie traktowane jest, jako jednokrotne. W przypadku, kiedy będzie
# inaczej algorytm daje zły wynik ponieważ przecięcie traktowane jest jako dwukrotne, a punkt
# przecież leży wewnątrz. Dlatego też również w tym algorytmie nie można uniknąć bezpośredniego
# sprawdzania, czy punkt nie pokrywa się z wierzchołkiem wielokąta.
# 12
# Na zakończenie należy zwrócić uwagę na fakt, że istotna jest w nim jedynie liczba występujących
# przecięć, a nie same wartości współrzędnych punktów przecięcia. Aby ustalić liczbę przecięć nie
# zawsze musimy korzystać ze stwierdzania ich istnienia w drodze wyznaczania punktu przecięcia
# dwóch odcinków. Są takie przypadki położenia boków wielokąta, w których istnienie lub brak
# przecięcia można stwierdzić badając jedynie proste warunki. Jest to znacznie korzystniejsze
# czasowo niż wykonywanie obliczeń. Sposób postępowania w niniejszym algorytmie, pozwalający
# uniknąć obliczania niektórych przecięć może być następujący:
# a) jeśli oba punkty boku leżą w po tej samej stronie odcinka pionowego wtedy bok nie przecina
# się z tym odcinkiem (boki na rys. 13a) i można przejść do analizy następnego boku,
# w przeciwnym wypadku sprawdzić następny warunek przedstawiony w punkcie b,
# b) jeśli oba punkty boku leżą poniżej punktu, którego położenie badamy wtedy bok również nie
# przecina się odcinkiem pionowym (rys. 13b) i można przejść do analizy następnego boku,
# w przeciwnym wypadku należy przejść do punktu c,
# c) jeśli oba punkty leżą powyżej punktu sprawdzanego wtedy stwierdzamy istnienie przecięcia
# bez obliczań (boki na rys. 13c) i przechodzimy do analizy następnego boku, w przeciwnym
# wypadku przechodzimy do punktu d,
# d) konieczne jest stwierdzenie istnienie przecięcia przez obliczenie (boki na rys. 13d).P
# a)
# P
# b)
# P
# c)
# P
# d)
# Rysunek 14. Ilustracja szczególnych położeń boków wielokąta w stosunku do odcinka pionowego
# Jak widzimy przedstawiony sposób postępowania zdecydowanie ogranicza liczbę boków
# wielokąta, dla których w drodze obliczeń należy sprawdzać istnienie przecięcia z odcinkiem
# pionowym. Konieczność taka będzie występowała jedynie dla boków o położeniu schematycznie
# przedstawionym na rys. 13d.
# 13
# 4.3 REALIZACJA ZADANIA
# Należy przygotować program komputerowy w dowolnym środowisku programowania z
# zaimplementowanym jednym z algorytmów. Program powinien umożliwiać:
# 1. wczytanie wielokąta z pliku tekstowego,
# 2. przedstawić graficznie wczytany wielokąt,
# 3. sprawdzać położenie podawanych z klawiatury punktów i wizualizować je graficznie na tle
# wielokąta,
# 4. na podstawie pliku punktów z sprawdzić, ile punktów znajduje się wewnątrz wielokąta,
# 5. powinna istnieć możliwość konfigurowania parametrów rysunku, tzn.: kolory, grubości i style
# linii,
# Przykładowe dane do obliczeń znajdują sie na stronie www.izdebski.edu.pl. Czas na wykonanie
# ćwiczenia: 3 zajęcia. Program powinien być oddany na koniec dziewiątych zajęć, w przypadku
# nieoddania wystawiana jest ocena negatywna.

import matplotlib.pyplot as plt
import PySimpleGUI as sg
import os
import itertools
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

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

# wczytanie wielokąta z pliku
def wczytaj_wielokat(sciezka: str) -> list[tuple]:
    """Wczytuje wielokąt z pliku.

    Args:
        sciezka (str): Ścieżka do pliku.

    Returns:
        list[tuple]: Wielokąt w postaci listy krotek.
    """
    # inicjalizacja listy przechowującej wierzchołki wielokąta
    wielokat = []
    
    # otwarcie pliku
    try:
        with open(sciezka, 'r') as f:
            # iteracja po liniach pliku
            for line in f:
                # podział linii na współrzędne
                x, y = line.split()
                # dodanie wierzchołka do wielokąta
                try:
                    wielokat.append((float(x), float(y)))
                except ValueError:
                    sg.popup_error('Plik zawiera niepoprawne dane!')
                    return []
    except FileNotFoundError:
        sg.popup_error('Nie znaleziono pliku!')
        return []
    
    # zwrócenie wielokąta
    return wielokat

def ile_puktow_wewnatrz(wielokat: list[tuple], plik) -> int:
    """Zlicza ile punktów z pliku jest wewnątrz wielokąta.

    Args:
        wielokat (list[tuple]): Wielokąt w postaci listy krotek.
        plik ([type]): Plik z punktami.

    Returns:
        int: Liczba punktów wewnątrz wielokąta.
    """
    # inicjalizacja licznika punktów wewnątrz wielokąta
    liczba_punktow = 0
    
    for line in plik:
        # podział linii na współrzędne
        x, y = line.split()
        # sprawdzenie czy punkt jest wewnątrz wielokąta
        try:
            if wewnatrz(wielokat, (float(x), float(y))):
                liczba_punktow += 1
        except ValueError:
            sg.popup_error('Plik zawiera niepoprawne dane!')
            return 0
    
    # zwrócenie liczby punktów wewnątrz wielokąta
    return liczba_punktow


punkt = sg.Frame('Punkt', [
    [sg.Text('x:'), sg.Input(key='x')],
    [sg.Text('y:'), sg.Input(key='y')]
])

default_width = 2
default_style = '-'
default_color = 'magenta'

default_inside_color = 'green'
default_outside_color = 'red'

line_width_combo = sg.Combo(list(range(1, 11)), default_value=default_width, key='line_width')
line_style_combo = sg.Combo(['-', '--', '-.', ':'], default_value=default_style, key='line_style')
line_color_combo = sg.Combo(['blue', 'green', 'red', 'cyan', 'magenta', 'yellow', 'black'], default_value=default_color, key='line_color')

punkt_inside_color_combo = sg.Combo(['blue', 'green', 'red', 'cyan', 'magenta', 'yellow', 'black'], default_value=default_inside_color, key='punkt_inside_color')
punkt_outside_color_combo = sg.Combo(['blue', 'green', 'red', 'cyan', 'magenta', 'yellow', 'black'], default_value=default_outside_color, key='punkt_outside_color')

layout = [
    [sg.Graph(canvas_size=(800, 800), graph_bottom_left=(0, 0), graph_top_right=(100, 100), key='graph')],
    [sg.Input(key='wielokat'), sg.FileBrowse('Wybierz plik z wielokatem'), sg.Button('Wczytaj wielokat', key='W')],
    [sg.Input(key='punkty'), sg.FileBrowse('Wybierz plik z punktami')],
    [sg.Button('Oblicz ile punktow wewnatrz wielokata', key='P'), sg.Text('Liczba punktow:'), sg.Text('0', key='punkty_wewnatrz')],
    [sg.Text('Grubosc linii:'), line_width_combo, sg.Text('Styl linii:'), line_style_combo, sg.Text('Kolor linii:'), line_color_combo],
    # punkt input
    [sg.Text('Podaj wspolzedne punktu:'), punkt, sg.Button('Dodaj punkt do wykresu')],
    [sg.Text('Kolor punktu wewnatrz:'), punkt_inside_color_combo, sg.Text('Kolor punktu na zewnatrz:'), punkt_outside_color_combo],
    [sg.Button('Odswiez')]
]

window = sg.Window('Zadanie 3', layout, finalize=True)

fig, ax = plt.subplots()

canvas = FigureCanvasTkAgg(fig, master=window['graph'].TKCanvas)
plot_widget = canvas.get_tk_widget()
plot_widget.grid(row=0, column=0)
ax.set_xlabel('x')
ax.set_ylabel('y')
fig.canvas.draw()

def redraw() -> None:
    ax.clear()
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    if wielokat:
        ax.plot(*zip(*itertools.chain(wielokat, [wielokat[0]])),
                color=wielokat_color, linewidth=wielokat_line_width, linestyle=wielokat_line_style)
    for p in punkty:
        if wewnatrz(wielokat, p):
            ax.scatter(*p, color=punkt_inside_color)
        else:
            ax.scatter(*p, color=punkt_outside_color)
    fig.canvas.draw()

file_path: str = ''
wielokat: list[tuple] = []
wielokat_color = default_color
wielokat_line_width = default_width
wielokat_line_style = default_style
punkty: set[tuple] = set()
punkt_inside_color = default_inside_color
punkt_outside_color = default_outside_color


while True:
    event, values = window.read()
    
    # combo events
    if values['line_width'] != wielokat_line_width:
        wielokat_line_width = values['line_width']
    if values['line_style'] != wielokat_line_style:
        wielokat_line_style = values['line_style']
    if values['line_color'] != wielokat_color:
        wielokat_color = values['line_color']
    if values['punkt_inside_color'] != punkt_inside_color:
        punkt_inside_color = values['punkt_inside_color']
    if values['punkt_outside_color'] != punkt_outside_color:
        punkt_outside_color = values['punkt_outside_color']

    if event == sg.WIN_CLOSED:
        break
    
    elif event == 'W':
        file_path = values['wielokat']
        if file_path == '':
            wielokat = []
            ax.clear()
            ax.set_xlabel('x')
            ax.set_ylabel('y')
            fig.canvas.draw()
            continue
        wielokat = wczytaj_wielokat(file_path)
        punkty = set()
        redraw()
    
    elif event == 'Dodaj punkt':
        # chekc if the point is correct
        try:
            x = float(values['x'])
            y = float(values['y'])
        except ValueError:
            sg.popup_error('Podano niepoprawne wspolrzedne punktu!')
            continue
        punkty.add((x, y))
        redraw()
    
    elif event == 'P':
        # check if a polygon has been loaded
        if wielokat == []:
            sg.popup_error('Nie wczytano wielokata!')
            continue
        # check if a file with points has been loaded
        if values['punkty'] == '':
            sg.popup_error('Nie wybrano pliku z punktami!')
            continue
        # check if the file with points exists
        try:
            with open(values['punkty'], 'r') as f:
                punkty_wewnatrz = ile_puktow_wewnatrz(wielokat, f)
                window['punkty_wewnatrz'].update(punkty_wewnatrz)
        except FileNotFoundError:
            sg.popup_error('Nie znaleziono pliku!')
            continue
                
    
    if event in ['line_width', 'line_style', 'line_color', 'punkt_inside_color', 'punkt_outside_color', 'Odswiez']:
        redraw()
