import secrets
import random

import PySimpleGUI as sg

sg.theme('Kayak')

layout = [
    [sg.Frame(
        layout=[
            [
                sg.Text('Length of Password?'),
                sg.InputText(key='_pwlen_', default_text='8', size=(10,1)),
                sg.Checkbox('Include symbols', default=False, key='_sym_'),
                sg.Frame(layout=
                    [
                        [sg.Combo(['Standard Mode', 'Extreme Mode'], default_value='Standard Mode', enable_events=True, key='_mode_')]
                    ],
                    title='Security Level'
                ),
            ]],
            title='Options'
            )],
    [sg.Output(key='_output_', size=(55, 3)), sg.Button('Generate')]
    ]


# * ASCII lists
upperCaseList = [chr(value) for value in range(65, 91)]
lowerCaseList = [chr(value) for value in range(97, 123)]
numeralsList = [chr(value) for value in range(48, 58)]
symbolsList = [chr(value) for value in range(33, 44)]

alphaNum = upperCaseList + lowerCaseList + numeralsList + symbolsList
anNoSymbols = upperCaseList + lowerCaseList + numeralsList

def pwgen(max_len, symbols=True):
    if (max_len < 4 and symbols == True) or (max_len < 3 and symbols == False):
        raise ValueError('Invalid password length, enter a valid length.')
    if symbols == True:
        pwStart = [secrets.choice(upperCaseList), secrets.choice(lowerCaseList), secrets.choice(numeralsList), secrets.choice(symbolsList)]
    else:
        pwStart = [secrets.choice(upperCaseList), secrets.choice(lowerCaseList), secrets.choice(numeralsList)]
    charRemain = max_len - len(pwStart)
    newAlphaNum = 0
    while newAlphaNum < charRemain:
        if symbols == True:
            pwStart += secrets.choice(alphaNum)
        else:
            pwStart += secrets.choice(anNoSymbols)
        newAlphaNum += 1
    secrets.SystemRandom().shuffle(pwStart)
    pwStart = ''.join(pwStart)
    return pwStart

window = sg.Window('Password Generator', layout)

while True:
    event, values = window.Read()
    if event == sg.WIN_CLOSED:
        break
    if event == 'Generate':
        window['_output_']('')
        if values['_mode_'] == 'Standard Mode':
            print(pwgen(int(values['_pwlen_']), symbols = values['_sym_']))
        elif values['_mode_'] == 'Extreme Mode':
            print('PASSWORD ' + random.choice(['!', '?', '~']))

window.close()