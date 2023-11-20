import tkinter as tk
from tkinter import ttk


def skillUsed():
    if chkUsedVar.get() == 1:
        style.map('custom.TCombobox', fieldbackground=[('readonly','green')])
        style.map('custom.TCombobox', foreground=[('readonly','red')])
    else:
        style.map('custom.TCombobox', fieldbackground=[('readonly','white')])
        style.map('custom.TCombobox', foreground=[('readonly','black')])

root = tk.Tk()

style = ttk.Style()
style.theme_use('alt')

cboxVar1 = tk.StringVar()
cboxVar1.set("spam")

cboxVar2 = tk.StringVar()
cboxVar2.set("silly")

chkUsedVar = tk.IntVar()
chk = tk.Checkbutton(root, text='Used', variable=chkUsedVar, command=skillUsed)
chk.grid(row=0, column=2)

combo01 = ttk.Combobox(root, values=['spam', 'eric', 'moose'], textvariable=cboxVar1)
combo01['state'] = 'readonly'
combo01.grid(row=0, column=0)

combo02 = ttk.Combobox(root, values=['parrot', 'silly', 'walk'], textvariable=cboxVar2, style='custom.TCombobox')
combo02['state'] = 'readonly'
combo02.grid(row=0, column=1)

root.mainloop()