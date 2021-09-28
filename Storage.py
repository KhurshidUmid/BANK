import Account
import Transaction
import sqlite3

class Storage:

    def __init__(self, fileName) -> None:
        self.connection = sqlite3.connect(fileName)
        self.cursor = self.connection.cursor()
        
        try:
            self.__createCustomerTable()
            
        except OperationalError as e:
            print(f'Information: {e}')

    def insertCustomer(self, customer:Account):
        command = f"""
        INSERT INTO 
        customers(id, number, name) 
        values('{customer.id}', '{customer.number}', '{customer.name}')
        """
        return self.__executeCommand(command, True)

    
    
    def getAllCustomers(self):
        command = """
        SELECT * from customers;
        """
        return self.__executeCommand(command)

    
    def search(self, query):
        command = """
        """

    def __createCustomerTable(self):
        command = """
        CREATE TABLE customers(
            id char(64) str(uuid(4)),
            number char(25),
            name char(255),
            
        );
        """

        self.cursor.execute(command)

    

    def __executeCommand(self, command:str, commit:bool=False):
        try:
            self.cursor.execute(command)
            if commit:
                self.connection.commit()
            
            return { 'isSuccess': True, 'data': self.cursor.fetchall(), 'error': None }
        except Exception as e:
            return { 'isSuccess': False, 'data': None, 'error': e }