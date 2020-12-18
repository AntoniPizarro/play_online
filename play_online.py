from tkinter import *
import GAMES.paperScissorsRock as psr

ventana = Tk()
window_W = 500
window_H = 100
ventana_geo = str(window_W) + "x" + str(window_H)
ventana.geometry(ventana_geo)
ventana.resizable(0, 0)

psr.declaringWidgets(ventana, window_W, window_H)

ventana.mainloop()