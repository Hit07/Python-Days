from tkinter import *
window = Tk()
window.title("First GUI")
window.minsize(width=300,height=400)
window.config(padx=20,pady=10)
def button_clicked():
    my_label.config(text=input_1.get())

# Label
my_label = Label(text="Label",font=("Arial", 14, "bold"))
my_label.grid(column= 0,row=0)
# my_label["text"] = "New Label"
# my_label.config(text="New Label")

new_button = Button(text="click")
new_button.grid(column=3,row=0)

button = Button(text="Click here",command=button_clicked)
button.grid(column=2,row=2)
# Entry
input_1 = Entry(width=10)
input_1.grid(column=4,row=4)
# for displaying we have pack,place and grid
# input1.pack()
# input1.place()
# input1.grid()
mainloop()
#----------------------------------------------------------


# #Creating a new window and configurations
# window = Tk()
# window.title("Widget Examples")
# window.minsize(width=500, height=500)
#
# #Labels
# label = Label(text="This is old text")
# label.config(text="This is new text")
# label.pack()
#
# #Buttons
# def action():
#     print("Do something")
#
# #calls action() when pressed
# button = Button(text="Click Me", command=action)
# button.pack()
#
# #Entries
# entry = Entry(width=30)
# #Add some text to begin with
# entry.insert(END, string="Some text to begin with.")
# #Gets text in entry
# print(entry.get())
# entry.pack()
#
# #Text
# text = Text(height=5, width=30)
# #Puts cursor in textbox.
# text.focus()
# #Adds some text to begin with.
# text.insert(END, "Example of multi-line text entry.")
# #Get's current value in textbox at line 1, character 0
# print(text.get("1.0", END))
# text.pack()
#
# #Spinbox
# def spinbox_used():
#     #gets the current value in spinbox.
#     print(spinbox.get())
# spinbox = Spinbox(from_=0, to=10, width=5, command=spinbox_used)
# spinbox.pack()
#
# #Scale
# #Called with current scale value.
# def scale_used(value):
#     print(value)
# scale = Scale(from_=0, to=100, command=scale_used)
# scale.pack()
#
# #Checkbutton
# def checkbutton_used():
#     #Prints 1 if On button checked, otherwise 0.
#     print(checked_state.get())
# #variable to hold on to checked state, 0 is off, 1 is on.
# checked_state = IntVar()
# checkbutton = Checkbutton(text="Is On?", variable=checked_state, command=checkbutton_used)
# checked_state.get()
# checkbutton.pack()
#
# #Radiobutton
# def radio_used():
#     print(radio_state.get())
# #Variable to hold on to which radio button value is checked.
# radio_state = IntVar()
# radiobutton1 = Radiobutton(text="Option1", value=1, variable=radio_state, command=radio_used)
# radiobutton2 = Radiobutton(text="Option2", value=2, variable=radio_state, command=radio_used)
# radiobutton1.pack()
# radiobutton2.pack()
#
#
# #Listbox
# def listbox_used(event):
#     # Gets current selection from listbox
#     print(listbox.get(listbox.curselection()))
#
# listbox = Listbox(height=4)
# fruits = ["Apple", "Pear", "Orange", "Banana"]
# for item in fruits:
#     listbox.insert(fruits.index(item), item)
# listbox.bind("<<ListboxSelect>>", listbox_used)
# listbox.pack()
# window.mainloop()




#-------------------------------------------------------------------------------------
# """Unlimited positional arguments of type tuple"""
#
#
# def add(*args):
#     sum1 = 0
#     for n in args:
#         sum1 += n
#     print(sum1)
#
#
# add(2, 3, 4, 5, 6)
#
# '''Unlimited keyword arguments of type dict'''
#
#
# def calculate(**kw):
#     print(kw["add"])
#
#
# calculate(add=2, mul=3)
#
#
# # window.mainloop()
#
# class Man:
#     def __init__(self, **kw):
#         # use of .get("") is similar as using kw[""] but if key is not present is returns none
#         self.move = kw.get("move")
#         self.sit = kw["sit"]
#
#
# man = Man(move="Bengaluru",sit="nearby")
# print(man.move,man.sit)
