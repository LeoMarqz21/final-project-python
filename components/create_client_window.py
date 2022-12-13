import re
import helpers
import database as db
from tkinter import *
from components.center_widget_mixin import CenterWidgetMixin


class CreateClientWindow(Toplevel, CenterWidgetMixin):
    def __init__(self, parent):
        super().__init__(parent)
        self.title('Crear cliente')
        self.build()
        self.center()
        self.transient(parent)
        self.grab_set() #impide usar la ventana padre mientras no cerremos esta.
        
    def build(self):
        frame = Frame(self)
        frame.pack(padx=20, pady=10)
        
        Label(frame, text='Id [2:int, 1:char, 2:int]').grid(row=0, column=0, padx=3)
        Label(frame, text='Nombre [min:3, max:30]').grid(row=0, column=1, padx=3)
        Label(frame, text='Apellido [min:3, max:30]').grid(row=0, column=2, padx=3)
        Label(frame, text='Email [min:3, max:120]').grid(row=0, column=3, padx=3)
        
        id = Entry(frame, textvariable=StringVar())
        id.grid(row=1, column=0, padx=3)
        id.bind('<KeyRelease>', lambda event: self.validate(event=event, field='id') )
        
        name = Entry(frame, textvariable=StringVar())
        name.grid(row=1, column=1, padx=3)
        name.bind('<KeyRelease>', lambda event: self.validate(event=event, field='name') )
        
        lastname = Entry(frame, textvariable=StringVar())
        lastname.grid(row=1, column=2, padx=3)
        lastname.bind('<KeyRelease>', lambda event: self.validate(event=event, field='lastname') )
        
        email = Entry(frame, textvariable=StringVar())
        email.grid(row=1, column=3, padx=3)
        email.bind('<KeyRelease>', lambda event: self.validate(event=event, field='email') )
        
        frame = Frame(self)
        frame.pack(pady=10)
        
        create = Button(frame, text='Guardar', command=self.createClient)
        create.config(state=DISABLED)
        create.grid(row=0, column=1)
        Button(frame, text='Cancelar', command=self.closeWindow).grid(row=0, column=2)
        
        self.id = id
        self.name = name
        self.lastname = lastname
        self.email = email
        self.validations = {"id":False, "name":False, "lastname":False, "email":False}
        self.btnCreate = create
        
        
    def createClient(self):
        print(self.id.get(), self.name.get(), self.lastname.get(), self.email.get())
        self.master.treeview.insert(
            parent='', index='end', iid=self.id.get(), 
            values=(self.id.get(), self.name.get(), self.lastname.get(), self.email.get())
        )
        self.closeWindow()
    
    def closeWindow(self):
        self.destroy()
        self.update()
    
    def validate(self, event = None, field:str = None):
        value = event.widget.get()
        if field == 'id':
            isValid = helpers.validateId(id=value, clients=db.Clients.lst)
        elif field == 'name' or field == 'lastname':
            isValid = value.isalpha() and len(value) >= 3 and len(value) <= 30 and value == value.capitalize()
        elif field == 'email':
            isValid = len(value) >= 3 and len(value) <= 120 and '@' in value and '.' in value
            
        event.widget.configure({"bg":"green"}) if isValid else event.widget.configure({"bg":"red"})
        print(self.validations)
        self.validations[field] = isValid
        self.btnCreate.config(
            state=NORMAL if self.validations  == {"id":True, "name":True, "lastname":True, "email":True} \
                else DISABLED
                )
        
                