import Account
import uuid
import datetime


class Transaction:

    def __init__(self, id, account_id, amount:float, date: datetime, note:str):
        self.id = str(uuid(4))
        self.account_id = account_id
        self.amount = amount
        self.note=note
        self.date = datetime.now()
        

    def __str__(self):
        return f'{self.id}\n{self.account_id}\n{self.amount}\n{self.date}\n{self.note}\n'