import PySimpleGUI as sg
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

layout = [
    [sg.Text('Numero')],
    [sg.Input(key='numero')],
    [sg.Button('Verificar')],
    [sg.Text(key='mensagem')]
]
window = sg.Window('Verificador de numeros', layout=layout)

leitura = pd.read_excel('teste.xlsx')
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    elif event == 'Verificar':
        numero = values['numero']
        # colocar aqui o cartão duplicado
        filtro = leitura['TABELA1'] == numero
        # #lembrar que quando acrescenta a tabela no excel o resultado da coluna sera +2 ou +1
        teste1 = leitura[filtro]
        window['mensagem'].update(teste1)
