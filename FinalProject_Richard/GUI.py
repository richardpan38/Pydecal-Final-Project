import tkinter as tk
from tkinter import *
from tkinter.messagebox import *
import matplotlib 
matplotlib.use("TkAgg")
#from matplotlib.backends.backend_TkAgg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure 
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
		self.frames = {}
		frame = StartPage(container, self)
		self.frames[StartPage] = frame
		frame.grid(row = 0, column = 0, sticky = "nsew")
		self.show_frame(StartPage)
	
	def show_frame(self, cont):
		frame = self.frames[cont]
		frame.tkraise()

def combine_funcs(*funcs):
    def combined_func(*args, **kwargs):
        for f in funcs:
            f(*args, **kwargs)
    return combined_func

class StartPage(Frame): # must need line
	def __init__(self, parent, controller): #must need line
		tk.Frame.__init__(self, parent) #Must need line
		#menubar = Menu(self)
		#self.config(menu=menubar)
		#fileMenu = Menu(menubar)
		#fileMenu.add_command(label="Exit", command=self.onExit)
		##fileMenu.add_command(label="Save", command=self.filewrite)
		#menubar.add_cascade(label="File", menu=fileMenu)
		#editMenu = Menu(menubar)
		#menubar.add_cascade(label="Edit", menu=editMenu).add_command(label="Universe", command=self.onExit)
		#viewMenu = Menu(menubar)
		#menubar.add_cascade(label="View", menu=editMenu)
		#viewMenu.add_command(label="Graph", command=self.onExit)
		Instruction = tk.Label(self, text = 'Enter Values', font = LARGE_FONT).grid(row = 0, column = 3, sticky = W)
		Redshift = tk.Label(self, text = "Redshift:").grid(row = 1, column = 0, columnspan = 1,  sticky = W)
		RedshiftBlank = Entry(self)
		RedshiftBlank.grid(row = 1, column = 3, columnspan = 1, sticky = W)
		AVGWL = tk.Label(self, text = "Average Wavelength:").grid(row = 2, column = 0, columnspan = 1, sticky = W)
		AVGWLBlank = Entry(self)
		AVGWLBlank.grid(row =2 , column = 3, columnspan = 1, sticky = W)
		ChangeWl= tk.Label(self, text = "Change in Wavelength").grid(row = 3, column = 0, sticky = W)
		ChangeWLBlank = Entry(self)
		ChangeWLBlank.grid(row = 3, column = 3, columnspan = 1, sticky = W)
		Distance = Label(self, text = "Vertical Distance").grid(row = 4, column = 0, sticky = W)
		DistanceBlank = Entry(self)
		DistanceBlank.grid(row = 4, column = 3, columnspan = 1, sticky = W)
		start_Solve = tk.Button(self, text = 'Solve', command = lambda: Solve()).grid(row = 5, column = 3, sticky = W) #This button runs the rotation curve solver #Where the button is on the GUI		#button1.grid(row = 5, column = 2, sticky = W)
		start_Graph = tk.Button(self, text = 'Graph', command = lambda: combine_funcs(Solve(), graph())).grid(row = 5, column = 3, padx = 125, sticky = W) #Graphs the curve on a different grame. Second command brings the frame forward.
		start_Exit = tk.Button(self, text = "Exit", command = lambda: sure()).grid(row = 6, column = 3, padx = 70, sticky = W)
		def sure():
			sure = tk.Tk()
			sure.wm_title("Exit")
			check = tk.Label(sure, text = "Are you sure?", font = LARGE_FONT).grid(row = 0, column = 2, columnspan = 2, sticky = W)
			sure.sure_yes = tk.Button(sure, text = "Yes", command = combine_funcs(sure.destroy, self.quit)).grid(row = 2, column = 3, sticky = W)
			sure_no = tk.Button(sure, text = "No", command = sure.destroy).grid(row = 2, column = 4, sticky =W)
		
		def Solve(): #Popups when pressing solve
			Solve = tk.Toplevel()
			Solve.wm_title("Rotation Curves Client")
			Solve_label = tk.Label(Solve, text = "Results", font = LARGE_FONT).grid(row = 0, column = 0, sticky = W)
			
			label_d = tk.Label(Solve, text = "Angular distance diameter: ", font = LARGE_FONT).grid(row = 1, column = 0 , sticky = W)
			text_d = Text(Solve, width = 25, height = 1, wrap = WORD)
			text_d.grid(row = 1, column = 7, columnspan = 3, rowspan = 1, sticky =W)
			units_d = tk.Label(Solve, text = "meters", font = LARGE_FONT).grid(row = 1, column = 10, sticky = W)
			
			label_v = tk.Label(Solve, text = "Converted vertical distance: ", font = LARGE_FONT).grid(row = 3, column = 0, sticky = W)
			text_v = Text(Solve, width = 25, height = 1, wrap = WORD)
			text_v.grid(row = 3, column = 7, columnspan = 3, rowspan =1, sticky =W)
			units_v = tk.Label(Solve, text = "radians", font = LARGE_FONT).grid(row = 3, column = 10, sticky = W)
			
			label_r = tk.Label(Solve, text = "Galactic Radius: ", font = LARGE_FONT).grid(row = 5, column = 0, sticky = W)
			text_r = Text(Solve, width = 25, height = 1, wrap = WORD)
			text_r.grid(row = 5, column = 7, columnspan = 3, rowspan = 1, sticky =W)
			units_r = tk.Label(Solve, text = "meters", font = LARGE_FONT).grid(row = 5, column = 10, sticky = W)
			
			label_s = tk.Label(Solve, text = "Galactic Rotation Speed: ", font = LARGE_FONT).grid(row = 7, column = 0, sticky = W)
			text_s = Text(Solve, width = 25, height = 1, wrap = WORD)
			text_s.grid(row = 7, column = 7, columnspan = 3, rowspan = 1, sticky =W)
			units_s = tk.Label(Solve, text = "radians per second", font = LARGE_FONT).grid(row = 7, column = 10, sticky = W)
			
			label_m = tk.Label(Solve, text = "Galactic Mass: ", font = LARGE_FONT).grid(row = 9, column = 0, sticky = W)
			text_m = Text(Solve, width = 25, height = 1, wrap = WORD)
			text_m.grid(row = 9, column = 7, columnspan = 3, rowspan = 1, sticky =W)
			units_m = tk.Label(Solve, text = "kilograms", font = LARGE_FONT).grid(row = 9, column = 10, sticky = W)
			
			rs = np.float(RedshiftBlank.get())
			awl = np.float(AVGWLBlank.get())
			cwl = np.float(ChangeWLBlank.get())
			db = np.float(DistanceBlank.get())
			
			Dm = 1130.2
			Da = (Dm/(1+rs))
			Da = Da * (3.0*10**(22))
			vertext = (db * 0.1185 * np.pi) / (3600 * 180)
			radi = (Da * vertext) / 2
			vel = (cwl * sp.c) / (awl * 2)
			mass = (radi * (vel**2)) / sp.G
			
			text_d.insert( '0.0', Da)
			text_v.insert( '0.0', vertext)
			text_r.insert( '0.0', radi)
			text_s.insert( '0.0', vel)
			text_m.insert( '0.0', mass)
			
			Solve_quit = tk.Button(Solve, text = "Quit", command = Solve.destroy).grid(row = 11, column = 0, sticky = W)
		
		def graph():
			graph = tk.Toplevel()
			graph.title("Rotation Curves Client")
			graph_quit = tk.Button(graph, text = "Quit", command = graph.destroy).grid(row = 2, column = 3, sticky = W)
			f = Figure(figsize = (5,5), dpi = 100)
			a = f.add_subplot(111)
			#effect_velocity = [1,vel]
			#effect_radius = [1,radius]
			#effect_mass = mass * (effect_radius)**3 / radius**3
			#effect_velocity = np.sqrt(sp.G * effect_mass / effect_radius)
			#x = effect_radius
			#y = effect_velocity
			a.plot([1,2,3,4,5,6],[1,2,3,4,5,6])
			#a.plot(x,y)
			a.axis([0, 1000000000, 0, 100000000000])
			canvas = tk.FigureCanvasTkAgg(f, self)
			canvas.show()
			canvas.get_tk_widget().pack(side = tk.TOP, fill = tk.BOTH, expand = True)

app = RotationCurves()
app.mainloop()

