import uuid
import Transaction

class Account:

    def __init__(self, id, number:int, name:str):
        self.id=str(uuid(4))
        self.number=number
        self.name=name


    def __str__(self):
        return f'{self.id}\n{self.number}\n{self.name}\n'