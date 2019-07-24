from tkinter import *
from tkinter import filedialog


class MainWindow():
    def __init__(self):
        self.root = Tk()
        self.root.title("ComplexityCounter | Complexity measuring tool")
        self.root.minsize(640,400)

        self.upperFrame = Frame(self.root)
        self.upperFrame.pack(fill=X)
        self.codeAreaFrame = Frame(self.root)
        self.codeAreaFrame.pack(side=LEFT,fill=X)

        self.labelFileOpen = Label(self.upperFrame, text="Select your source code")
        self.labelFileOpen.grid(column=0,row=1,padx=20,pady=20)
        self.buttonBrowse()

    def buttonBrowse(self):
        self.browseBtn = Button(self.upperFrame, text="Browse", command= self.openFile)
        self.browseBtn.grid(column=1,row=1,padx=20,pady=20)

    def openFile(self):
        self.srcFile = filedialog.askopenfilename(title="Select your source code",
                                                  filetype=(("java", "*.java"), ("C++", "*.cpp"), ("text", "*.txt")))
        self.labelFileName = Label(self.upperFrame,text="")
        # self.labelFileName.grid(column=2,row=2,padx=20,pady=20)
        # self.labelFileName.configure(text=self.srcFile)
        self.srcViewer(self.srcFile)

    def srcViewer(self,code):
        x = 1
        for line in open(code,"r").readlines():
            Label(self.codeAreaFrame,text=x).grid(column=1,row=x)
            Label(self.codeAreaFrame,text=line.split()).grid(column=2,row=x)
            x +=1



if __name__ == '__main__':
    runApp = MainWindow()
    runApp.root.mainloop()





# root = Tk()
#
# label = Label(root, text="Complexity Counter")
# label.pack()
# f = open("testString.java", "r")
# l = f.readlines()
# f.close()
# for line in l:
#     Label(root, text=line.split()).pack()
#
#
# root.mainloop()



