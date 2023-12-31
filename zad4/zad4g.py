import matplotlib.pyplot as plt
import PySimpleGUI as sg
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from collections import deque

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

def skret(p1: tuple, p2: tuple, p3: tuple) -> float:
    """Oblicza skręt p1, p2, p3.

    Args:
        p1 (tuple): Pierwszy punkt. (x, y)
        p2 (tuple): Drugi punkt. (x, y)
        p3 (tuple): Trzeci punkt. (x, y)

    Returns:
        float: Skręt.
    """
    return np.cross(np.array(p2) - np.array(p1), np.array(p3) - np.array(p1))

def graham(Q: list[tuple]) -> list[tuple]:
    """Zwraca otoczkę wypukłą zbioru punktów.

    Args:
        points (list[tuple]): Zbiór punktów.

    Returns:
        list[tuple]: Otoczka wypukła zbioru punktów.
    """
    # 1. ze zbioru Q (zawierającego n punktów) wyznaczamy punkt Po o minimalnym Y, jeśli takich punktów jest
    # więcej przyjmujemy punkt o największym X,
    Po: tuple = min(Q, key=lambda x: (x[1], -x[0]))
    # 2. sortujemy punkty ze względu na azymuty promieni łączących punkt Po z kolejnymi punktami zbioru Q,
    # jeśli więcej niż jeden promień posiada identyczną wartość azymutu usuwamy wszystkie punkty oprócz
    # położonego najdalej od Po (najdłuższym promieniu),
    Q = sorted(Q, key=lambda x: azymut(Po, x))
    # 3. w rezultacie tej operacji pozostaje do rozważania m punktów (kandydatów), z tego ograniczonego zbioru
    # punktów do otoczki na pewno należy punkt ostatni czyli Pm,
    m: int = len(Q)
    # 4. zerujemy stos S zapamiętujący punkty otoczki i wprowadzamy na stos punktu Po oraz P1 i P2,
    s: deque[tuple] = deque([Po, Q[0], Q[1]])
    # 5. od j w zakresie od 3 do m przeglądamy kolejne punkty w nawiązaniu do ostatnich dwóch punktów stosu
    # S sprawdzając kierunek skrętu (wykorzystujemy własność iloczynu wektorowego), do chwili kiedy skręt
    # w ostatnim wierzchołku na stosie do punktu Pj nie jest skrętem w prawo wtedy eliminujemy taki
    # wierzchołek ze stosu dopiero przy skręcie w prawo dodajemy punkt Pj do stosu,
    for j in range(2, m):
        while len(s) > 1 and skret(s[-2], s[-1], Q[j]) <= 0:
            s.pop()
        s.append(Q[j])
    # 6. po przejrzeniu wszystkich punktów stos zawiera otoczkę wypukłą zbioru Q.
    return list(s) + [Po]


        

# wczytanie wielokąta z pliku
def wczytaj_wielokat(sciezka: str) -> list[tuple]:
    """Wczytuje wielokąt z pliku.

    Args:
        sciezka (str): Ścieżka do pliku.

    Returns:
        list[tuple]: Wielokąt w postaci listy krotek.
    """
    # inicjalizacja listy przechowującej wierzchołki wielokąta
    wielokat: list[tuple] = []
    
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
        sg.popup_error('Nie udalo sie zczytac pliku!')
        return []
    
    # zwrócenie wielokąta
    return wielokat

fig, ax = plt.subplots()

styl_lini: dict[str, str] = {
    # po polsku
    'linia kropkowa': ':',
    'linia kreskowa': '--',
    'linia kreskowo-kropkowa': '-.',
    'linia ciagla': '-'
}

styl_punktu: dict[str, str] = {
    # po polsku
    'kropka': '.',
    'plus': 'o',
    'x': 'x',
    'gwiazdka': '*',
    'kwadrat': 's',
    'trójkąt': '^',
    'diament': 'D',
    'pentagram': 'p',
    'hexagram': 'h'
}

punkt_frame: sg.Frame = sg.Frame('Punkt', [
    [sg.Text('x:'), sg.Input(key='x')],
    [sg.Text('y:'), sg.Input(key='y')]
])

default_marker: str = 'kropka'
default_marker_size: int = 50
default_marker_color: str = 'red'

default_width: int = 2
default_style: str = 'linia kreskowa'
default_color: str = 'magenta'

default_border_width: int = 1
default_border_style: str = 'linia kropkowa'
default_border_color: str = 'black'
ogranicz: bool = True
otoczk: bool = True
numeracja: bool = True

default_pt_color: str = 'green'

line_width_combo = sg.Combo(list(range(1, 11)), default_value=default_width, key='line_width', enable_events=True)
line_style_combo = sg.Combo(list(styl_lini.keys()), default_value=default_style, key='line_style', enable_events=True)
line_color_combo = sg.ColorChooserButton('Wybierz kolor linii', key='line_color')
prostokat_color_comb = sg.ColorChooserButton('Wybierz kolor linii prostokata', key='border_color')
col_comb = sg.ColorChooserButton('Wybierz kolor punktu', key='punkt_inside_color')
marker_color_comb = sg.ColorChooserButton('Wybierz kolor punktu', key='marker_color')
# przycisk - file dialog
wybierz_punkty = sg.FileBrowse('Wybierz plik z punktami', enable_events=True, key='punkty')

layout = [
    [sg.Graph(canvas_size=(800, 800), graph_bottom_left=(0, 0), graph_top_right=(100, 100), key='graph')],
    [sg.In("", visible=False, enable_events=True, key='punkty'), wybierz_punkty],
    [sg.Text('Znak punktu:'), sg.Combo(list(styl_punktu.keys()), default_value=default_marker, key='marker', enable_events=True),
        sg.Text('Rozmiar punktu:'), sg.Combo(list(range(10, 101, 10)), default_value=default_marker_size, key='marker_size', enable_events=True),
        sg.In("", visible=False, enable_events=True, key='marker_color'), marker_color_comb],
    [sg.Button('Oblicz otoczke', key='Oblicz otoczke'), sg.Text('Otoczka:'),
        sg.Button('On', size=(3, 1), button_color='white on green', key='-otczk-'), sg.Text('Numeracja punktow:'),
        sg.Button('On', size=(3, 1), button_color='white on green', key='-numeracja-')],
    [sg.Text('Grubosc linii otoczki:'), line_width_combo, sg.Text('Styl linii otoczki:'), line_style_combo,
        sg.In("", visible=False, enable_events=True, key='line_color'), line_color_combo],
    #  to samo dla prostokąta
    [sg.Text('Prostokat ograniczajacy:'), sg.Button('On', size=(3, 1), button_color='white on green', key='-B-')],
    [sg.Text('Grubosc linii prostokata:'), sg.Combo(list(range(1, 11)), default_value=default_border_width, key='border_width', enable_events=True),
        sg.Text('Styl linii prostokata:'), sg.Combo(list(styl_lini.keys()), default_value=default_border_style, key='border_style', enable_events=True),
        sg.In("", visible=False, enable_events=True, key='border_color'), prostokat_color_comb],
    [sg.Text('Podaj wspolzedne punktu:'), punkt_frame, sg.Button('Dodaj punkt', key='Dodaj punkt')]
]

# show window in the middle of the screen
window = sg.Window('Zadanie 4', layout, finalize=True, location=(0, 0))

canvas = FigureCanvasTkAgg(fig, master=window['graph'].TKCanvas)
plot_widget = canvas.get_tk_widget()
plot_widget.grid(row=0, column=0)


file_path: str = ''
wielokat: list[tuple] = []
wielokat_color: str = default_color
marker: str = default_marker
marker_size: int = default_marker_size
marker_color: str = default_marker_color
wielokat_line_width: int = default_width
wielokat_line_style: str = default_style
border_color: str = default_border_color
border_width: int = default_border_width
border_style: str = default_border_style
punkty: list[tuple] = []
punkt: tuple = ()

def redraw() -> None:
    ax.clear()
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_aspect('equal', adjustable='box')
    if punkty:
        ax.scatter(*zip(*punkty), c=marker_color, marker=styl_punktu[marker], s=marker_size)
        # add a number to the right bottom corner of each point
        if numeracja:
            for i, p in enumerate(punkty):
                ax.text(p[0], p[1], i+1, ha='left', va='bottom', fontsize=10)
        # narysuj prostokąt ograniczający
        if ogranicz:
            min_x = min(punkty, key=lambda x: x[0])[0]
            max_x = max(punkty, key=lambda x: x[0])[0]
            min_y = min(punkty, key=lambda x: x[1])[1]
            max_y = max(punkty, key=lambda x: x[1])[1]
            ax.plot([min_x, max_x, max_x, min_x, min_x], [min_y, min_y, max_y, max_y, min_y],
                    c=border_color, lw=border_width, ls=styl_lini[border_style])
    if wielokat:
        if otoczk:
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
    elif event == 'Oblicz otoczke':
        if not punkty:
            sg.popup_error('Nie wczytano punktów!')
            continue
        if len(punkty) < 2:
            sg.popup_error('Za mało punktów!')
            continue
        wielokat = graham(punkty)
    # styl punktu
    elif event == 'marker':
        marker = values['marker']
    # rozmiar punktu
    elif event == 'marker_size':
        marker_size = int(values['marker_size'])
    # kolor punktu
    elif event == 'marker_color':
        marker_color = values['marker_color']
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
    # grubosc linii prostokata
    elif event == 'border_width':
        border_width = int(values['border_width'])
    # styl linii prostokata
    elif event == 'border_style':
        border_style = values['border_style']
    # kolor linii prostokata
    elif event == 'border_color':
        border_color = values['border_color']
    elif event == '-B-':
        ogranicz = not ogranicz
        window['-B-'].update(text='On' if ogranicz else 'Off', button_color=('white on green' if ogranicz else 'white on red'))
    elif event == '-otczk-':
        otoczk = not otoczk
        window['-otczk-'].update(text='On' if otoczk else 'Off', button_color=('white on green' if otoczk else 'white on red'))
    elif event == '-numeracja-':
        numeracja = not numeracja
        window['-numeracja-'].update(text='On' if numeracja else 'Off', button_color=('white on green' if numeracja else 'white on red'))

    redraw()
