import matplotlib.pyplot as plt
import PySimpleGUI as sg
import itertools
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

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
    except UnicodeDecodeError:
        sg.popup_error('Plik nie jest tekstem!')
        return []
    
    # zwrócenie wielokąta
    return wielokat

def punkty_wewnatrz(wielokat: list[tuple], plik) -> list[tuple]:
    """Zlicza ile punktów z pliku jest wewnątrz wielokąta.

    Args:
        wielokat (list[tuple]): Wielokąt w postaci listy krotek.
        plik ([type]): Plik z punktami.

    Returns:
        int: Liczba punktów wewnątrz wielokąta.
    """
    # inicjalizacja licznika punktów wewnątrz wielokąta
    punkty = []
    
    for line in plik:
        # podział linii na współrzędne
        x, y = line.split()
        try:
            xf = float(x)
            yf = float(y)
        except ValueError:
            sg.popup_error('Plik zawiera niepoprawne dane!')
            return []
        if wewnatrz(wielokat, (xf, yf)):
            punkty.append((xf, yf))
    
    # zwrócenie liczby punktów wewnątrz wielokąta
    return punkty


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
    [sg.In("", visible=False, enable_events=True, key='wielokat'), wybierz_wielokat,
     sg.In("", visible=False, enable_events=True, key='punkty'), wybierz_punkty],
    [sg.Text('Liczba punktow wewnatrz:'), sg.Text('0', key='punkty_wewnatrz')],
    [sg.Text('Grubosc linii:'), line_width_combo, sg.Text('Styl linii:'), line_style_combo,
     sg.In("", visible=False, enable_events=True, key='line_color'), line_color_combo],
    # punkt input
    [sg.Text('Podaj wspolzedne punktu:'), punkt_frame, sg.Button('Dodaj punkt', key='Dodaj punkt')],
    [sg.In("", visible=False, enable_events=True, key='punkt_inside_color'), in_col_comb,
     sg.In("", visible=False, enable_events=True, key='punkt_outside_color'), out_col_comb],
    [sg.Button('Odswiez')]
]

# show window in the middle of the screen
window = sg.Window('Zadanie 3', layout, finalize=True, location=(0, 0))

fig, ax = plt.subplots()

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
    if wielokat:
        if wielokat[-1] != wielokat[0]:
            wielokat.append(wielokat[0])
        ax.plot(*zip(*wielokat), color=wielokat_color, linewidth=wielokat_line_width, linestyle=wielokat_line_style)
    if punkty:
        for p in punkty:
            if wewnatrz(wielokat, p):
                ax.scatter(*p, color=punkt_inside_color)
            else:
                ax.scatter(*p, color=punkt_outside_color)
    elif punkt:
        if wewnatrz(wielokat, punkt):
            ax.scatter(*punkt, color=punkt_inside_color)
        else:
            ax.scatter(*punkt, color=punkt_outside_color)
    fig.canvas.draw()

redraw()

while True:
    event, values = window.read()
    
    if event == sg.WIN_CLOSED:
        break
    
    # combo events
    elif event == 'line_width':
        wielokat_line_width = values['line_width']
    elif event == 'line_style':
        wielokat_line_style = values['line_style']
    elif event == 'line_color':
        wielokat_color = values['line_color']
    elif event == 'punkt_inside_color':
        punkt_inside_color = values['punkt_inside_color']
    elif event == 'punkt_outside_color':
        punkt_outside_color = values['punkt_outside_color']
    
    elif event == 'Dodaj punkt':
        # check if the point is correct
        try:
            x = float(values['x'])
            y = float(values['y'])
        except ValueError:
            sg.popup_error('Podano niepoprawne wspolrzedne punktu!')
            continue
        punkt = (x, y)
        if not wielokat:
            sg.popup_error('Nie wprowadzono wielokata!')
        if wewnatrz(wielokat, punkt):
            sg.popup_ok('Punkt znajduje sie wewnatrz wielokata!', title='Punkt wewnatrz')
        else:
            sg.popup_ok('Punkt znajduje sie na zewnatrz wielokata!', title='Punkt na zewnatrz')
        # set liczba punktow wewnatrz to 0
        window['punkty_wewnatrz'].update(0)
        punkty = set()
    
    elif event == 'punkty':
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
                punkty_w = punkty_wewnatrz(wielokat, f)
                window['punkty_wewnatrz'].update(len(punkty_w))
        except FileNotFoundError:
            sg.popup_error('Nie znaleziono pliku!')
            continue
        finally:
            punkty = set(punkty_w)

    elif event == 'wielokat':
        file_path = values['wielokat']
        if file_path == '':
            wielokat = []
            ax.clear()
            ax.set_xlabel('x')
            ax.set_ylabel('y')
            fig.canvas.draw()
            continue
        wielokat = wczytaj_wielokat(file_path)
        punkt = None
        punkty = set()

    redraw()