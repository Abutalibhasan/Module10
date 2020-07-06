class Employee:
 '''Employee Class '''
 # Constructor
 def __init__(self, lname, fname, addr, phone, salaried, st_date, sal):
         self.last_name = lname
         self.first_name = fname
         self.address = addr
         self.phone_number = phone
         self.salaried = salaried
         self.start_date = st_date
         self.salary = sal

 def set_last_name(self, lname):
        self.last_name = lname

 def set_first_name(self, fname):
         self.first_name = fname

 def set_address(self, addr):
         self.address = addr

 def set_phone_number(self, phone):
         self.phone_number = phone

 def set_salaried(self, salaried):
         self.salaried = salaried

 def start_date(self, st_date):
         self.start_date = st_date

 def set_salary(self, sal):
         self.salary = sal

 def display(self):
         print (self.last_name, self.first_name)
         print (self.address)
         print (self.salaried, self.salary)
         print (self.start_date)



class SalariedEmployee(Employee):
    def __init__(self,lname, fname, addr, phone, salaried, start_date,salary):
        Employee.__init__(self, lname, fname, addr, phone, salaried, start_date, salary)
        self.st_date = start_date
        self.sal = salary
    def give_raise(self, raises):
        self.sal = raises

    def display(self):
     return self.sal

class HourlyEmployee(Employee):

    def __init__(self,lname, fname, addr, phone, salaried, start_date, salary ,hourly_pay,):
        Employee.__init__(self, lname, fname, addr, phone, salaried, start_date)
        self.rate = hourly_pay
        self.stdate = start_date
        self.sal = salary
    def give_raise(self, r):
        self.rat = r
    def display(self):
     return self.rate


if __name__ == '__main__':
 emp = SalariedEmployee('A','B','1054 14th st','0907','yes','07/3/2020', '45,000')
 emp.give_raise('45,000')
print(emp.display())
emp1 = Employee('HASAN', 'abu', '1888 stname st', '090787', 'yes','1/1/19', '11000')
print(emp1.display())
r = HourlyEmployee('AMR', 'HAL', '1000 stname st','0188811', 'yes','07/05/202','20,000','11,00')
print(r.display())



