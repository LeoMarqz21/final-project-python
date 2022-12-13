from tkinter import *
from tkinter import ttk
from tkinter.messagebox import askokcancel, WARNING 
from components.center_widget_mixin import CenterWidgetMixin
from components.create_client_window import CreateClientWindow
from components.update_client_window import UpdateClientWindow
import database as db

class MainWindow(Tk, CenterWidgetMixin):
    def __init__(self) -> None:
        super().__init__()
        self.title("Gestor de clientes")
        self.build()
        self.center()
    
    def build(self):
        frame = Frame(self)
        frame.pack()
        treeView = ttk.Treeview(frame)
        treeView['columns'] = ("Id", "Nombre", "Apellido", "Email")
        
        treeView.column("#0", width=0, stretch=NO)
        treeView.column("Id", anchor=CENTER)
        treeView.column("Nombre", anchor=CENTER)
        treeView.column("Apellido", anchor=CENTER)
        treeView.column("Email", anchor=CENTER)
        
        treeView.heading("Id", text='Id', anchor=CENTER)
        treeView.heading("Nombre", text='Nombre', anchor=CENTER)
        treeView.heading("Apellido", text='Apellido', anchor=CENTER)
        treeView.heading("Email", text='Email', anchor=CENTER)
        
        scrollbar = Scrollbar(frame)
        scrollbar.pack(side=RIGHT, fill=Y)
        
        treeView['yscrollcommand'] = scrollbar.set
        
        for client in db.Clients.lst:
            treeView.insert(
                parent='', index='end', iid=client.id, 
                values=(client.id, client.name, client.lastname, client.email)
            )
        
        treeView.pack()
        
        footer = Frame(self)
        footer.pack(pady=20)
        
        Button(footer, text="Crear registro", command=self.create).grid(row=0, column=0, sticky=W)
        Button(footer, text="Modificar registro", command=self.edit).grid(row=0, column=1, sticky=W)
        Button(footer, text="Eliminar registro", command=self.delete).grid(row=0, column=2, sticky=W)
        
        self.treeview = treeView
        
    def delete(self):
        client = self.treeview.focus()
        if client:
            fields = self.treeview.item(client, 'values')
            confirm = askokcancel(
                title='Confirmar borrado', 
                message='Está seguro que desea eliminar este registro ({} - {})?'.format(fields[0], fields[1]),
                icon=WARNING)
            if confirm:
                self.treeview.delete(client)
                db.Clients.delete(fields[0])
        
    def create(self):
        CreateClientWindow(self)
        
    def edit(self):
        if self.treeview.focus():
            UpdateClientWindow(self)
    

if __name__ == '__main__':
    app = MainWindow()
    app.mainloop()
