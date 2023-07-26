class employee:
    # init is a contructor, where you are using self keyword to
    # initialize a variable
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

    def full_name(self):
        return '{} {}'.format(self.first, self.last)


emp_1 = employee('Daksh', 'Sharma', 50000)
emp_2 = employee('test', 'user', 60000)

print(emp_1.email)
print(emp_1.full_name())
