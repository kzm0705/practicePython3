import PySimpleGUI as sg

layout = [[sg.Text('麻雀')]]

window = sg.Window('麻雀スピード', layout, size=(600,600))

def main():
    while True:
        event, values = window.read()

        if event == sg.WINDOW_CLOSED:
            break

    window.close()

if __name__ =="__main__":
    main()

