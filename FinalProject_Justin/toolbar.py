import tkinter as tk
from tkinter import ttk #add this to the main file
import webbrowser as wb #add this to the main file
from tkinter import *
from tkinter.messagebox import *
import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure  import Figure
import numpy as np
import scipy.constants as sp

LARGE_FONT = ("Verdana", 12)

class RotationCurves(tk.Tk):
	def __init__(self, *args, **kwargs):
		tk.Tk.__init__(self)
		tk.Tk.wm_title(self, "Rotation Curves Client")
		self.minsize(width = 200, height = 200)
		container = tk.Frame(self)
		container.pack(side = "top", fill = "both", expand = True)
		container.grid_rowconfigure(0, weight = 1)
		container.grid_columnconfigure(0, weight = 1)
		'''self.frames = {}
		frame = StartPage(container, self)
		self.frames[StartPage] = frame
		frame.grid(row = 0, column = 0, sticky = "nsew")
		self.show_frame(StartPage)'''
		menubar = Menu(container)
		tk.Tk.config(self, menu=menubar)
		fileMenu = tk.Menu(menubar, tearoff = 0 )
		fileMenu.add_command(label="Exit", command=self.quit)
		fileMenu.add_command(label="Save", command=self.popup)
		menubar.add_cascade(label="File", menu=fileMenu)
		editMenu = tk.Menu(menubar)
		menubar.add_cascade(label="Edit", menu=editMenu)
		editMenu.add_command(label="Universe", command=self.quit)
		viewMenu = tk.Menu(menubar)
		menubar.add_cascade(label="View", menu=editMenu)
		viewMenu.add_command(label="Graph", command=self.quit)
		helpMenu = tk.Menu(menubar)
		menubar.add_cascade(label="Help", menu=helpMenu)
		helpMenu.add_command(label="Tutorial", command=self.quit)
		helpMenu.add_command(label="Git repo", command=self.link)


	def link(self):
		wb.open('https://github.com/rpanman/Pydecal-Final-Project')
	def show_frame(self, cont):
		frame = self.frames[cont]
		frame.tkraise()
	def show_frame(self, cont):
		frame = self.frames[cont]
		frame.tkraise()
	def popup(self):
		popup = tk.Tk()
		popup.wm_title("Not yet supported!")
		label = ttk.Label(popup, text=msg, font=LARGE_FONT)
		labelpack(side="top", fill="x", pady=10)
		B1 = ttk.Button(popup, text="Okay", command=self.quit)
		B1.pack()
		popup.mainloop()
app = RotationCurves()
app.mainloop()
