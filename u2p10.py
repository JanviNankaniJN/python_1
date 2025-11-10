#Create a program name “employee.py” and implement the
#functions DA, HRA, PF, and ITAX. Create another program
#that uses the function of employee module and calculates gross
#and net salaries of an employee
import employee_u2p10
name=input("enter your name:")
basic=float(input("enter your salary:"))
da=employee_u2p10.DA(basic)
hra=employee_u2p10.HRA(basic)
pf=employee_u2p10.PF(basic)
gross=basic+da+hra
itax=employee_u2p10.ITAX(gross)
net=gross-(pf+itax)

print("Employee name:",name)
print("basic salary:",basic)
print("DA(10%):",da)
print("HRA(15%):",hra)
print("PF(12%):",pf)
print("ITAX(8%):",itax)
print("Gross salary:",gross)
print("Net salary:",net)