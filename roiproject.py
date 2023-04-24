class Investment:
    def __init__(self):
        self.rent = int(input('please enter the amount you charge for rent: '))
        self.laundry = int(input('please enter the amount you charge for laundry: '))
        self.storage = int(input('please enter the amount you charge for storage: '))
        self.misc = int(input('please enter the amount you charge for misc: '))
        self.tax = int(input('Please enter how much you spend on Tax: '))
        self.insurance = int(input('Please enter how much you will spend on Insurasnce: '))
        self.utilities = int(input('Please enter how much you will spend on Utilities: '))
        self.vacancy = int(input('Please enter how much you will save for vacancy: '))
        self.repairs = int(input('Please enter how much you will save for repairs: '))
        self.mortgage = int(input('Please enter how much you will spend on your mortgage: '))
        self.property_manager = int(input('Please enter how much you wiil spend on a property manager: '))
        self.down_payment = int(input('Please enter how much you will spend on the down payment: '))
        self.closing_cost = int(input('Please enter how much you will spend on the closing cost: '))
        self.rehab_budget = int(input('Please enter how much you will spend on the rehab budget: '))
      
    def income(self):
        self.total_income = self.rent + self.laundry + self.storage + self.misc
        
        return self.total_income


    def expenses(self):
        self.total_expenses = self.tax + self.insurance + self.utilities + self.repairs + self.property_manager + self.mortgage + self.vacancy

        return self.total_expenses
    
    def annual_cashflow(self):
        self.monthly_cashflow = self.income() - self.expenses()
        self.yearly_cashflow = self.monthly_cashflow*12

        return self.yearly_cashflow
    def total_investment(self):

        self.sum_investment = self.down_payment + self.closing_cost +self.rehab_budget

        return self.sum_investment
    
    def return_on_investment(self):
        self.roi = (self.annual_cashflow() / self.total_investment())*100

        return self.roi
    
    def driver(self):
        self.income()
        self.expenses()
        self.annual_cashflow()
        self.total_investment()
        self.return_on_investment()
        print(f'your total income is: {self.total_income}')
        print(f'your total expenses are: {self.total_expenses}')
        print(f'your monthly cashflow will be your total income: {self.total_income} - total expenses: {self.total_expenses} to get {self.monthly_cashflow}')
        print(f'then take monthly cashflow: {self.monthly_cashflow} and multiply it by 12 to get your yearly cashflow of: {self.yearly_cashflow}')
        print(f'then we will take the down payment: {self.down_payment} and add that to closing cost: {self.closing_cost} and then add your rehab budget: {self.rehab_budget} to get your total investment of: {self.total_investment()}')
        print(f'finally we want to take the annual cashflow of: {self.annual_cashflow()} and divide it by your total investment:{self.total_investment()} to get the return on investment which is: {self.roi} percent!')
    
    
