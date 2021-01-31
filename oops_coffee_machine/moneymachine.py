class Moneymachine():
    def __init__(self, denomination_map) -> None:
        self.denomination_map = denomination_map
        self.total_amt = 0
        self.cash_balance = 0

    def count_total_amt(self) -> int:
        self.total_amt = 0
        for key, val in self.denomination_map.items():
            self.total_amt += int(key)*int(val)
        return self.total_amt

    def return_change(self, product_amt = None) -> int:
        change = self.total_amt
        if product_amt:
            change = self.total_amt - product_amt
        return change

    def  update_cash_balance(self, income_amt) -> int:
        self.cash_balance += income_amt

    def check_money(self, coffee_cost):
        if self.total_amt < coffee_cost:
            return False
        else:
            return True
