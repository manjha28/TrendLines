#Created by Manish JHa

'''First we need to get the data
for Daily data we'll get it from NSEPy or Yahoo finance
for intraday data we'll need to subscribe for Zerodha/NSE API
'''

from nsepy import get_history
import numpy as np
import pandas as pd
import PySimpleGUI as sg
from datetime import date
sg.theme('DarkAmber')

layout = [[sg.Text('Enter symbol of stock'), sg.InputText()], [sg.Text('Date in format(YYYY,MM,DD)')],
          [sg.Text('From'), sg.InputText()], [sg.Text('TO'), sg.InputText()],
          [sg.Button("Get Data"), sg.CloseButton("Cancel")]]

window = sg.Window('Window Title', layout)

while True:
    event, values = window.read()
    if event == 'Get Data':
        h = values[0]
        t = (tuple(map(int,(values[1]).split(','))))
        f = (tuple(map(int,(values[2]).split(','))))
        a = t[0]
        b = t[1]
        c = t[2]
        d = f[0]
        e = f[1]
        g = f[2]
        Stock_History = get_history(symbol=h,
                                    start=date(a, b, c),
                                    end=date(d, e, g))
