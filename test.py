# # from tkinter import *
# from tkinter.filedialog import *
# root = Tk()
# root.title("Save and Load")
# root.geometry("600x500-400+50")

# def importFiles():
#     try:
#         filenames = askopenfilenames()
#         global file
#         for file in filenames:
#             fileList.insert(END, file)
#     except:
#         pass

# def removeFiles():
#     try:
#         fileList.delete(fileList.curselection())
#     except:
#         pass

# def openFile():
#     try:
#         text.delete(END)
#         fob = open(file, 'r')
#         text.insert(0.0, fob.read())
#     except:
#         pass

# def saveFile():
#     try:
#         fob = open(file, 'w')
#         fob.write(text.get(0.0, 'end-1c'))
#         fob.close()
#     except:
#         pass

# listFrame = Frame(root)
# listFrame.pack()

# sby = Scrollbar(listFrame, orient='vertical')
# sby.pack(side=RIGHT, fill=Y)

# fileList = Listbox(listFrame, width=100, height=5, yscrollcommand=sby.set)
# fileList.pack()

# sby.config(command=fileList.yview)

# buttonFrame = Frame(root)
# buttonFrame.pack()

# importButton = Button(buttonFrame, text="Import", command=importFiles)
# importButton.pack(side=LEFT)

# removeButton = Button(buttonFrame, text="Remove", command=removeFiles)
# removeButton.pack(side=LEFT)

# openButton = Button(buttonFrame, text="Open", command=openFile)
# openButton.pack(side=LEFT)

# saveButton = Button(buttonFrame, text="Save", command=saveFile)
# saveButton.pack(side=LEFT)

# text = Text(root)
# text.pack()

# root.mainloop()

#___________________________________________________________________

# from collections import deque
#
# # you can initialize a deque with a list
# numbers = deque()
#
# # Use append like before to add elements
# numbers.append(99)
# numbers.append(15)
# numbers.append(82)
# numbers.append(50)
# numbers.append(47)
#
# # You can pop like a stack
# last_item = numbers.pop()
# print(last_item) # 47
# print(numbers) # deque([99, 15, 82, 50])
#
# # You can dequeue like a queue
# first_item = numbers.popleft()
# print(first_item) # 99
# print(numbers) # deque([15, 82, 50])


from tkinter import *
from time import sleep

textFont1 = ("Arial", 10, "bold italic")
textFont2 = ("Arial", 16, "bold")
textFont3 = ("Arial", 8, "bold")


class LabelWidget(Entry):
    def __init__(self, master, x, y, text):
        self.text = StringVar()
        self.text.set(text)
        Entry.__init__(self, master=master)
        self.config(relief="ridge", font=textFont1,
                    bg="#ffffff000", fg="#000000fff",
                    readonlybackground="#ffffff000",
                    justify='center', width=8,
                    textvariable=self.text,
                    state="readonly")
        self.grid(column=x, row=y)


class EntryWidget(Entry):
    def __init__(self, master, x, y):
        Entry.__init__(self, master=master)
        self.value = StringVar()
        self.config(textvariable=self.value, width=8,
                    relief="ridge", font=textFont1,
                    bg="#ddddddddd", fg="#000000000",
                    justify='center')
        self.grid(column=x, row=y)
        self.value.set("")


class EntryGrid(Tk):
    ''' Dialog box with Entry widgets arranged in columns and rows.'''

    def __init__(self, colList, rowList, title="Entry Grid"):
        self.cols = colList[:]
        self.colList = colList[:]
        self.colList.insert(0, "")
        self.rowList = rowList
        Tk.__init__(self)
        self.title(title)

        self.mainFrame = Frame(self)
        self.mainFrame.config(padx='3.0m', pady='3.0m')
        self.mainFrame.grid()
        self.make_header()

        self.gridDict = {}
        for i in range(1, len(self.colList)):
            for j in range(len(self.rowList)):
                w = EntryWidget(self.mainFrame, i, j + 1)
                self.gridDict[(i - 1, j)] = w.value

                def handler(event, col=i - 1, row=j):
                    return self.__entryhandler(col, row)

                w.bind(sequence="<FocusOut>", func=handler)
        self.mainloop()

    def make_header(self):
        self.hdrDict = {}
        for i, label in enumerate(self.colList):
            def handler(event, col=i, row=0, text=label):
                return self.__headerhandler(col, row, text)

            w = LabelWidget(self.mainFrame, i, 0, label)
            self.hdrDict[(i, 0)] = w
            w.bind(sequence="<KeyRelease>", func=handler)

        for i, label in enumerate(self.rowList):
            def handler(event, col=0, row=i + 1, text=label):
                return self.__headerhandler(col, row, text)

            w = LabelWidget(self.mainFrame, 0, i + 1, label)
            self.hdrDict[(0, i + 1)] = w
            w.bind(sequence="<KeyRelease>", func=handler)

    def __entryhandler(self, col, row):
        s = self.gridDict[(col, row)].get()
        if s.upper().strip() == "EXIT":
            self.destroy()
        elif s.upper().strip() == "DEMO":
            self.demo()
        elif s.strip():
            print
            s

    def demo(self):
        ''' enter a number into each Entry field '''
        for i in range(len(self.cols)):
            for j in range(len(self.rowList)):
                sleep(0.25)
                self.set(i, j, "")
                self.update_idletasks()
                sleep(0.1)
                self.set(i, j, i + 1 + j)
                self.update_idletasks()

    def __headerhandler(self, col, row, text):
        ''' has no effect when Entry state=readonly '''
        self.hdrDict[(col, row)].text.set(text)

    def get(self, x, y):
        return self.gridDict[(x, y)].get()

    def set(self, x, y, v):
        self.gridDict[(x, y)].set(v)
        return v


if __name__ == "__main__":
    cols = ['A', 'B', 'C', 'D']
    rows = ['1', '2', '3', '4']
    app = EntryGrid(cols, rows)

