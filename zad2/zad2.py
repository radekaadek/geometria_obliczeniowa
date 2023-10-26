# 2 WYZNACZENIE PUNKTU PRZECIĘCIA DWÓCH ODCINKÓW
# Zadanie polega na napisaniu programu, który będzie wyznaczał punkt przecięcia dwóch
# odcinków, z których każdy jest dany przez współrzędne dwóch punktów. Ilustrację zadania
# przedstawia rys. 4.
# Rysunek 4. Ilustracja zadania przecięcia dwóch prostych określonych dwoma punktami
# 2.1 METODA ROZWIĄZANIA ZADANIA
# Z punktu widzenia wzorów rozwiązujących, to zadanie jest szczególnym przypadkiem
# ogólnego zadania polegającego na wyznaczeniu punktu przecięcia dwóch prostych. Do rozwiązania
# zadania wykorzystujemy równanie parametryczne prostej, w którym każdy punkt na prostej daje
# się wyrazić w funkcji punktu początkowego, końcowego i pewnego parametru rzeczywistego 𝑡.
# Parametryczne równanie prostej przechodzącej przez punkty A i B ma postać:
# 𝑋 = 𝑋𝐴 + 𝑡 ∗ 𝛥𝑋𝐴𝐵,
# 𝑌 = 𝑌𝐴 + 𝑡 ∗ 𝛥𝑌𝐴𝐵,
# gdzie 𝑡 ∈ (−∞, ∞). Przy czym na uwagę zasługuje fakt, że w punkcie A parametr 𝑡 = 0 natomiast
# w punkcie B parametr 𝑡 = 1. Rozwiązanie zadania możemy przedstawić następującymi wzorami:
# 𝑋𝑃 = 𝑋𝐴 + 𝑡1𝛥𝑋𝐴𝐵,
# 𝑌𝑃 = 𝑌𝐴 + 𝑡1𝛥𝑌𝐴𝐵
# lub 𝑋𝑃 = 𝑋𝐶 + 𝑡2𝛥𝑋𝐶𝐷,
# 𝑌𝑃 = 𝑌𝐶 + 𝑡2𝛥𝑌𝐶𝐷,
# gdzie:
# 𝑡1 = 𝛥𝑋𝐴𝐶𝛥𝑌𝐶𝐷−𝛥𝑌𝐴𝐶𝛥𝑋𝐶𝐷
# 𝛥𝑋𝐴𝐵𝛥𝑌𝐶𝐷−𝛥𝑌𝐴𝐵𝛥𝑋𝐶𝐷
# , 𝑡2 = 𝛥𝑋𝐴𝐶𝛥𝑌𝐴𝐵−𝛥𝑌𝐴𝐶𝛥𝑋𝐴𝐵
# 𝛥𝑋𝐴𝐵𝛥𝑌𝐶𝐷−𝛥𝑌𝐴𝐵𝛥𝑋𝐶𝐷
# .
# O ile jednak w ogólnym zadaniu wyznaczenia współrzędnych punktu przecięcia prostych
# wystarczające jest obliczenie parametrów parametry 𝑡1 i 𝑡2 a następnie współrzędnych punktu
# przecięcia, to w zadaniu wyznaczenia współrzędnych punkty przecięcia odcinków należy
# dodatkowo sprawdzić czy wyznaczony punkt przecięcia należy do obu odcinków (co jest konieczne
# do uznania go za rozwiązanie).
# Rysunek 5. Różne położenie punktu przecięcia dwóch prostych w stosunku do odcinków
# 6
# W celu sprawdzenia przynależności do odcinków możemy wykorzystać parametry 𝑡1 i 𝑡2, na
# podstawie których, można stwierdzić czy punkt przecięcia będzie należał do obu przecinanych
# odcinków. Ma to miejsce, jeżeli: (0 ≤ 𝑡1 ≤ 1) i (0 ≤ 𝑡2 ≤ 1).
# Przykładowe dane do obliczeń przedstawiono w poniższych tabelach, a przykładowy wygląd
# programu realizującego wyznaczenie przecięcia przedstawiono na rys. 6.
# Zestaw 1 Zestaw 2
# Punkt X Y Punkt X Y
# A 1186.00 17962.69 A 5772348.431 7501363.570
# B 1144.74 18006.22 B 5772443.825 7501363.570
# C 1184.31 18004.14 C 5772452.342 7501466.630
# D 1151.14 17957.41 D 5772488.399 7501471.740
# P 1168.210 17981.459 P 5772501.971 7501529.449
# Rysunek 6. Przykładowy wygląd programu
# 2.2 ĆWICZENIE 2 – WYMAGANIA DO PROGRAMU
# 1. Program może być napisany w dowolnym środowisku programistycznym.
# 2. Program powinien mieć możliwość wprowadzania danych z klawiatury jak i odczytu danych
# z pliku tekstowego, a także mieć możliwość zapisania wyników do pliku tekstowego.
# 3. Program powinien realizować prezentację graficzną analizowanych punktów i odcinków wraz
# z punktem ich przecięcia:
# a. pierwsza prezentacja powinna być dopasowana do widoczności wszystkich punktów,
# b. punkty na rysunku powinny być opisana swoimi oznaczeniami (A,B,C,D,P),
# c. powinna istnieć możliwość konfigurowania parametrów rysunku, tzn.: kolory, grubości
# i style linii, widoczność ukrycie oznaczeń punktów.
# 4. Czas na wykonanie ćwiczenia: 4 zajęcia. Program powinien być oddany na koniec szóstych
# zajęć, w przypadku nieoddania wystawiana jest ocena negatywna.

import matplotlib.pyplot as plt
import PySimpleGUI as sg
import os

def tofloat(numbers: list[str]) -> list[float]:
    try:
        retv = [float(x) for x in numbers]
        if len(retv) != 2:
            raise ValueError
        return retv
    except ValueError:
        raise ValueError("Podano błędne dane")


def intersection(A: list[int], B: list[int], C: list[int], D: list[int]) -> list[int]:
    t1l = ((C[0] - A[0]) * (D[1] - C[1]) - (C[1] - A[1]) * (D[0] - C[0]))
    t1m = ((B[0] - A[0]) * (D[1] - C[1]) - (B[1] - A[1]) * (D[0] - C[0]))
    if t1m == 0:
        return None
    t1 = t1l / t1m
    t2l = ((C[0] - A[0]) * (B[1] - A[1]) - (C[1] - A[1]) * (B[0] - A[0]))
    t2m = ((B[0] - A[0]) * (D[1] - C[1]) - (B[1] - A[1]) * (D[0] - C[0]))
    if t2m == 0:
        return None
    t2 = t2l / t2m
    x = A[0] + t1 * (B[0] - A[0])
    y = A[1] + t1 * (B[1] - A[1])
    if 0 <= t1 <= 1 and 0 <= t2 <= 1:
        return [x, y]
    else:
        return None

def update_plot(graph_img, a: list[int], b: list[int], c: list[int], d: list[int], p: list[int],
                ab_color='red', cd_color='blue', labels=True, ab_linewidth=2, cd_linewidth=2):
    plt.clf()
    plt.plot([a[0], b[0]], [a[1], b[1]], ab_color, label='AB', linewidth=ab_linewidth)
    plt.plot([c[0], d[0]], [c[1], d[1]], cd_color, label='CD', linewidth=cd_linewidth)
    if labels:
        plt.text(a[0], a[1], 'A', color=ab_color, fontsize=12)
        plt.text(b[0], b[1], 'B', color=ab_color, fontsize=12)
        plt.text(c[0], c[1], 'C', color=cd_color, fontsize=12)
        plt.text(d[0], d[1], 'D', color=cd_color, fontsize=12)
    if p is not None:
        plt.plot(p[0], p[1], 'go', label='P')
        if labels:
            plt.text(p[0], p[1], 'P', color='green', fontsize=12)
    plt.legend()
    plt.savefig('graph.png')
    graph_img.update(filename='graph.png')
    os.remove('graph.png')


def btn_update(graph_img: sg.Image, window: sg.Window):
    try:
        a_float = tofloat([window['ax'].get(), window['ay'].get()])
        b_float = tofloat([window['bx'].get(), window['by'].get()])
        c_float = tofloat([window['cx'].get(), window['cy'].get()])
        d_float = tofloat([window['dx'].get(), window['dy'].get()])
    except ValueError:
        sg.popup_error('Podano bledne dane')
        return
    p = intersection(a_float, b_float, c_float, d_float)
    if p is None:
        sg.popup_error('Nie ma punktu przeciecia')
        return
    update_plot(graph_img, a_float, b_float, c_float, d_float, p, window['ab_color'].get(), window['cd_color'].get(),
                labels=window['oznaczenia'].get(), ab_linewidth=window['ab_line_width'].get(), cd_linewidth=window['cd_line_width'].get())

# update the plot with data from a file
def file_update(graph_img: sg.Image, window: sg.Window, filename: str, ab_color: str, cd_color: str):
    try:
        # read data from file
        with open(filename, 'r') as f:
            data = f.readlines()
    except FileNotFoundError:
        sg.popup_error('Nie znaleziono pliku')
        return
    # check if data is correct
    if len(data) != 4:
        sg.popup_error('Plik zawiera bledne dane')
        return
    try:
        a_float = tofloat(data[0].split())
        b_float = tofloat(data[1].split())
        c_float = tofloat(data[2].split())
        d_float = tofloat(data[3].split())
    except ValueError:
        sg.popup_error('Plik zawiera bledne dane')
        return
    # set ax, ay, bx, by, cx, cy, dx, dy
    window['ax'].update(a_float[0])
    window['ay'].update(a_float[1])
    window['bx'].update(b_float[0])
    window['by'].update(b_float[1])
    window['cx'].update(c_float[0])
    window['cy'].update(c_float[1])
    window['dx'].update(d_float[0])
    window['dy'].update(d_float[1])
    p = intersection(a_float, b_float, c_float, d_float)
    if p is None:
        sg.popup_error('Nie ma punktu przeciecia')
        return
    update_plot(graph_img, a_float, b_float, c_float, d_float, p, window['ab_color'].get(), window['cd_color'].get(),
                labels=window['oznaczenia'].get(), ab_linewidth=window['ab_line_width'].get(), cd_linewidth=window['cd_line_width'].get())
  

def main():
    ab_color = 'red'
    cd_color = 'blue'
    # stworzenie okna z miejscami na wprowadzenie danych oraz wykres
    ax = sg.InputText(size=(10, 1), key='ax')
    ay = sg.InputText(size=(10, 1), key='ay')
    bx = sg.InputText(size=(10, 1), key='bx')
    by = sg.InputText(size=(10, 1), key='by')
    cx = sg.InputText(size=(10, 1), key='cx')
    cy = sg.InputText(size=(10, 1), key='cy')
    dx = sg.InputText(size=(10, 1), key='dx')
    dy = sg.InputText(size=(10, 1), key='dy')
    A = sg.Frame('A', [[ax, ay]])
    B = sg.Frame('B', [[bx, by]])
    C = sg.Frame('C', [[cx, cy]])
    D = sg.Frame('D', [[dx, dy]])
    # change color of button
    colors = ['red', 'blue', 'green', 'yellow', 'black', 'white']
    ab_color_combo = sg.Combo(colors, default_value='red', key='ab_color', size=(10, 4), font=('Helvetica', 12))
    cd_color_combo = sg.Combo(colors, default_value='blue', key='cd_color', size=(10, 4), font=('Helvetica', 12))
    # line width
    ab_line_width = sg.Combo(list(range(1,11)), default_value=2, key='ab_line_width', size=(10, 4), font=('Helvetica', 12))
    cd_line_width = sg.Combo(list(range(1,11)), default_value=2, key='cd_line_width', size=(10, 4), font=('Helvetica', 12))
    oznaczenia = sg.Checkbox('Oznaczenia', default=True, key='oznaczenia')
    # load data from a file button, accepted file format: .txt
    wczytaj = sg.FileBrowse('Wczytaj dane z pliku', file_types=(('Pliki tekstowe', '*.txt'),), key='wczytaj')
    nazwa_pliku = sg.InputText(size=(10, 1), key='nazwa_pliku')
    oblicz = sg.Button('Oblicz', key='Oblicz')

    graph_img: sg.Image = None

    # check if graph.png exists
    if os.path.isfile('graph.png'):
        os.remove('graph.png')
    plt.plot(0, 0)
    plt.savefig('graph.png')
    graph_img = sg.Image(filename='graph.png', key='graph')

    layout = [[sg.Text('Podaj wspolrzedne punktu A'), A],
                [sg.Text('Podaj wspolrzedne punktu B'), B],
                [sg.Text('Podaj wspolrzedne punktu C'), C],
                [sg.Text('Podaj wspolrzedne punktu D'), D],
                [graph_img],
                [sg.Text('Kolor odcinka AB'), ab_color_combo, ab_line_width, sg.Text('Kolor odcinka CD'), cd_color_combo, cd_line_width, oznaczenia],
                [wczytaj, nazwa_pliku],
                [oblicz]]
    
    window = sg.Window('Zadanie 2', layout, background_color='lightblue').Finalize()

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break
        
        # if the button is clicked
        elif event == 'Oblicz':
            if values['nazwa_pliku'] != '':
                file_update(graph_img, window, values['nazwa_pliku'], values['ab_color'], values['cd_color'])
                # clear the input
                window['nazwa_pliku'].update('')
            else:
                btn_update(graph_img, window)
        

if __name__ == "__main__":
    main()