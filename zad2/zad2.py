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
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

fig, ax = plt.subplots()
ax.set_xlabel('x')
ax.set_ylabel('y')

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


def update_plot(canvas, a: list[int] | None, b: list[int] | None, c: list[int] | None, d: list[int] | None,
                p: list[int] | None, ab_color='red', cd_color='blue', labels=True, ab_linewidth=2, cd_linewidth=2):
    # clear plot
    ax.cla()
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    if a is not None and b is not None:
        ax.plot([a[0], b[0]], [a[1], b[1]], ab_color, label='AB', linewidth=ab_linewidth)
    if c is not None and d is not None:
        ax.plot([c[0], d[0]], [c[1], d[1]], cd_color, label='CD', linewidth=cd_linewidth)
    if labels:
        if a is not None:
            ax.scatter(a[0], a[1], color=ab_color)
            ax.text(a[0], a[1], 'A', color=ab_color, fontsize=12)
        if b is not None:
            ax.scatter(b[0], b[1], color=ab_color)
            ax.text(b[0], b[1], 'B', color=ab_color, fontsize=12)
        if c is not None:
            ax.scatter(c[0], c[1], color=cd_color)
            ax.text(c[0], c[1], 'C', color=cd_color, fontsize=12)
        if d is not None:
            ax.scatter(d[0], d[1], color=cd_color)
            ax.text(d[0], d[1], 'D', color=cd_color, fontsize=12)
    if p is not None:
        ax.plot(p[0], p[1], 'go', label='P')
        if labels:
            ax.scatter(p[0], p[1], color='green')
            ax.text(p[0], p[1], 'P', color='green', fontsize=12)
    ax.legend()
    fig.canvas.draw()


def btn_update(canvas, window):
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
    else:
        window['px'].update(p[0])
        window['py'].update(p[1])
        update_plot(canvas, a_float, b_float, c_float, d_float, p, window['ab_color'].get(), window['cd_color'].get(),
                    labels=window['oznaczenia'].get(), ab_linewidth=window['ab_line_width'].get(), cd_linewidth=window['cd_line_width'].get())

def line_style_update(canvas, window):
    try:
        a_float = tofloat([window['ax'].get(), window['ay'].get()])
        b_float = tofloat([window['bx'].get(), window['by'].get()])
        c_float = tofloat([window['cx'].get(), window['cy'].get()])
        d_float = tofloat([window['dx'].get(), window['dy'].get()])
        p_float = tofloat([window['px'].get(), window['py'].get()])
    except ValueError:
        return
    update_plot(canvas, a_float, b_float, c_float, d_float, p_float, window['ab_color'].get(), window['cd_color'].get(),
                labels=window['oznaczenia'].get(), ab_linewidth=window['ab_line_width'].get(), cd_linewidth=window['cd_line_width'].get())

# update the plot with data from a file
def file_update(canvas, window: sg.Window, ab_color: str, cd_color: str):
    filename = sg.popup_get_file('Wybierz plik', file_types=(('Pliki tekstowe', '*.txt'),))
    if filename is None or filename == '':
        return
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
    else:
        window['px'].update(p[0])
        window['py'].update(p[1])
        update_plot(canvas, a_float, b_float, c_float, d_float, p, window['ab_color'].get(), window['cd_color'].get(),
                    labels=window['oznaczenia'].get(), ab_linewidth=window['ab_line_width'].get(), cd_linewidth=window['cd_line_width'].get())
  

def main():
    # stworzenie okna z miejscami na wprowadzenie danych oraz wykres
    ax = sg.InputText(size=(10, 1), key='ax')
    ay = sg.InputText(size=(10, 1), key='ay')
    bx = sg.InputText(size=(10, 1), key='bx')
    by = sg.InputText(size=(10, 1), key='by')
    cx = sg.InputText(size=(10, 1), key='cx')
    cy = sg.InputText(size=(10, 1), key='cy')
    dx = sg.InputText(size=(10, 1), key='dx')
    dy = sg.InputText(size=(10, 1), key='dy')
    # make them uneditable
    px = sg.InputText(size=(10, 1), key='px', disabled=True)
    py = sg.InputText(size=(10, 1), key='py', disabled=True)
    A = sg.Frame('A', [[ax, ay]])
    B = sg.Frame('B', [[bx, by]])
    C = sg.Frame('C', [[cx, cy]])
    D = sg.Frame('D', [[dx, dy]])
    P = sg.Frame('P', [[px, py]])
    # change color of button
    colors = ['magenta', 'red', 'blue', 'green', 'yellow', 'black', 'white']
    ab_color_combo = sg.Combo(colors, default_value='magenta', key='ab_color', size=(10, 4), font=('Helvetica', 12))
    cd_color_combo = sg.Combo(colors, default_value='blue', key='cd_color', size=(10, 4), font=('Helvetica', 12))
    # line width
    ab_line_width = sg.Combo(list(range(1,11)), default_value=2, key='ab_line_width', size=(10, 4), font=('Helvetica', 12))
    cd_line_width = sg.Combo(list(range(1,11)), default_value=2, key='cd_line_width', size=(10, 4), font=('Helvetica', 12))
    oznaczenia = sg.Checkbox('Oznaczenia', default=True, key='oznaczenia')
    # load data from a file button, accepted file format: .txt
    wczytaj = sg.Button('Wczytaj dane z pliku', key='wczytaj')
    zapisz = sg.FileSaveAs('Wybierz plik do zapisania danych', file_types=(('Pliki tekstowe', '*.txt'),), key='zapisz')
    zapisz_button = sg.Button('Zapisz', key='zapisz_button')
    zapisz_nazwa_pliku = sg.InputText(sg.user_settings_get_entry('-filename-', ''), key='zapisz_nazwa_pliku', size=(30, 1))
    oblicz = sg.Button('Oblicz', key='Oblicz')

    

    layout = [[sg.Text('Podaj wspolrzedne punktu A'), A, sg.Text('Podaj wspolrzedne punktu B'), B],
                [sg.Text('Podaj wspolrzedne punktu C'), C, sg.Text('Podaj wspolrzedne punktu D'), D],
                [sg.Text('Wspolrzedne punktu P'), P],
                [sg.Graph(canvas_size=(800, 800), graph_bottom_left=(0, 0), graph_top_right=(100, 100), key='graph')],
                [sg.Text('Kolor odcinka AB'), ab_color_combo, ab_line_width, sg.Text('Kolor odcinka CD'), cd_color_combo, cd_line_width, oznaczenia],
                [wczytaj],
                [sg.Text('Nazwa pliku do zapisu:'), zapisz_nazwa_pliku, zapisz, zapisz_button],
                [oblicz]]
    
    
    window = sg.Window('Zadanie 2', layout)
    window.finalize()

    canvas = FigureCanvasTkAgg(fig, master=window['graph'].Widget)
    plot_widget = canvas.get_tk_widget()
    plot_widget.grid(row=0, column=0)
    ab_old_val = window['ab_color'].get()
    cd_old_val = window['cd_color'].get()
    oznaczenia_old_val = window['oznaczenia'].get()
    szerokosc_ab = window['ab_line_width'].get()
    szerokosc_cd = window['cd_line_width'].get()

    while True:
        event, values = window.read(10)
        if event == sg.WIN_CLOSED:
            if os.path.isfile('graph.png'):
                os.remove('graph.png')
            break
        if event == 'Oblicz':
            btn_update(canvas, window)
        elif event == 'wczytaj':
            file_update(canvas, window, values['ab_color'], values['cd_color'])
        elif event == 'zapisz_button':
            try:
                with open(values['zapisz_nazwa_pliku'], 'w') as f:
                    f.write(f'{values["ax"]} {values["ay"]}\n')
                    f.write(f'{values["bx"]} {values["by"]}\n')
                    f.write(f'{values["cx"]} {values["cy"]}\n')
                    f.write(f'{values["dx"]} {values["dy"]}\n')
                    f.write(f'{values["px"]} {values["py"]}\n')
            except FileNotFoundError:
                sg.popup_error('Nie znaleziono pliku')
            window['zapisz_nazwa_pliku'].update('')
        # on combo color change
        if ab_old_val != window['ab_color'].get() or cd_old_val != window['cd_color'].get() or oznaczenia_old_val != window['oznaczenia'].get() or szerokosc_ab != window['ab_line_width'].get() or szerokosc_cd != window['cd_line_width'].get():
            ab_old_val = window['ab_color'].get()
            cd_old_val = window['cd_color'].get()
            oznaczenia_old_val = window['oznaczenia'].get()
            line_style_update(canvas, window)

if __name__ == "__main__":
    main()