from tkinter import *
from tkinter import ttk
root = Tk()
root.geometry("900x600")
root.title("Project 1")

gui_elements = ["Label","Dropdown","Button"]
dropdown = ttk.Combobox(root, state="readonly", values = gui_elements)
dropdown.pack()

class CreateElements:
    
    def __init__(self):
        print("This is CreateElemnents Class")
        
    
    def createLabel(self):
        label = Label(root,text="A new Label is being created using class" , fg="red")
        label.pack()
        
    
    def createButton(self):
        button = Button(root,text="Button", command= self.message)
        class_btn.pack(padx="20",pady="10")
        
    
    
    def createDropdown(self):
        value = [1,2,3,4]
        class_dropdown = ttk.Combobox(root, state="readonly", values = values)
        class_dropdown.pack()
        
        
    def choose(self):
        global dropdown
        element = dropdown.get()
        if(element=="Label"):
            self.createLabel()
        elif(element=="Button"):
            self.createButton()
        elif(element=="Dropdown"):
                self.createDropdown()
        
        
    def message(self):
        messagebox.showinfo("showinfo","You clicked the button created using class")
        
        obj_of_createElements= createElements()
        btn = Button(root,text="Create ELement", command= obj_of_createElements.choose)
        btn.pack(padx=20,pady=10)
        
        
        root.mainloop()