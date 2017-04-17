import tkinter as tk
from tkinter import *
import matplotlib 
matplotlib.use("TkAgg")
#from matplotlib.backends.backend_TkAgg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure 
import numpy as np 

LARGE_FONT = ("Verdana", 12)

class RotationCurves(tk.Tk):
	def __init__(self, *args, **kwargs):
		tk.Tk.__init__(self)
		tk.Tk.wm_title(self, "Rotation Curves Client")
		self.minsize(width = 600, height = 200)
		container = tk.Frame(self)
		container.pack(side = "top", fill = "both", expand = True)
		container.grid_rowconfigure(0, weight = 1)
		container.grid_columnconfigure(0, weight = 1)
		self.frames = {}
		frame = StartPage(container, self)
		self.frames[StartPage] = frame
		frame.grid(row = 0, column = 0, sticky = "nsew")
		self.show_frame(StartPage)
	
	def show_frame(self, cont):
		frame = self.frames[cont]
		frame.tkraise()

def solve(msg):
	print(msg)

def graph():
	popup = tk.Tk()
	popup.wm_title("Graph")
	label = tk.Label(popup, text = "Velocity vs Radius", font = LARGE_FONT).grid(row = 0, column = 3, columnspan = 2, sticky = W)
	graph_quit = tk.Button(popup, text = "Quit", command = popup.destroy).grid(row = 2, column = 3, sticky = W)
	popup.mainloop()

def sure():
	sure = tk.Tk()
	sure.wm_title("Exit")
	check = tk.Label(sure, text = "Are you sure?", font = LARGE_FONT).grid(row = 0, column = 2, columnspan = 2, sticky = W)
	sure.sure_yes = tk.Button(sure, text = "Yes", command = combine_funcs(sure.destroy)).grid(row = 2, column = 3, sticky = W)
	sure_no = tk.Button(sure, text = "No", command = sure.destroy).grid(row = 2, column = 4, sticky =W)


def combine_funcs(*funcs):
    def combined_func(*args, **kwargs):
        for f in funcs:
            f(*args, **kwargs)
    return combined_func

class StartPage(Frame):
	
	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		def reveal(self):
			RS = RedshiftBlank.get()
			Message = "Congrats"
			self.Results.insert(0.0, Message)
		Instruction = tk.Label(self, text = 'Enter Values', font = LARGE_FONT).grid(row = 0, column = 0, sticky = W)
		Redshift = tk.Label(self, text = "Redshift:").grid(row = 1, column = 0, columnspan = 2,  sticky = W)
		RedshiftBlank = Entry(self).grid(row = 1, column = 3, columnspan = 2, sticky = W)
		AVGWL = tk.Label(self, text = "Average Wavelength:").grid(row = 2, column = 0, columnspan = 2, sticky = W)
		AVGWLBlank = Entry(self).grid(row =2 , column = 3, columnspan = 2, sticky = W)
		ChangeWl= tk.Label(self, text = "Change in Wavelength").grid(row = 3, column = 0, sticky = W)
		ChangeWLBlank = Entry(self).grid(row = 3, column = 3, columnspan = 2, sticky = W)
		Distance = Label(self, text = "Vertical Distance").grid(row = 4, column = 0, sticky = W)
		DistanceBlank = Entry(self).grid(row = 4, column = 3, columnspan = 2, sticky = W)
		start_Solve = tk.Button(self, text = 'Solve', command = reveal).grid(row = 5, column = 2, sticky = W) #This button runs the rotation curve solver #Where the button is on the GUI		#button1.grid(row = 5, column = 2, sticky = W)
		start_Graph = tk.Button(self, text = 'Graph', command = lambda: graph()).grid(row = 5, column = 4, sticky = W) #Graphs the curve on a different grame. Second command brings the frame forward.
		start_Exit = tk.Button(self, text = "Exit", command = lambda: sure()).grid(row = 6, column = 2, sticky = W)
		self.Results = Text(self, width = 30, height = 6, wrap = WORD).grid(row = 0, column = 5, columnspan = 5, rowspan = 6, sticky = W)

		#f = Figure(figsize = (5,5), dpi = 100)
		#canvas = FigureCanvasTkAgg(f, self)
		#canvas.show()
		#canvas .get_tk_widget().pack(side = tk.TOP, fill = tk.BOTH, expand = True)

app = RotationCurves()
app.mainloop()

