import csv
import config

class Client:
    def __init__(self, id:str, name:str, lastname:str, email:str) -> None:
        self.id = id
        self.name = name
        self.lastname = lastname
        self.email = email
        
    def __str__(self) -> str:
        return f'({self.id}) {self.name} {self.lastname} {self.email}'
    

class Clients:
    lst = []
    with open(config.DATABASE_PATH, newline='\n') as file:
        reader = csv.reader(file, delimiter=';')
        for Id,Name,Lastname,Email in reader:
            client = Client(Id, Name, Lastname, Email)
            lst.append(client)

    @staticmethod
    def findById(id:str) -> Client:
        for client in Clients.lst:
            if client.id == id:
                return client
    
    @staticmethod
    def create(id:str, name:str, lastname:str, email:str) -> Client:
        client = Client(id, name, lastname, email)
        Clients.lst.append(client)
        Clients.save()
        return client
        
    @staticmethod
    def update(id:str, name:str, lastname:str, email:str) -> Client:
        for index, client in enumerate(Clients.lst):
            if client.id == id:
                Clients.lst[index].name = name
                Clients.lst[index].lastname = lastname
                Clients.lst[index].email = email
                Clients.save()
                return Clients.lst[index]
    
    @staticmethod
    def delete(id:str) -> Client:
        for index, client in enumerate(Clients.lst):
            if client.id == id:
                clt = Clients.lst.pop(index)
                Clients.save()
                return clt
    
    @staticmethod
    def save():
        with open(config.DATABASE_PATH, 'w', newline='\n') as file:
            writer = csv.writer(file, delimiter=';')
            for client in Clients.lst:
                writer.writerow([client.id, client.name, client.lastname, client.email])