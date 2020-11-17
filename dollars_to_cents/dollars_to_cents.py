import PySimpleGUI as sg

sg.theme('darkgreen')

layout = [
    [sg.Text('How much did the item cost?'), sg.InputText(key='_cost_')],
    [sg.Text('How much did you pay?'), sg.InputText(key='_paid_')],
    [sg.Button('Get Change'), sg.Button('Clear')],
    [sg.Output((20, 5), key='_output_')]
]

def coin_split(number):
    number = int(number * 100)
    quarter = number // 25
    balance = number % 25
    dime = balance // 10
    balance = balance % 10
    nickel = balance // 5
    balance = balance % 5
    penny = balance // 1
    newline = '\n'
    return f'quarters: {quarter}{newline}dimes: {dime}{newline}nickels: {nickel}{newline}pennies: {penny}'

def change_make(cost, paid):
    remainder = paid - cost
    if remainder < 0:
        return 'Need more money.'
    else:
        return coin_split(remainder)

# print(coin_split(0.58))
# print(change_make(3.60, 5))

window = sg.Window('Change Maker', layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    if event == 'Get Change':
        print(change_make(float(values['_cost_']), float(values['_paid_'])))
    if event == 'Clear':
        window['_output_']('')
        window['_cost_']('')
        window['_paid_']('')

window.close()