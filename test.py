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

from collections import deque
import re

# you can initialize a deque with a list 
numbers = deque()

# Use append like before to add elements
numbers.append(99)
numbers.append(15)
numbers.append(82)
numbers.append(50)
numbers.append(47)

# You can pop like a stack
last_item = numbers.pop()
print(last_item) # 47
print(numbers) # deque([99, 15, 82, 50])

# You can dequeue like a queue
first_item = numbers.popleft()
print(first_item) # 99
print(numbers) # deque([15, 82, 50])

t = '        if((number && 0) ||(number||1)){'
func_set = re.findall('\w*\s*\(.*\)', t)
for func in func_set:
    func_name = func.split('(',1)[0].strip()
    func_condition = func.split('(',1)[1].strip()
    condition_set = re.findall('&&|\|\|',func_condition)






