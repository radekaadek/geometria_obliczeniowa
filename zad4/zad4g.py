import time
import matplotlib.pyplot as plt
import PySimpleGUI as sg
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


#  WYZNACZENIE OTOCZKI WYPUKŁEJ ZBIORU PUNKTÓW
# Określenie otoczki wypukłej zbioru punktów jest jednym z podstawowych zadań geometrii
# obliczeniowej. Zadanie polega na znalezieniu najmniejszego wielokąta P ograniczającego zbiór
# punktów Q takiego, że każdy z punktów leży na brzegu P, albo w jego wnętrzu. Wypukłą otoczkę
# zbioru oznaczamy przez CH(Q) (skrót od angielskiego convex hull). Odwołując się do intuicji, zbiór
# punktów możemy wyobrazić sobie jako gwoździe wystające z deski. Na gwoździe zakładamy gumkę,
# która przybierze kształt wypukłej otoczki. Jest wiele algorytmów wyznaczania otoczki wypukłej.
# Poniżej przedstawiono dwa tj.: algorytm Grahama (1972) oraz Jarvisa (1973). Cechą wspólną
# algorytmów jest zastosowanie metoda zwanej „zamiataniem obrotowym”, polegającym na
# przetwarzaniu wierzchołków w kolejności występowania kątów, jakie tworzą z ustalonym punktem
# i przechodzącym przez niego osią.
# Rysunek 15. Obraz otoczki wypukłej P zbioru punktów Q
# 5.1 ALGORYTM GRAHAMA
# W algorytmie Grahama otoczka jest wyznaczana z wykorzystaniem stosu S, który zawiera
# kandydatów na wierzchołki otoczki. Każdy punkt będący kandydatem do punktu otoczki jest raz
# wkładany na stos, a jeśli w dalszej analizie okazuje się, że nie spełnia odpowiednich warunków jest
# z niego zdejmowany. Po zakończeniu działania algorytmu stos zawiera wyłącznie wierzchołki
# CH(Q). Kolejność czynności wykonywane w ramach algorytmu Grahama jest następująca:
# 1. ze zbioru Q (zawierającego n punktów) wyznaczamy punkt Po o minimalnym Y, jeśli takich punktów jest
# więcej przyjmujemy punkt o największym X,
# 2. sortujemy punkty ze względu na azymuty promieni łączących punkt Po z kolejnymi punktami zbioru Q,
# jeśli więcej niż jeden promień posiada identyczną wartość azymutu usuwamy wszystkie punkty oprócz
# położonego najdalej od Po (najdłuższym promieniu),
# 3. w rezultacie tej operacji pozostaje do rozważania m punktów (kandydatów), z tego ograniczonego zbioru
# punktów do otoczki na pewno należy punkt ostatni czyli Pm,
# 4. zerujemy stos S zapamiętujący punkty otoczki i wprowadzamy na stos punktu Po oraz P1 i P2,
# 5. od j w zakresie od 3 do m przeglądamy kolejne punkty w nawiązaniu do ostatnich dwóch punktów stosu
# S sprawdzając kierunek skrętu (wykorzystujemy własność iloczynu wektorowego), do chwili kiedy skręt
# w ostatnim wierzchołku na stosie do punktu Pj nie jest skrętem w prawo wtedy eliminujemy taki
# wierzchołek ze stosu dopiero przy skręcie w prawo dodajemy punkt Pj do stosu,
# 6. po przejrzeniu wszystkich punktów stos zawiera otoczkę wypukłą zbioru Q.
# Rysunek 16. Ilustracja tworzenia otoczki wypukłej metodą Grahama
# 16
# 5.2 ALGORYTM JARVISA
# W algorytmie Jarvisa wypukła otoczka zbioru punktów Q jest wyznaczana metodą zwaną
# owijaniem. Ujmując rzecz intuicyjne, algorytm Jarvisa naśladuje ciasne owijanie taśmy wokół
# punktów zbioru Q. Zaczynamy od zamocowania końca taśmy do położonego najbardziej z lewej
# strony punktu zbioru Q. Punkt ten oznaczamy jako Po. Punkt ten jest identyczny z punktem Po
# z algorytmu Grahama. Napinamy taśmę podnosząc ją do góry a następnie przesuwamy w prawo
# dopóki nie natrafimy na jakiś punkt. Punkt ten także musi należeć do otoczki. Tak więc trzymając
# cały czas napiętą taśmę wędrujemy naokoło zbioru, dopóki nie trafimy z powrotem do punktu
# początkowego. Formalnie rzecz biorąc postępowanie polega na tym, że zamiast napinania taśmy
# jako kolejny punkt otoczki bierzemy taki, który z jej punktem ostatnim daje promień wodzący
# o najmniejszej wartości azymutu. Postępowanie takie prowadzimy do chwili kiedy nie dotrzemy do
# wierzchołka położonego najbardziej z prawej strony. Po osiągnięciu tego punktu mamy
# skonstruowany łańcuch górny otoczki. Łańcuch dolny konstruujemy podobnie lecz zamiast wartości
# azymutu wykorzystujemy zawsze najmniejszą wartość kata utworzonego z ujemna półosią X.
# Rysunek 17. Ilustracja tworzenia otoczki wypukłej metodą Jarvisa
# 17
# W algorytmie niniejszym można zrezygnować z tworzenia osobnych łańcuchów górnego i dolnego
# ale wtedy należy operować wartością azymutu w zakresie od 0 do 2 co zmusza nas do jawnego
# obliczania jego wartości. Przy zastosowaniu podziału na łańcuchy możemy korzystać jedynie z
# iloczynu wektorowego zamiast z wartości azymutu.
# 5.3 REALIZACJA ZADANIA
# Należy przygotować program komputerowy w dowolnym środowisku programowania
# z zaimplementowanym jednym z algorytmów. Program powinien umożliwiać:
# 1. wczytanie wykazu punktów z pliku tekstowego,
# 2. możliwość dodania do wykazu punktów pojedynczego punktu z klawiatury
# 3. przedstawić graficznie wczytane do wykazu punkty z możliwością:
# a. wybór znaku prezentacji np. okrąg, kwadrat,
# b. możliwość opisania numerem punktu,
# c. zmiany koloru znaku prezentacji,
# d. zmiany wielkości znaku prezentacji,
# 4. przedstawić graficznie prostokąt ograniczający wykaz punktów z możliwością
# a. wyboru kolory linii prostokąta,
# b. wyboru grubości linii prostokąta,
# c. wyboru stylu linii prostokąta,
# 5. na podstawie zbioru punktów zbudować otoczkę wypukłą,
# 6. przedstawić graficznie otoczką z możliwością
# a. wyboru kolory linii otoczki
# b. wyboru grubości linii otoczki
# c. wyboru stylu linii otoczki
# 7. zapisanie punktów otoczki do pliku tekstowego
# Przykładowe dane do obliczeń znajdują się na stronie www.izdebski.edu.pl. Program powinien
# być oddany na koniec czternastych zajęć, w przypadku nieoddania wystawiana jest ocena
# negatywna.

fig, ax = plt.subplots()

def azymut(p1: tuple, p2: tuple) -> float:
    """Oblicza azymut do północy promienia łączącego dwa punkty.

    Args:
        p1 (tuple): Pierwszy punkt. (x, y)
        p2 (tuple): Drugi punkt. (x, y)

    Returns:
        float: Dodatni azymut w radianach.
    """
    delta_x = p2[0] - p1[0]
    delta_y = p2[1] - p1[1]
    azymut_rad = np.arctan2(delta_y, delta_x)
    
    # Zamień azymut na zakres od 0 do 2*pi
    azymut_rad = (azymut_rad + 2 * np.pi) % (2 * np.pi)
    return azymut_rad

def graham(Q: list[tuple]) -> list[tuple]:
    """Zwraca otoczkę wypukłą zbioru punktów.

    Args:
        points (list[tuple]): Zbiór punktów.

    Returns:
        list[tuple]: Otoczka wypukła zbioru punktów.
    """
    # 1. ze zbioru Q (zawierającego n punktów) wyznaczamy punkt Po o minimalnym Y, jeśli takich punktów jest
    # więcej przyjmujemy punkt o największym X,
    Po = min(Q, key=lambda x: (x[1], -x[0]))
    # 2. sortujemy punkty ze względu na azymuty promieni łączących punkt Po z kolejnymi punktami zbioru Q,
    # jeśli więcej niż jeden promień posiada identyczną wartość azymutu usuwamy wszystkie punkty oprócz
    # położonego najdalej od Po (najdłuższym promieniu),
    Q = sorted(Q, key=lambda x: azymut(Po, x))
    # 3. w rezultacie tej operacji pozostaje do rozważania m punktów (kandydatów), z tego ograniczonego zbioru
    # punktów do otoczki na pewno należy punkt ostatni czyli Pm,
    m = len(Q)
    # 4. zerujemy stos S zapamiętujący punkty otoczki i wprowadzamy na stos punktu Po oraz P1 i P2,
    S = [Po, Q[0], Q[1]]
    # 5. od j w zakresie od 3 do m przeglądamy kolejne punkty w nawiązaniu do ostatnich dwóch punktów stosu
    # S sprawdzając kierunek skrętu (wykorzystujemy własność iloczynu wektorowego), do chwili kiedy skręt
    # w ostatnim wierzchołku na stosie do punktu Pj nie jest skrętem w prawo wtedy eliminujemy taki
    # wierzchołek ze stosu dopiero przy skręcie w prawo dodajemy punkt Pj do stosu,
    for j in range(2, m):
        while len(S) > 1 and np.cross(np.array(S[-1]) - np.array(S[-2]), np.array(Q[j]) - np.array(S[-2])) <= 0:
            S.pop()
        S.append(Q[j])
    # 6. po przejrzeniu wszystkich punktów stos zawiera otoczkę wypukłą zbioru Q.
    return S


        

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
                try:
                    x, y = line.split()
                except ValueError:
                    sg.popup_error('Plik zawiera niepoprawne dane!')
                    return []
                # dodanie wierzchołka do wielokąta
                try:
                    wielokat.append((float(y), float(x)))
                except ValueError:
                    sg.popup_error('Plik zawiera niepoprawne dane!')
                    return []
    except FileNotFoundError:
        sg.popup_error('Nie znaleziono pliku!')
        return []
    except UnicodeDecodeError:
        sg.popup_error('Plik nie jest tekstem!')
        return []
    
    # zwrócenie wielokąta
    return wielokat


punkt_frame: sg.Frame = sg.Frame('Punkt', [
    [sg.Text('x:'), sg.Input(key='x')],
    [sg.Text('y:'), sg.Input(key='y')]
])

default_width: int = 2
default_style: str = '-'
default_color: str = 'magenta'

default_inside_color: str = 'green'
default_outside_color: str = 'red'

line_width_combo = sg.Combo(list(range(1, 11)), default_value=default_width, key='line_width', enable_events=True)
line_style_combo = sg.Combo(['-', '--', '-.', ':'], default_value=default_style, key='line_style', enable_events=True)
line_color_combo = sg.ColorChooserButton('Wybierz kolor linii', key='line_color')

in_col_comb = sg.ColorChooserButton('Wybierz kolor punktu wewnatrz', key='punkt_inside_color')
out_col_comb = sg.ColorChooserButton('Wybierz kolor punktu na zewnatrz', key='punkt_outside_color')
# przycisk - file dialog
wybierz_wielokat = sg.FileBrowse('Wybierz wielokat', enable_events=True, key='wielokat')
wybierz_punkty = sg.FileBrowse('Wybierz plik z punktami', enable_events=True, key='punkty')

layout = [
    [sg.Graph(canvas_size=(800, 800), graph_bottom_left=(0, 0), graph_top_right=(100, 100), key='graph')],
    [sg.In("", visible=False, enable_events=True, key='punkty'), wybierz_punkty,
     sg.Button('Narysuj otoczke', key='Narysuj otoczke')],
    [sg.Text('Grubosc linii:'), line_width_combo, sg.Text('Styl linii:'), line_style_combo,
     sg.In("", visible=False, enable_events=True, key='line_color'), line_color_combo],
    # punkt input
    [sg.Text('Podaj wspolzedne punktu:'), punkt_frame, sg.Button('Dodaj punkt', key='Dodaj punkt')],
    [sg.In("", visible=False, enable_events=True, key='punkt_inside_color'), in_col_comb,
     sg.In("", visible=False, enable_events=True, key='punkt_outside_color'), out_col_comb]
]

# show window in the middle of the screen
window = sg.Window('Zadanie 3', layout, finalize=True, location=(0, 0))

canvas = FigureCanvasTkAgg(fig, master=window['graph'].TKCanvas)
plot_widget = canvas.get_tk_widget()
plot_widget.grid(row=0, column=0)


file_path: str = ''
wielokat: list[tuple] = []
wielokat_color = default_color
wielokat_line_width = default_width
wielokat_line_style = default_style
punkty: set[tuple] = set()
punkt: tuple = ()
punkt_inside_color = default_inside_color
punkt_outside_color = default_outside_color

def redraw() -> None:
    ax.clear()
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_aspect('equal', adjustable='box')
    if punkty:
        ax.scatter(*zip(*punkty), c=punkt_inside_color)
    if wielokat:
        ax.plot(*zip(*wielokat), c=wielokat_color, lw=wielokat_line_width, ls=wielokat_line_style)
    fig.canvas.draw()

redraw()

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    elif event == 'punkty':
        file_path = values['punkty']
        punkty = set(wczytaj_wielokat(file_path))
        redraw()
    elif event == 'Narysuj otoczke':
        if not punkty:
            sg.popup_error('Nie wczytano punktów!')
            continue
        wielokat = graham(list(punkty))
        redraw()

    redraw()