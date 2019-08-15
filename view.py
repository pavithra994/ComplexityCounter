from tkinter import *
from tkinter import filedialog
import model,configurations,controller
from model.complexity import *


class MainWindow():
    def __init__(self):
        self.root = Tk()
        self.root.title("ComplexityCounter | Complexity measuring tool")
        self.root.minsize(640,400)

        self.topFrame = Frame(self.root)
        self.topFrame.pack(side=TOP)

        self.browseLabel = Label(self.topFrame,text="Insert your source file")
        self.browseLabel.pack(side=LEFT)

        self.browseButton = Button(self.topFrame,text="Browse",command=self.openFile)
        self.browseButton.pack()

        self.textBox = Text(self.root, height=5)
        self.scrollBar = Scrollbar(self.root)
        self.textBox.pack(side=LEFT,fill=Y)
        self.scrollBar.pack(side=RIGHT,fill=Y)
        self.scrollBar.config(command=self.textBox.yview)
        self.textBox.config(yscrollcommand=self.scrollBar.set)




    def viewSourceCode(self):
        self.srcComplexity = CodeFactory(self.srcFile.read())
        print(self.srcComplexity)
        self.textBox.insert(END,str(self.srcComplexity))





    def openFile(self):
        self.srcFile = filedialog.askopenfilename(title="Select your source code",
                                                  filetype=(("java", "*.java"), ("C++", "*.cpp"), ("text", "*.txt")))
        # self.labelFileName = Label(self.upperFrame,text="")
        # self.labelFileName.grid(column=2,row=2,padx=20,pady=20)
        # self.labelFileName.configure(text=self.srcFile)
        # self.srcViewer(self.srcFile)
        self.root.title(self.srcFile + " - pyPad")  # Returning the basename of 'file'
        # self.textPad.delete(1.0, END)
        self.srcFile = open(self.srcFile, "r")
        self.viewSourceCode()
        # self.textPad.insert(1.0, self.srcFile.read())
        self.srcFile.close()
        # self.update_line_number()

    # def srcViewer(self,code):
    #     x = 1
    #     for line in open(code,"r").readlines():
    #         Label(self.codeAreaFrame,text=x).grid(column=1,row=x)
    #         Label(self.codeAreaFrame,text=line.split()).grid(column=2,row=x)
    #         x +=1

    # Displaying Line Numbers
    def update_line_number(self,event=None):
        endline, endcolumn = self.textPad.index('end-1c').split('.')
        txt = '\n'.join(map(str, range(1, int(endline))))
        self.lnlabel.config(text=txt, anchor='nw')


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



