class Vehicle(object):

    def __init__(self, name, color):
        self.name = name
        self.color = color

    def who_am_i(self):
        print('I am a ' + self.color + ' ' + self.name + ' car ')



