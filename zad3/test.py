import PySimpleGUI as sg

layout = [
    [sg.Combo(['blue', 'red', 'green'], default_value='blue', key='color', enable_events=True)],
]


window = sg.Window('Window Title', layout)

while True:
    event, values = window.read()
    dodaj()
    print(a)
    if event == sg.WIN_CLOSED:
        break
    print(event, values)