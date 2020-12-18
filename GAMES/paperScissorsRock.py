import tkinter

def declaringWidgets(root, wWidth, wHeigh):
    paperButton = tkinter.Button(root, text ="Papel", width=10, command = lambda: action("paper"))
    scissorsButton = tkinter.Button(root, text ="Tigeras", width=10, command = lambda: action("scissors"))
    rockButton = tkinter.Button(root, text ="Piedra", width=10, command = lambda: action("rock"))
    
    rockButton.place(x=((wWidth / 3) - 35),y=(wHeigh * 0.4 - wHeigh * 0.08))
    scissorsButton.place(x=(((wWidth / 3) * 2) - 35),y=(wHeigh * 0.4 - wHeigh * 0.08))
    paperButton.place(x=((wWidth / 2) - 35),y=(wHeigh * 0.4 - wHeigh * 0.08))

def action(act):
    print(act)