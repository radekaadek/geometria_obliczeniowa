import matplotlib.pyplot as plt
import PySimpleGUI as sg
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

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
    return S + [Po]


        

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

styl_lini = {
    # po polsku
    'kropkowa': ':',
    'kreskowa': '--',
    'kreskowo-kropkowa': '-.',
    'ciagla': '-'
}

punkt_frame: sg.Frame = sg.Frame('Punkt', [
    [sg.Text('x:'), sg.Input(key='x')],
    [sg.Text('y:'), sg.Input(key='y')]
])

default_width: int = 2
default_style: str = 'kreskowa'
default_color: str = 'magenta'

default_border_width: int = 1
default_border_style: str = 'kropkowa'
default_border_color: str = 'black'

default_pt_color: str = 'green'

line_width_combo = sg.Combo(list(range(1, 11)), default_value=default_width, key='line_width', enable_events=True)
line_style_combo = sg.Combo(list(styl_lini.keys()), default_value=default_style, key='line_style', enable_events=True)
line_color_combo = sg.ColorChooserButton('Wybierz kolor linii', key='line_color')

col_comb = sg.ColorChooserButton('Wybierz kolor punktu', key='punkt_inside_color')
# przycisk - file dialog
wybierz_punkty = sg.FileBrowse('Wybierz plik z punktami', enable_events=True, key='punkty')

layout = [
    [sg.Graph(canvas_size=(800, 800), graph_bottom_left=(0, 0), graph_top_right=(100, 100), key='graph')],
    [sg.In("", visible=False, enable_events=True, key='punkty'), wybierz_punkty,
     sg.Button('Narysuj otoczke', key='Narysuj otoczke')],
    [sg.Text('Grubosc linii:'), line_width_combo, sg.Text('Styl linii:'), line_style_combo,
     sg.In("", visible=False, enable_events=True, key='line_color'), line_color_combo],
    #  to samo dla prostokąta
    [sg.Text('Grubosc linii prostokata:'), sg.Combo(list(range(1, 11)), default_value=default_border_width, key='border_width', enable_events=True),
        sg.Text('Styl linii prostokata:'), sg.Combo(list(styl_lini.keys()), default_value=default_border_style, key='border_style', enable_events=True),
        sg.In("", visible=False, enable_events=True, key='border_color'), sg.ColorChooserButton('Wybierz kolor linii prostokata', key='border_color')],
    [sg.Text('Podaj wspolzedne punktu:'), punkt_frame, sg.Button('Dodaj punkt', key='Dodaj punkt')],
    [sg.In("", visible=False, enable_events=True, key='punkt_color'), col_comb]
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
border_color = default_border_color
border_width = default_border_width
border_style = default_border_style
punkty: list[tuple] = []
punkt: tuple = ()
punkt_color = default_pt_color

def redraw() -> None:
    ax.clear()
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_aspect('equal', adjustable='box')
    if punkty:
        ax.scatter(*zip(*punkty), c=punkt_color)
        # narysuj prostokąt ograniczający
        min_x = min(punkty, key=lambda x: x[0])[0]
        max_x = max(punkty, key=lambda x: x[0])[0]
        min_y = min(punkty, key=lambda x: x[1])[1]
        max_y = max(punkty, key=lambda x: x[1])[1]
        ax.plot([min_x, max_x, max_x, min_x, min_x], [min_y, min_y, max_y, max_y, min_y], c=border_color, lw=border_width, ls=styl_lini[border_style])
    if wielokat:
        ax.plot(*zip(*wielokat), c=wielokat_color, lw=wielokat_line_width, ls=styl_lini[wielokat_line_style])
    fig.canvas.draw()

redraw()

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    elif event == 'punkty':
        file_path = values['punkty']
        punkty = wczytaj_wielokat(file_path)
        wielokat = []
    elif event == 'Narysuj otoczke':
        if not punkty:
            sg.popup_error('Nie wczytano punktów!')
            continue
        wielokat = graham(punkty)
    # grubosc linii
    elif event == 'line_width':
        wielokat_line_width = int(values['line_width'])
    # styl linii
    elif event == 'line_style':
        wielokat_line_style = values['line_style']
    # kolor linii
    elif event == 'line_color':
        wielokat_color = values['line_color']
    # dodaj punkt
    elif event == 'Dodaj punkt':
        try:
            punkt = (float(values['x']), float(values['y']))
        except ValueError:
            sg.popup_error('Podano niepoprawne współrzędne!')
            continue
        punkty.append(punkt)
        if wielokat:
            wielokat = graham(punkty)
    # kolor punktu
    elif event == 'punkt_color':
        punkt_color = values['punkt_color']
    # grubosc linii prostokata
    elif event == 'border_width':
        border_width = int(values['border_width'])
    # styl linii prostokata
    elif event == 'border_style':
        border_style = values['border_style']
    # kolor linii prostokata
    elif event == 'border_color':
        border_color = values['border_color']

    redraw()