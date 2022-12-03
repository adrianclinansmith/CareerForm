import os
import PySimpleGUI as gui
import sys

if len(sys.argv) != 2:
    print(f"usage: python3 {sys.argv[0]} file_name", file=sys.stderr)
    exit(1)
if os.path.exists(sys.argv[1]) == False:
    with open(sys.argv[1], "w") as file:
        file.write("Company,Sign-In,PW\n")

gui.theme("DarkTeal9")
font = ("Helvetica", 20)

def guiText(text: str, width: int = 18) -> str:
    return gui.Text(text, size=(width,1), font=font, grab=True)

def guiTextAndInput(text: str) -> list:
    return [guiText(text), gui.Input(key=text, expand_x=True, font=font, enable_events=True)]

layout = [
    [guiText("File"), gui.FileBrowse(key="Browse", font=font)],
    guiTextAndInput("Company"),
    guiTextAndInput("Sign-In"),
    guiTextAndInput("PW"),
    [gui.Submit(font=font)]
]

# Event loop
window = gui.Window("Career Form", layout, resizable=True)
while True:
    event, values = window.read()
    print(event)
    if event == gui.WINDOW_CLOSED:
        break
    elif event == "File":
        print("file selected")
    elif event == "Submit":
        with open(sys.argv[1], "a") as file:
            row = f"{values['Company']},{values['Sign-In']},{values['PW']}\n"
            file.write(row)
window.close()