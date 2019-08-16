from tkinter import *
from tkinter import filedialog
import model,configurations,controller
from model.complexity import *
from model.inheritence import *
from model.ControlStuctureAndNestedControl import *
from model.size import *


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

        self.classListFrame = Frame(self.root)
        self.classListFrame.pack(side=LEFT,fill=Y)

        self.classListLabel = Label(self.classListFrame,text="Class List",bg='yellow')
        self.classListLabel.pack()
        self.classList = Listbox(self.classListFrame,selectmode=SINGLE)
        self.classList.bind('<<ListboxSelect>>',self.class_on_selet)
        self.classList.pack()

        self.codeCanvas = Canvas(self.root)
        self.codeFrame = Frame(self.codeCanvas)

        self.codeFrame.pack(side=LEFT,fill=Y)

        self.scrollBar = Scrollbar(self.root, orient="vertical", command=self.codeCanvas.yview)
        self.scrollBar.pack(side=RIGHT, fill=Y)
        self.scrollBar.config(command=self.codeCanvas.yview)
        self.codeCanvas.config(yscrollcommand=self.scrollBar.set)
        self.codeCanvas.pack(fill='both', expand=True, side='left')

    def class_on_selet(self,evt):
        for item in self.codeFrame.winfo_children():
            item.destroy()
        class_index = self.classList.curselection()[0]
        self.viewSourceCode(class_index)

    def viewSourceCode(self,index):
        selected_class = self.srcComplexity.classList[index]
        complexity_of_inheritance = calCi(selected_class,self.srcComplexity.classList)
        entries =[]
        count = 0

        Label(self.codeFrame, text="Code List", justify=LEFT, width=80, anchor="w", bg='yellow').grid(row=0, column=0)
        Label(self.codeFrame, text="s", justify=LEFT, width=2, anchor="w", bg='yellow').grid(row=0, column=1)
        Label(self.codeFrame, text="tc", justify=LEFT, width=2, anchor="w", bg='yellow').grid(row=0, column=2)
        Label(self.codeFrame, text="nc", justify=LEFT, width=2, anchor="w", bg='yellow').grid(row=0, column=3)
        Label(self.codeFrame, text="i", justify=LEFT, width=2, anchor="w", bg='yellow').grid(row=0, column=4)
        Label(self.codeFrame, text="TW", justify=LEFT, width=2, anchor="w", bg='yellow').grid(row=0, column=5)
        Label(self.codeFrame, text="ps", justify=LEFT, width=2, anchor="w", bg='yellow').grid(row=0, column=6)
        Label(self.codeFrame, text="cr", justify=LEFT, width=2, anchor="w", bg='yellow').grid(row=0, column=7)
        for i,atr in enumerate(selected_class.getAttributeList()):
            # entries.append(Entry(self.codeFrame,width=50))
            # entries[i].grid(row=i,column=0)
            # entries[i].insert(0,atr)
            complexity_of_tc = identifyControlStructure(atr)
            complexity_of_size = sizeComplexity(atr)

            row_value = i+1
            Label(self.codeFrame,text=atr,justify=LEFT,width=80,anchor="w").grid(row=row_value,column=0,sticky=W)
            Label(self.codeFrame,text=complexity_of_size,justify=LEFT,width=2,anchor="w").grid(row=row_value,column=1)
            Label(self.codeFrame, text=str(complexity_of_tc), justify=LEFT, width=2, anchor="w").grid(row=row_value, column=2)
            Label(self.codeFrame, text="nc", justify=LEFT, width=2, anchor="w").grid(row=row_value, column=3)
            Label(self.codeFrame, text=str(complexity_of_inheritance), justify=LEFT, width=2, anchor="w").grid(row=row_value, column=4)
            Label(self.codeFrame, text="TW", justify=LEFT, width=2, anchor="w").grid(row=row_value, column=5)
            Label(self.codeFrame, text="ps", justify=LEFT, width=2, anchor="w").grid(row=row_value, column=6)
            Label(self.codeFrame, text="cr", justify=LEFT, width=2, anchor="w").grid(row=row_value, column=7)
            count += 1

        for i,meth in enumerate(selected_class.methodList):
            #function name title
            count +=2
            l_text = str(i+1)+". Function Name - "+meth.methodName
            Label(self.codeFrame,text=l_text,justify=LEFT,width=80,bg="light blue").grid(row=i+count,column=0,sticky=W)
            rc = 1
            if meth.hasRecurtion():
                rc = 2
            for j,line in enumerate(meth.getCodeListLineByLine()):
                count +=1
                row_value = i + count
                complexity_of_tc = identifyControlStructure(line)
                complexity_of_size = sizeComplexity(line)
                Label(self.codeFrame, text=line, justify=LEFT, width=80, anchor="w").grid(row=row_value, column=0,
                                                                                         sticky=W)
                Label(self.codeFrame, text=complexity_of_size, justify=LEFT, width=2, anchor="w").grid(row=row_value, column=1)
                Label(self.codeFrame, text=str(complexity_of_tc), justify=LEFT, width=2, anchor="w").grid(row=row_value, column=2)
                Label(self.codeFrame, text="nc", justify=LEFT, width=2, anchor="w").grid(row=row_value, column=3)
                Label(self.codeFrame, text=str(complexity_of_inheritance), justify=LEFT, width=2, anchor="w").grid(
                    row=row_value, column=4)
                Label(self.codeFrame, text="TW", justify=LEFT, width=2, anchor="w").grid(row=row_value, column=5)
                Label(self.codeFrame, text="ps", justify=LEFT, width=2, anchor="w").grid(row=row_value, column=6)
                Label(self.codeFrame, text=str(rc), justify=LEFT, width=2, anchor="w").grid(row=row_value, column=7)






    def openFile(self):
        self.srcFile = filedialog.askopenfilename(title="Select your source code",
                                                  filetype=(("java", "*.java"), ("C++", "*.cpp"), ("text", "*.txt")))
        self.classList.delete(0,END)

        self.root.title(self.srcFile + " - ComplexityCounter")  # Returning the basename of 'file'
        self.srcFile = open(self.srcFile, "r")
        self.srcComplexity = CodeFactory(self.srcFile.read())
        for i,Cls in enumerate(self.srcComplexity.classList):
            self.classList.insert(i,Cls.className)
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



