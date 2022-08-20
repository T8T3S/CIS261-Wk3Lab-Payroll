def get_total_hours():
    totalhours = float(input('Enter number of hours worked: '))
    return totalhours
def get_hourly_rate():
    hourlyrate = float(input('Enter hourly rate: '))
    return hourlyrate
def get_income_tax_rate():
    incometaxrate = input('Enter income tax rate: ')
    return float(incometaxrate)
def get_dates():
    from_date = input('Enter From Date(mm/dd/yyyy): ')
    to_date = input('Enter To Date(mm/dd/yyyy): ')
    return from_date, to_date
def calc_gross_pay(hourlyrate, totalhours):
    grosspay = float(hourlyrate) * float(totalhours)
    return float(grosspay)

def calc_income_tax(grosspay,incometaxrate):
    incometax = grosspay * incometaxrate
    return incometax

def calc_net_pay(grosspay, incometax):

    netpay = grosspay - incometax
    return netpay
def get_income_tax_and_net_pay(totalhours, incometaxrate, hourlyrate):
    grosspay = calc_gross_pay(hourlyrate, totalhours)
    incometax = calc_income_tax(grosspay, incometaxrate)
    netpay = calc_net_pay(grosspay, incometax)
    return incometax, netpay, grosspay
def print_all_payroll(employee_list):
    employeecount = 0
    totalhoursworked = 0.00
    totalgrosspay = 0.00
    totalincometax = 0.00
    totalnetpay = 0.00
    for e in employee_list:
        from_date = e[0]
        to_date = e[1]
        name = e[2]
        totalhours = e[3]
        hourlyrate = e[4]
        incometaxrate = e[5]
        incometax, netpay, grosspay = get_income_tax_and_net_pay(totalhours, incometaxrate, hourlyrate)
        print(from_date, to_date, name, f'{totalhours:,.2f}', f'{hourlyrate:,.2f}', f'{grosspay:,.2f}', f'{incometaxrate:,.1%}', f'{incometax:,.2f}', f'{netpay:,.2f}',)
        employeecount += 1
        totalhoursworked += totalhours
        totalgrosspay += grosspay
        totalincometax += incometax
        totalnetpay += netpay
        employee_totals['number_of_employees'] = employeecount
        employee_totals['total_hours_worked'] = totalhoursworked
        employee_totals['total_gross_pay'] = totalgrosspay
        employee_totals['total_income_tax'] = totalincometax
        employee_totals['total_net_pay'] = totalnetpay

def print_payroll_totals(employee_totals):
     print(f'Total number of employees: {employee_totals["number_of_employees"]}')
     print(f'Total hours worked:        {employee_totals["total_hours_worked"]:,.2f}')
     print(f'Total gross pay:           {employee_totals["total_gross_pay"]:,.2f}')
     print(f'Total income taxes:        {employee_totals["total_income_tax"]:,.2f}')
     print(f'Total net play:            {employee_totals["total_net_pay"]:,.2f}')

employee_list = []
employee_totals = {}
while True:
    name = input('Enter employee name: ')
    if name.upper() == 'END':
        break
    else:
        from_date, to_date = get_dates()
        totalhours = get_total_hours()
        hourlyrate = get_hourly_rate()
        incometaxrate = get_income_tax_rate()
        single_employee_list = [from_date, to_date, name, totalhours, hourlyrate,incometaxrate]
        employee_list.append(single_employee_list)
print_all_payroll(employee_list)
print_payroll_totals(employee_totals)
