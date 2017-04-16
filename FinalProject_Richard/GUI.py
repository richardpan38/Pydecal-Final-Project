import tkinter as tk

LARGE_FONT = ("Verdana", 12)

class RotationCurves(Game):
	def __init__(self):
		Game.__init(self,master)
		container = tk.Game(self)
		container.pack(side = 'top', fill = 'both', expand = True)
		container.grid_rowconfigure(0, weight = 1)
		container.grid_columnconfigure(0, weight = 1)
		self.Game = ()
		for F in (StartPage, PageOne): 

			frame = F(container, self)
			self.Game[F] = frame
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
class StartPage(tk.Frame):
	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		laebl =tk.Label(self, text = 'Graph' , font = LARGE_FONT)
		label.grid()


app = RotationCurves()
app.mainloop()

