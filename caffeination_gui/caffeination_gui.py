import pyautogui
import time
import sys
import PySimpleGUI as sg
import _thread
import os
import platform

def run_caffeination():
    global stop
    try:
        while not stop:
            mouse_x, mouse_y = pyautogui.position()
            pyautogui.moveTo(mouse_x + 1, mouse_y + 1)
            pyautogui.moveTo(mouse_x - 1, mouse_y - 1)
            for second in range(30):
                if stop:
                    break
                time.sleep(second)
            else:
                break
    except KeyboardInterrupt:
        sys.exit()
    
def gui():
    global stop
    pyautogui.FAILSAFE = False
    if platform.system() == "Linux" or platform.system() == "Darwin":
        icon_path = "coffee.png"
    else:
        icon_path = "coffee.ico"
    sg.theme('DarkBrown1')
    layout = [
        [sg.Text('                                                                                 ')],
        [sg.Text('Caffeination prevents your\ncomputer from going to sleep', justification='center')],
        [sg.Button('Start', key="-start-"), sg.Button('Stop', disabled=True)],
        [sg.Button('Quit')],
        [sg.Button('About', button_color=(sg.YELLOWS[1], sg.GREENS[0]))]
        ]
    window = sg.Window('Caffeination', layout, element_justification='center', icon=icon_path)
    while True:
        event, values = window.read()
        if event == '-start-':
            stop = False
            window.FindElement('-start-').Update("Running", disabled=True)
            window.FindElement('Stop').Update(disabled=False)
            caffeination_thread = _thread.start_new_thread(run_caffeination, ())
            sg.SystemTray.notify('Caffeination','Caffeination started successfully\nStop it by clicking on Stop or Quit buttons', icon="coffee.png")
        if event == 'Stop':
            stop = True
            time.sleep(1.2)
            window.FindElement('-start-').Update("Start", disabled=False)
            window.FindElement('Stop').Update(disabled=True)
            sg.SystemTray.notify('Caffeination','Caffeination was stopped')
        if event == 'About':
            sg.Popup('''Caffeination was created by\n
Antonio Raffaele Iannaccone\n
https://github.com/neisor\n\n
Creator of the icon is:\n
https://constantino.co.nz/''', title='About', icon=icon_path)
        if event == sg.WIN_CLOSED or event == 'Quit':
            break
    window.Close()
    sys.exit()

if __name__ == '__main__':
    gui()


