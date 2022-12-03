"""
How to Create an Excel Data Entry Form in 10 Minutes Using Python:
https://m.youtube.com/watch?v=svcv8uub0D0
"""

import PySimpleGUI as gui

gui.theme("DarkTeal9")

font = ("Helvetica", 20)

def guiText(text: str) -> str:
    return gui.Text(text, size=(15,1), font=font)
layout = [
    [guiText("Please fill out:")],
    [guiText("Name"), gui.Input(key="Name", expand_x=True, font=font)],
    [guiText("Favorite Color"), 
        gui.Combo(["Red", "Green", "Blue"], key="Favorite Color")],
    [guiText("I Speak"),
        gui.Checkbox("English", key="English"), 
        gui.Checkbox("Chinese", key="Chinese")],
    [guiText("No. of Children"), gui.Spin([0,1,2,3], initial_value=0, key="Children")],
    [gui.Submit(auto_size_button=True), gui.Exit()]
]
window = gui.Window("Data entry form", layout, resizable=True)
while True:
    event, values = window.read()
    if event == gui.WINDOW_CLOSED or event == "Exit":
        break
    elif event == "Submit":
        print(event, values)
window.close()