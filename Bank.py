class BankAccount:

    no_of_cust = 0
    acc_num = 42010

    def __init__(self, name, mobile_no, initial_depo, pin):
        
        self.name                 = name
        self.cust_acc_num         = BankAccount.acc_num
        self.mobile_no            = mobile_no
        self.acc_balance          = initial_depo
        self.pin                  = pin
        
        BankAccount.acc_num       = BankAccount.acc_num + 1
        BankAccount.no_of_cust    = BankAccount.no_of_cust + 1

    def basic_details(self):
        print(f'User: {self.name}\t Account No: {self.cust_acc_num}\t Balance: ₹{self.acc_balance}')

    def deposit(self):
        amount = int(input('Enter the deposit amount: '))
        if amount > 0:
            self.acc_balance      = self.acc_balance + amount
            print(f'Transaction completed. Current Balance: ₹{self.acc_balance}')
        else:
            print('Invalid amount transaction aborted')

    def withdrawl(self):
        amount = int(input('Enter the withdrawl amount: '))
        if amount <= self.acc_balance and amount > 0:
            self.acc_balance      = self.acc_balance - amount
            print(f'Transaction completed. Current Balance: ₹{self.acc_balance}')
        else:
            print('Invalid amount transaction aborted')

    def payment(self, other):
        amount = int(input('Enter the payment amount: '))
        if amount <= self.acc_balance and amount > 0:
            self.acc_balance      = self.acc_balance - amount
            other.acc_balance     = other.acc_balance + amount
            print(f'Transaction completed. Current Balance: ₹{self.acc_balance}')
        else:
            print('Invalid amount transaction aborted')


if __name__ == '__main__':

    cust1 = BankAccount(name='Ishaan', mobile_no=9876543210, initial_depo=1000, pin=123)
    cust2 = BankAccount(name='Akash', mobile_no=9876543212, initial_depo=2000, pin=456)
    print('No. of customers is',BankAccount.no_of_cust)
    print(cust1.basic_details())
    print(cust2.basic_details())
    # cust1.deposit()
    # print(cust1.basic_details())
    # cust1.withdrawl()
    # print(cust1.basic_details())
    cust1.payment(cust2)
    print(cust2.basic_details())