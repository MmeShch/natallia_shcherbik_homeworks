class Client:
    def __init__(self, name, id):
        self.name = name
        self.id = id

class BankAccount:
    def __init__(self, account_number, initial_balance, client):
        self.account_number = account_number
        self.balance = initial_balance
        self.client = client

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance > amount:
            self.balance -= amount
        else:
            raise ValueError("Insufficient funds in the account.")

class Bank:
    def __init__(self):
        self.accounts = {}

    def create_account(self, client, initial_balance):
        account_number = len(self.accounts) + 1
        new_account = BankAccount(account_number, initial_balance, client)
        self.accounts[account_number] = new_account
        return new_account

    def get_account(self, account_number):
        if account_number in self.accounts:
            return self.accounts[account_number]
        else:
            raise ValueError("Account does not exist")


    def transfer(self, sender_account, receiver_account, amount):
        sender = self.get_account(sender_account)
        receiver = self.get_account(receiver_account)
        if sender.balance < amount:
            raise ValueError("Insufficient funds")
        sender.withdraw(amount)
        receiver.deposit(amount)

    def get_total_balance(self, client):
        total_balance = 0
        for account in self.accounts.values():
            if account.client.id == client.id:
                total_balance += account.balance
        return total_balance


bank = Bank()
client1 = Client("Boldrin R.", 1)
client2 = Client("Heil.S", 2)
account1 = bank.create_account(client1, 1000)
account2 = bank.create_account(client2, 800)
account1.deposit(300)
account2.deposit(200)
print(bank.get_total_balance(client1))
print(bank.get_total_balance(client2))

