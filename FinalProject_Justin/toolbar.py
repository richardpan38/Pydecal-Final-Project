from tkinter import *


class Example(Frame):

    def __init__(self,*args, **kwargs):
        Frame.__init__(self, *args, **kwargs)          
    def UI(self):
      
        self.parent.title("Menu")
        
        menubar = Menu(self.parent)
        self.parent.config(menu=menubar)
        
        fileMenu = Menu(menubar)
        fileMenu.add_command(label="Exit", command=self.onExit)
        fileMenu.add_command(label="Save", command=self.filewrite)
        menubar.add_cascade(label="File", menu=fileMenu)
        
        editMenu = Menu(menubar)
        menubar.add_cascade(label="Edit", menu=editMenu)
        editMenu.add_command(label="Universe", command=self.onExit)

        viewMenu = Menu(menubar)
        menubar.add_cascade(label="View", menu=editMenu)
        viewMenu.add_command(label="Graph", command=self.onExit)


    def onExit(self):
        self.quit()

    def filewrite(self):
        writeFile()

#def writeFile(textObj):
        #file = open("data.txt")
        #file.write(textFile2)
        #textObj.insert(INSERT, file.read())
        #file.close()    

app = Example()
app.mainloop()