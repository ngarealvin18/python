class Mpesa:
    def __init__(self, account_balance, phone_number):
        self.account_balance = account_balance
        self.phone_number = phone_number
    def send_money(self, amount, receipient):
        if self.account_balance >= amount:
            self.account_balance -= amount
            print(f"{amount} KES sent to {receipient}")
        else:
            print("insufficient Amount to send MOney")
class PersonalMpesa(Mpesa):
    def __init__(self, account_balance, phone_number, id_no):
        super().__init__(account_balance, phone_number)
        self.id_no = id_no
    def buy_airtime(self, amount):
        self.account_balance-=amount
        print(f"{amount} KES airtime bought successfull")
class BusinessMpesa(Mpesa):
    def __init__(self, account_balance, phone_number, business_name):
        super().__init__(account_balance, phone_number)
        self.business_name =business_name
    def receive_payment(self, amount):
        self.account_balance += amount
        print(f"{amount} KES received from a customer")
personal=PersonalMpesa(20000, 722383427, 12345678)
personal.send_money(1500, 721863427)
personal.send_money(15000, 722383427)
