import unittest
from roiproject import Investment

class TestInvestments(unittest.TestCase):

    def setUp(self):
        
        self.rent = 2000
        self.laundry = 0
        self.storage = 0
        self.misc = 0
        self.tax = 150
        self.insurance = 100
        self.utilities = 0
        self.vacancy = 100
        self.repairs = 100
        self.mortgage = 860
        self.property_manager = 200
        self.down_payment = 40000
        self.closing_cost = 3000
        self.rehab_budget = 7000
        self.expected_expenses = self.tax + self.insurance + self.utilities + self.vacancy + self.repairs + self.mortgage + self.property_manager
        self.expected_income = self.rent + self.laundry + self.storage + self.misc
        self.expected_cash_flow = (self.expected_income - self.expected_expenses)*12
        self.expected_investment = self.down_payment + self.closing_cost +self.rehab_budget
        self.roi = (self.expected_cash_flow / self.expected_investment)*100
        
    @classmethod  
    def setUpClass(self):
        self.calculator = Investment()

    def test_total_income(self):
        
        self.assertEqual(self.calculator.income(), self.expected_income)

    def test_total_expense(self):
        
        self.assertEqual(self.calculator.expenses(), self.expected_expenses)
    
    def test_cash_flow(self):
        
        self.assertEqual(self.calculator.annual_cashflow(), self.expected_cash_flow)

    def test_total_investment(self):
        
        self.assertEqual(self.calculator.total_investment(),self.expected_investment)
    
    def test_roi(self):

        self.assertEqual(self.calculator.return_on_investment(),self.roi)

unittest.main()
