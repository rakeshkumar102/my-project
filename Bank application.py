class Bank_1:
    bank_name="sbi"
    bank_roi=7
    bank_adress="kizikistan"
    def _init_(self,c_name,c_account,c_balance,c_pin):
        self.name=c_name
        self.account=c_account
        self.balance=c_balance
        self.pin=c_pin
    @classmethod
    def bank_details(cls):
        print(f"custmer name is {cls.bank_name}")
        print(f"custmer roi no is {cls.bank_roi}")
        print(f"custmer balance is {cls.bank_adress}")
    @staticmethod
    def get_input():
        value=int(input("enter value "))
        return value
    def withdraw(self):
        amount=self.get_input()
        pin=self.get_input()
        if self.pin == pin and self.balance > amount:
            self.balance -=amount
            print(f"your new balance is {self.balance}")
        else:
            print("invalid pin or insufficient funds")
    def deposit(self):
        amount=self.get_input()
        self.balance +=amount
        print(f"your new balance is {self.balance}")
class Bank_v2(Bank_1):
    bank_branch= "banglore"
    bank_ifc= 214
    def customer_details(self):
        print(f"customer name is {self.name} account number is {self.account}"
        f"and his/her current balance is RS{self.balance}.")
    @classmethod
    def change_roi(cls):
        new_roi=cls.get_input()
        cls.bank_roi=new_roi
        print(f"ROI has been changed to {cls.bank_roi}%.")
raj=Bank_v2("raj",8222,1234,5645)
raj.bank_details()
raj.customer_details()
