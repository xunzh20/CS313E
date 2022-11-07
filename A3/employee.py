#  File: employee.py
#  Description: There program is a set of classes that simulates an employee record system. 
#  Student Name: Xun Zhou
#  Student UT EID: xz7637
#  Partner Name: Siqi Xie
#  Partner UT EID: sx2564
#  Course Name: CS 313E
#  Unique Number: 52520
#  Date Created: 9/18/2022
#  Date Last Modified: 9/19/2022

import sys


class Employee:

    def __init__(self, **kwargs):
        self.name = kwargs.get("name", None)
        self.id = kwargs.get("id", None)
        self.salary = kwargs.get("salary", None)

    def __str__(self):
        print("Employee\n"+self.name,",",self.id,",",self.salary,end ="")
        return "" 

############################################################
############################################################
############################################################

class Permanent_Employee(Employee) :

    def __init__(self, **kwargs):
        super().__init__(name = kwargs.get("name",None), id = kwargs.get("id", None), salary = kwargs.get("salary", None))
        self.benefits = kwargs.get("benefits",[])

    def cal_salary(self):
        if ("retirement" in self.benefits) and ("health_insurance" in self.benefits):
            return float(self.salary*0.7)
        elif "retirement" in self.benefits:
            return float(self.salary*0.8)
        elif "health_insurance" in self.benefits:
            return float(self.salary*0.9)


    def __str__(self):
        print("Permanet_Employee\n",self.name,",",self.id,",",self.salary,",",end="")
        print(self.benefits,end="")
        return ""
############################################################
############################################################
############################################################

class Manager(Employee) :
    def __init__(self,**kwargs):
        super().__init__(name = kwargs.get("name",None), id = kwargs.get("id", None), salary = kwargs.get("salary", None))
        self.bonus = kwargs.get("bonus",0)

    def cal_salary(self):
        return float(self.salary + self.bonus)
    def __str__(self):
        print("Manager\n",self.name+",",self.id,",",self.salary,",",self.bonus,end="")
        return ""


############################################################
############################################################
############################################################
class Temporary_Employee(Employee) :
    def __init__(self, **kwargs):
        super().__init__(name = kwargs.get("name",None), id = kwargs.get("id", None), salary = kwargs.get("salary", 0))
        self.hours = kwargs.get("hours",0)
        
    def cal_salary(self):
        return float(self.hours*self.salary)

    def __str__(self):
        print("Temporary_Employee\n",self.name,",",self.id,",",self.salary,", ",self.hours,end="")
        return ""

############################################################
############################################################
############################################################


class Consultant (Temporary_Employee):
    def __init__(self, **kwargs):
        super().__init__(name = kwargs.get("name",None), id = kwargs.get("id", None), salary = kwargs.get("salary", 0), hours = kwargs.get("hours",0))
        self.travel = kwargs.get("travel",0)
    def cal_salary(self):
        return float(self.hours*self.salary + self.travel*1000)

    def __str__(self):
        print("Consultant\n",self.name,",",self.id,",",self.salary,",",self.hours,",",self.travel,end="")
        return ""
############################################################
############################################################
############################################################


class Consultant_Manager(Manager,Consultant) :
    def __init__(self,  **kwargs):
        Manager.__init__(self,name = kwargs.get("name",None), id = kwargs.get("id", None), salary = kwargs.get("salary", None), bonus = kwargs.get("bonus",0))
        Consultant.__init__(self,name = kwargs.get("name",None), id = kwargs.get("id", None), salary = kwargs.get("salary", None),hours = kwargs.get("hours",0),travel = kwargs.get("travel",0))
       
        # super().__init__(name = kwargs.get("name",None), id = kwargs.get("id", None), salary = kwargs.get("salary", 0),bonus = kwargs.get("bonus",0), hours = kwargs.get("hours",0),travel = kwargs.get("travel",0))
    
    def cal_salary(self):
        return float(self.salary*self.hours + self.travel*1000 + self.bonus)
    def __str__(self):
        print("Consultant_Manager\n",self.name,",",self.id,",",self.salary,",",self.hours,",",self.travel,end=" Consultant_Manager")
        print("Manager\n",self.name+",",self.id,",",self.salary,",",self.bonus,end="")
        return ""

############################################################
############################################################
############################################################



###### DO NOT CHANGE THE MAIN FUNCTION ########

def main():

    chris = Employee(name="Chris", id="UT1")
    print(chris, "\n")

    emma = Permanent_Employee(name="Emma", id="UT2", salary=100000, benefits=["health_insurance"])
    print(emma, "\n")

    sam = Temporary_Employee(name="Sam", id="UT3", salary=100,  hours=40)
    print(sam, "\n")

    john = Consultant(name="John", id="UT4", salary=100, hours=40, travel=10)
    print(john, "\n")

    charlotte = Manager(name="Charlotte", id="UT5", salary=1000000, bonus=100000)
    print(charlotte, "\n")

    matt = Consultant_Manager(name="Matt", id="UT6", salary=1000, hours=40, travel=4, bonus=10000)
    print(matt, "\n")

    ###################################
    print("Check Salaries")

    print("Emma's Salary is:", emma.cal_salary(), "\n")
    emma.benefits = ["health_insurance"]

    print("Emma's Salary is:", emma.cal_salary(), "\n")
    emma.benefits = ["retirement", "health_insurance"]

    print("Emma's Salary is:", emma.cal_salary(), "\n")

    print("Sam's Salary is:", sam.cal_salary(), "\n")

    print("John's Salary is:", john.cal_salary(), "\n")

    print("Charlotte's Salary is:", charlotte.cal_salary(), "\n")

    print("Matt's Salary is:",  matt.cal_salary(), "\n")


if __name__ == "__main__":
  main()
