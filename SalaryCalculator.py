class SalaryCalculator(object):

    def __init__(self):
        self.basic = 0
        self.hra = 0
        self.da = 0
        self.tax = 0
        self.salary = 0

    def calculate(self):
        _gross = self.basic + self.hra + self.da
        _net = _gross * ((100 - self.tax) / 100.0)
        self.salary = _net

    def display(self):
        print(self.basic)
        print(self.hra)
        print(self.da)
        print(self.tax)
        print(self.salary)


if (__name__ == '__main__'):
    calc = SalaryCalculator()
    calc.basic = 10000
    calc.hra = 2000
    calc.da = 3000
    calc.tax = 10
    calc.calculate()
    calc.display()
