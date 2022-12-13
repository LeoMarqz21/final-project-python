import database as db
import unittest
import helpers
import copy

class TestDatabase(unittest.TestCase):
    
    def setUp(self) -> None:
        db.Clients.lst = [
            db.Client('15J77', 'Pedro', 'Hernandez', 'hernand78@gmail.com'),
            db.Client('25H11', 'Gloria', 'Sanchez', 'gloria@gmail.com'),
            db.Client('78F00', 'Francisco', 'Juarez', 'francisco@gmail.com')
        ]
        
    def test_findClientById(self):
        client = db.Clients.findById('15J77')
        clientNone = db.Clients.findById('19G23')
        self.assertIsNotNone(client)
        self.assertIsNone(clientNone)
    
    def test_createClient(self):
        db.Clients.create('74L09', 'Katy', 'Gomez', 'katy@gmail.com')
        db.Clients.create('20P20', 'Katy', 'Perry', 'katyp20@gmail.com')
        client = db.Clients.create('74L07', 'Lola', 'Venanvidez', 'lola12@gmail.com')
        self.assertEqual(len(db.Clients.lst), 6)
        self.assertEqual(client.id, '74L07')
        self.assertEqual(client.name, 'Lola')
        self.assertEqual(client.email, 'lola12@gmail.com')
    
    def test_updateClient(self):
        clientCopy = copy.copy(db.Clients.findById('25H11'))
        client = db.Clients.update('25H11', 'Gloria', 'Mendez', 'gloariamendez@gmail.com')
        self.assertEqual(clientCopy.name, client.name)
        print(client.lastname)

    def test_deleteClient(self):
        client = db.Clients.delete('25H11')
        clientIsNone = db.Clients.findById(client.id)
        self.assertEqual(len(db.Clients.lst), 2)
        self.assertIsNone(clientIsNone)
    
    def test_validateId_valid(self):
        self.assertTrue(helpers.validateId("00A21", db.Clients.lst))
    
    def test_validateId_invalid(self):
        self.assertFalse(helpers.validateId("15J77", db.Clients.lst))
        self.assertFalse(helpers.validateId("30BH4", db.Clients.lst))
    
    def tearDown(self) -> None:
        db.Clients.lst = []
    