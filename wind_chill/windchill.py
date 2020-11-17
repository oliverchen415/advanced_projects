import PySimpleGUI as sg

sg.theme('TealMono')

layout = [
          [sg.Text('Enter the current temperature'), sg.InputText(key='_temp_')],
          [sg.Text('Enter the wind speed'), sg.InputText(key='_wind_')],
          [sg.Text('Select units'),
           sg.Radio('Imperial (°F/mph)', 'RADIO1', default=True),
           sg.Radio('Metric (°C/kph)', 'RADIO1')],
          [sg.Button('Calculate'), sg.Button('Clear')],
          [sg.Output(key = '_output_')]
          ]

window = sg.Window('Wind Chill Calc', layout)

# ? The equation for US windchill is 35.74 + 0.6215*T_air - 35.75v**0.16 + 0.4275*T_air*v**0.16
# ? The values are for Fahrenheit and mph

# ? The equation for metric windchill is 13.12 + 0.6215*T_air - 11.37*v**0.16 + 0.3965*T_air*(v**0.16)
# ? The values are for Celcius and kph

def wind_chill(airtemp, windspeed, units='imperial'):
    results = 0
    units = units.lower()

    if units == 'imperial':
        results = round((35.74 + 0.6215*airtemp - 35.75*(windspeed**0.16) + 0.4275*airtemp*(windspeed**0.16)), 2)
    elif units == 'metric':
        results = round(13.12 + 0.6215*airtemp - 11.37*(windspeed**0.16) + 0.3965*airtemp*(windspeed**0.16), 2)

    if results >= airtemp:
        return 'Error, calculated wind chill higher than actual temp'
    else:
        return results

# print(wind_chill(32, 10))
# print(wind_chill(0, 16, 'Metric'))
# print(wind_chill(55, 2))
# print(wind_chill(0, 40, 'Metric'))

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    if event == 'Calculate':
        if values['_temp_'] == '' or values['_wind_'] == '':
            print('Error, please make sure all fields are filled.')
        elif values[0]:
            print(wind_chill(int(values['_temp_']), int(values['_wind_'])))
        elif values[1]:
            print(wind_chill(int(values['_temp_']), int(values['_wind_']), 'Metric'))
    if event == 'Clear':
        window['_output_']('')
        window['_temp_']('')
        window['_wind_']('')

window.close()