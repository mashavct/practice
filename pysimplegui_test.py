import PySimpleGUI as sg

# All the stuff inside your window.
layout = [[sg.Text('Calculator')],
            [sg.Text('Введите пример'), sg.InputText()],
            [sg.Button('Calculate')],
            [sg.Text('', key='-RESULT-')]]

# Create the Window
window = sg.Window('Calculator Mashiksov', layout)

# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event != sg.WIN_CLOSED:
        try:
            values_after_splitting = values[0].split(" ")
            fisrt_number = float(values_after_splitting[0])
            second_number = float(values_after_splitting[2])
            sign = values_after_splitting[1]
            calc = 0

            if sign == '+':
                calc = fisrt_number + second_number
                calc = f'Результат равен {calc}'
            elif sign == '-':
                calc = fisrt_number - second_number
                calc = f'Результат равен {calc}'
            elif sign == '*':
                calc = fisrt_number * second_number
                calc = f'Результат равен {calc}'
            elif sign == '/':
                calc = fisrt_number / second_number
                calc = f'Результат равен {calc}'
            else:
                raise Exception

            window['-RESULT-'].update(calc)

        except Exception:
            calc = "Проверьте правильность введенного примера"
            window['-RESULT-'].update(calc)

        calc = None

window.close()
