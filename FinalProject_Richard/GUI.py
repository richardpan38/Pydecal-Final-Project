#2 frames.
#frame 1 will have space to insert numbers on the left side. Set these numbers to a variable that will be part of the program later on.
#Buttons in frame 1 to run the program and print the results on the right side.
#Redshift, average wavelength, change in wavelength, vertical extent as blanks
#Right side print values
#Another button to graph onto frame 2
#Frame 2 will show a graph of the values
import tkinter as tk
import matplotlib 
matplotlib.use("TkAgg")
from matplotlib.backends.backend_TkAgg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure 

LARGE_FONT = ("Verdana", 12)

class RotationCurves(Frame):
	def __init__(self):
		Frame.__init(self,master)
		container = tk.Frame(self)
		container.pack(side = 'top', fill = 'both', expand = True)
		container.grid_rowconfigure(0, weight = 1)
		container.grid_columnconfigure(0, weight = 1)
		self.Frame = ()
		for F in (StartPage, PageOne): 

			frame = F(container, self)
			self.Frame[F] = frame
			frame.grid(row = 0, column = 0, sticky = "nsew")
		self.show_frame(StartPage)


	def show_frame(self, cont):
		frame = self.Game[cont]
		frame.tkraise()

class StartPage(tk.Frame):
	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		label = tk.Label(self, text = 'Rotation Curves', font = LARGE_FONT)
		label.grid()
		button1 = tk.Button(self, text = 'Solve') #This button runs the rotation curve solver
		button1.grid() #Where the button is on the GUI
		button2 = tk.Button(self, text = 'Graph', command = lambda: controller.show_frame(PageOne)) #Graphs the curve on a different grame. Second command brings the frame forward.
class PageOne(tk.Frame):
	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		laebl =tk.Label(self, text = 'Graph' , font = LARGE_FONT)
		label.pack(pady=10, padx=10)
		f = Figure(figsize = (5,5), dpi = 100)
		canvas = FigureCanvasTkAgg(f, self)
		canvas.show()
		canvas .get_tk_widget().pack(side = tk.TOP, fill = tk.BOTH, expand = True)


app = RotationCurves()
app.mainloop()

