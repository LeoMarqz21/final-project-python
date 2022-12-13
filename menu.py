import os
import helpers
import database as db
from time import sleep

def start():
    while True:
    #    helpers.cleanScreen()
       print('==========================')     
       print('   Bienvenido al Gestor   ') 
       print('==========================')      
       print(
           '[1] Listar clientes \n' +
           '[2] Buscar cliente \n' +
           '[3] Añadir cliente \n' +
           '[4] Modificar cliente \n' +
           '[5] Eliminar cliente \n' +
           '[6] Salir \n'
       )
       choice = input('>>> ')  
          
       helpers.cleanScreen()
       
       if choice == '1':
           print('Listando clientes\n')
           if len(db.Clients.lst) == 0:
               print('\tNo hay clientes disponibles')
           for client in db.Clients.lst:
               print(client)
           print('')
       elif choice == '2':
           print('Buscando cliente...')
           clientId = helpers.readInput(5,5, '2:int, 1:char, 2:int >> 45F77').upper()
           client = db.Clients.findById(clientId)
           print(client) if client is not None else print('Client not found')
       elif choice == '3':
           print('Añadiendo cliente')
           Id = None
           while True:
               Id = helpers.readInput(5,5, 'Id= 2:int, 1:char, 2:int >>> 45F77').upper()
               result = helpers.validateId(id=Id, clients=db.Clients.lst)
               if result:
                   break
           Name = helpers.readInput(3,30, 'Nombre= min:3, max:30 >>> Carlos').capitalize()
           Lastname = helpers.readInput(3,30, 'Apellido= min:3, max:30 >>> Rodriguez').capitalize()
           Email = helpers.readInput(3,120, 'Email >>> carlosrodriguez@gmail.com').lower()
           client = db.Clients.create(id=Id, name=Name, lastname=Lastname, email=Email)
           print('Cliente adicionado correctamente: {}\n'.format(client))
           sleep(3)
           helpers.cleanScreen()
           
       elif choice == '4':
           print('Modificando cliente')
           Id = helpers.readInput(5,5, 'Id= 2:int, 1:char, 2:int >>> 45F77').upper()
           client = db.Clients.findById(id=Id)
           if client is None:
               print('Cliente no encontrado')
           else:
               Name = helpers.readInput(5,30, f'Nombre= min:3, max:30 >>> [ID: {Id}]').capitalize()
               Lastname = helpers.readInput(5,30, f'Nombre= min:3, max:30 >>> [ID:{Id}]').capitalize()
               Email = helpers.readInput(5,30, f'Email >>> [ID: {Id}]').lower()
               result = db.Clients.update(id=client.id, name=Name, lastname=Lastname, email=Email)
               print('Cliente modificado correctamente: {}'.format(result))
       elif choice == '5':
           print('Eliminando cliente')
           Id = helpers.readInput(5,5, 'Id= 2:int, 1:char, 2:int >>> 45F77').upper()
           client = db.Clients.findById(id=Id)
           if client is None:
               print('Cliente no encontrado')
           else:
               client = db.Clients.delete(client.id)
               print('Cliente eliminado correctamente: {}'.format(client))
       elif choice == '6':
           print('Saliendo.... ')
           break
       else:
           helpers.cleanScreen()
           print('-------------------')
           print('opcion invalida ...')
           print('-------------------')
           
          
            
    
