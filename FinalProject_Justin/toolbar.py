from tkinter import Tk, Frame, Menu



class Example(Frame):

    def __init__(self, parent):
        Frame.__init__(self, parent)   
         
        self.parent = parent        
        self.UI()
        
        
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

def main():
  
    root = Tk()
    root.geometry("250x150+300+300")
    app = Example(root)
    root.mainloop()  


if __name__ == '__main__':
    main()    