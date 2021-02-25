from Bank import BankAccount

customer_dict = {}
mobile_acc_link = {}

cust1 = BankAccount(name='Ishaan', mobile_no=9876543210, initial_depo=1000, pin=123)
customer_dict[cust1.cust_acc_num] = cust1
mobile_acc_link[cust1.mobile_no] = cust1.cust_acc_num
cust2 = BankAccount(name='Anirudh', mobile_no=9876543211, initial_depo=2000, pin=456)
customer_dict[cust2.cust_acc_num] = cust2
mobile_acc_link[cust2.mobile_no] = cust2.cust_acc_num
# print(cust1.cust_acc_num)
# customer_dict[42010].basic_details()

def new_cust():
    name = input('Enter the name of customer: ')
    mobile_no = int(input('Enter the mobile number of customer: '))
    initial_depo = int(input('Enter the initial deposit amount: '))
    if initial_depo <= 0:
        print('Invalid Amount')
        return
    pin = int(input('Create PIN: '))
    customer = BankAccount(name=name, mobile_no=mobile_no, initial_depo=initial_depo, pin=pin)
    customer_dict[customer.cust_acc_num] = customer
    mobile_acc_link[customer.mobile_no] = customer.cust_acc_num
    print('New User Created!')
    print(f'Welcome {customer.name} to Corporate Bank. {customer.cust_acc_num} is your account number')

def login():
    account_no = int(input('Enter your Account Number: '))
    account_pin = int(input('Enter your Account PIN: '))
    if account_no in customer_dict.keys() and account_pin == customer_dict[account_no].pin :
        print(f'\n{customer_dict[account_no].name} Logged in')
        customer_dict[account_no].basic_details()
    else:
        print('Account either not exist or the pin is wrong')
        return
    while True:
        user_input1 = input('''Press 1 for deposit:
Press 2 for withdrawl:
Press 3 for money transfer:
Press 4 to log out\n''')
        if user_input1 == '1':
            customer_dict[account_no].deposit()
        elif user_input1 == '2':
            customer_dict[account_no].withdrawl()
        elif user_input1 == '3':
            # print('Money Transfer')
            mobile = int(input('Enter the mobile number of recepient: '))
            if mobile in mobile_acc_link.keys():
                secondary = mobile_acc_link[mobile]
                customer_dict[account_no].payment(customer_dict[secondary])
            else:
                print('The mobile number you have enter does not have an account associated with it')
        elif user_input1 == '4':
            print('Logged Out')
            return
        else:
            print('Invalid input try again')
        print('\n#############################################################\n')
        customer_dict[account_no].basic_details()


while True:
    user_input1 = input('''Press 1 for creating a new customer:
Press 2 for logging in as an existing customer:
Press 3 for displaying number of customers:
Press 4 for exit\n''')

    if user_input1 == '1':
        print('Create user')
        new_cust()
    elif user_input1 == '2':
        # print('logging in')
        # for customer in customer_dict.values():
        #     customer.basic_details()
        login()
    elif user_input1 == '3':
        print('There currently', BankAccount.no_of_cust,'customers in Corporate bank.')
    elif user_input1 == '4':
        print('Exited')
        break
    else:
        print('Invalid input try again')
    print('\n*************************************************************\n')