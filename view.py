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
        self.topFrame.pack(side=LEFT)

        self.browseLabel = Label(self.topFrame,text="Insert your source file")
        self.browseLabel.pack(side=LEFT)

        self.browseButton = Button(self.topFrame,text="Browse",command=self.openFile())
        self.browseButton.pack()

        # menu bar
        # self.menubar = Menu(self.root)
        #
        # self.filemenu = Menu(self.menubar, tearoff=0)
        # self.filemenu.add_command(label="New", accelerator='Ctrl+N', compound=LEFT, underline=0)
        # self.filemenu.add_command(label="Open", accelerator='Ctrl+O', compound=LEFT, underline=0, command= self.openFile)
        # self.filemenu.add_command(label="Save", accelerator='Ctrl+S', compound=LEFT, underline=0)
        # self.filemenu.add_command(label="Save as", accelerator='Shift+Ctrl+S')
        # self.filemenu.add_separator()
        # self.filemenu.add_command(label="Exit", accelerator='Alt+F4')
        # self.menubar.add_cascade(label="File", menu=self.filemenu)
        #
        # # self.editmenu = Menu(self.menubar, tearoff=0)
        # # self.menubar.add_cascade(label="Edit", menu=self.editmenu)
        # #
        # # self.viewmenu = Menu(self.menubar, tearoff=0)
        # # self.menubar.add_cascade(label="View", menu=self.viewmenu)
        #
        # self.aboutmenu = Menu(self.menubar, tearoff=0)
        # self.aboutmenu.add_command(label="About")
        # self.aboutmenu.add_command(label="Help")
        # self.menubar.add_cascade(label="About", menu=self.aboutmenu)
        #
        # self.root.config(menu=self.menubar)
        #
        # # shortcut bar
        # self.shortcutbar = Frame(self.root, height=50, bg='light sea green')
        # self.shortcutbar.pack(expand=NO, fill=X)
        # # line number bar left corner
        # self.lnlabel = Label(self.root, width=2, bg='antique white')
        # self.lnlabel.pack(side=LEFT, anchor='nw', fill=Y)
        # # complexity statics bar
        # self.staticFrame = Frame(self.root, width=100, bg='red')
        # self.staticFrame.pack(side=RIGHT, anchor='ne', fill=Y)
        #
        # self.textPad = Text(self.root)
        # self.textPad.pack(expand=YES, fill=BOTH)
        # self.scroll = Scrollbar(self.textPad)
        # self.textPad.configure(yscrollcommand=self.scroll.set)
        # self.scroll.config(command=self.textPad.yview)
        # self.scroll.pack(side=RIGHT, fill=Y)
        # self.textPad.bind("<Any-KeyPress>", self.update_line_number)


        # self.upperFrame = Frame(self.root)
        # self.upperFrame.pack(fill=X)
        # self.codeAreaFrame = Frame(self.root)
        # self.codeAreaFrame.pack(side=LEFT,fill=X)
        # self.codeAreaFrame.place(relwidth=0.8, y=250, anchor=W )
        #
        # self.labelFileOpen = Label(self.upperFrame, text="Select your source code")
        # self.labelFileOpen.grid(column=0,row=1,padx=20,pady=20)
        # self.buttonBrowse()

    # def buttonBrowse(self):
    #     self.browseBtn = Button(self.upperFrame, text="Browse", command= self.openFile)
    #     self.browseBtn.grid(column=1,row=1,padx=20,pady=20)

    def viewSourceCode(self):
        self.srcComplexity = CodeFactory(self.srcFile.read())
        print(self.srcComplexity)




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



