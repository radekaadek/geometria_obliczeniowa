import matplotlib.pyplot as plt
import PySimpleGUI as sg
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
    [sg.Text('Podaj wspolzedne punktu:'), punkt, sg.Button('Dodaj punkt do wykresu', key='Dodaj punkt')],
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
