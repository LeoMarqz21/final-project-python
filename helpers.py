import os
import re
import platform

def cleanScreen():
    os.system('cls') if platform.system() == 'Windows' else os.system('clear')
        
def readInput(min:int = 0, max:int = 100, message:str = None):
    """
    Description:
        - This function reads input from the user and validates the input.

    Args:
        - min (int, optional): minimum number of characters - default is 0.
        - max (int, optional): maximum number of characters - default is 100.
        - message (str, optional): message to display to the user - default is None.
    """
    print(message) if message is not None else None
    while True:
        text = input('>>> ')
        if len(text) >= min and len(text) <= max:
            return text

def validateId(id:str, clients:list)->bool:
    """
    Description:
        - This function validates the id of the user.
    """
    if not re.match('[0-9]{2}[A-Z]{1}[0-9]{2}$', id):
        print('Invalid id')
        return False
    for client in clients:
        if client.id == id:
            print('This id is already in use')
            return False
    return True


    