class Employee(object):
    
    def __init__(self, id, name, salary):
        self.id = id
        self.name = name
        self.salary = salary



class FullTimeEmployee(Employee):

    def __init__(self, id, name, salary, benefits):
        Employee.__init__(self, id, name, salary)
        self.benefits = benefits

    def display(self):
        print(self.id, self.name, self.salary, self.benefits)


if (__name__ == '__main__'):
    fte = FullTimeEmployee(100, 'Magesh', 10000, 'Good Food')
    fte.display()