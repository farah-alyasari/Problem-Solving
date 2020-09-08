#my solution - it turns out that they were some design points that are different in mine than theirs probably b/c the instructions were a little vague

class Account_Exception(Exception):
    pass

class Bank_Account:
    serial_number = 0

    def __init__(self):
        Bank_Account.serial_number += 1
        self.__account_number = Bank_Account.serial_number
        self.__account_balance = 0

    #get method for account_number
    @property
    def account_number(self):
        return self.__account_number

    #set method for account_number; not a possible user choice
    @account_number.setter
    def account_number(self):
        raise Account_Exception("Can't change the account number")

    #delete account_number
    @account_number.deleter
    def account_number(self):
        if self.__account_balance > 0:
            raise Account_Exception("Can't delete the account when it has a non zero balance, your account has: {} dollars".format(self.__account_balance))
        else:
            self.__account_number = None
            print("Done. Your account is deleted")

    #get the account_balance
    @property
    def account_balance(self):
        return self.__account_balance

    #set the account balance
    @account_balance.setter
    def account_balance(self, amount):
        if amount < 0:
            raise Account_Exception("Not possible to set a negataive value")
        elif abs(amount) > 100:
            self.__account_balance += amount
            print("Alert, amount is above 100.000")
        else:
            self.__account_balance += amount

    #delete the account balance
    #doesn't make sense to have this method

bank = Bank_Account()

try:
    bank.account_balance = 1000
except Exception as e:
    print(e)

try:
    bank.account_balance = -200
except Exception as e:
    print("2nd try: ",e)

try:
    bank.account_balance += 500
except Exception as e:
    print("3rd try: ", e)

try:
    bank.account_balance = 1000000
except Exception as e:
    print("4th try: ", e)

try:
    del bank.account_number
except Exception as e:
    print("5th try: ", e)

print("done")

# their solution
class AccountException(Exception):
    pass

class Account:
    def __init__(self, number):
        self.__balance = 0
        self.__number = number
        pass

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, value):
        if value < 0:
            raise AccountException('Can not set negative value')

        if abs(self.__balance - value) > 100_000:
            print('This operation will be audited')

        self.__balance = value

    @balance.deleter
    def balance(self):
        if self.__balance > 0:
            raise AccountException('Can not delete account as long it is not empty')
        self.__balance = None

    @property
    def number(self):
        return self.__number

    @number.setter
    def number(self, value):
        raise AccountException('Invalid operation')

    @number.deleter
    def number(self):
        raise AccountException('Invalid operation')

    def __str__(self):
        return 'Account #{} balance is {}'.format(self.__number, self.__balance)

account = Account('34-6514-7654-9999-0002')
account.balance += 1000
print(account)

try:
    account.balance = -200
except AccountException as e:
    print('Exception detected:', e)

try:
    account.number = 'a new one'
except AccountException as e:
    print('Exception detected:', e)

try:
    account.balance += 1_000_000
except AccountException as e:
    print('Exception detected:', e)

try:
    del account.balance
except AccountException as e:
    print('Exception detected:', e)
