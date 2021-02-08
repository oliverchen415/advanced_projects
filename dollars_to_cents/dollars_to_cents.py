import PySimpleGUI as sg
import decimal

sg.theme('darkgreen')

layout = [
    [sg.Text('How much did the item cost?'), sg.InputText(key='_cost_')],
    [sg.Text('How much did you pay?'), sg.InputText(key='_paid_')],
    [sg.Button('Get Change'), sg.Button('Clear')],
    [sg.Output((20, 5), key='_output_')]
]

def coin_split(number):
    number = int(number * 100)
    quarter = str(decimal.Decimal(number) // decimal.Decimal(25))
    balance = number % 25
    dime = str(decimal.Decimal(balance) // decimal.Decimal(10))
    balance = balance % 10
    nickel = str(decimal.Decimal(balance) // decimal.Decimal(5))
    balance = balance % 5
    newline = '\n'
    return f'quarters: {quarter}{newline}dimes: {dime}{newline}nickels: {nickel}{newline}pennies: {balance}'

def change_make(cost, paid):
    remainder = paid - cost
    if remainder < 0:
        return 'Need more money.'
    return coin_split(remainder)

# print(coin_split(0.58))
# print(change_make(3.60, 5))

window = sg.Window('Change Maker', layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    if event == 'Get Change':
        print(change_make(decimal.Decimal(values['_cost_']), decimal.Decimal(values['_paid_'])))
    if event == 'Clear':
        window['_output_']('')
        window['_cost_']('')
        window['_paid_']('')

window.close()