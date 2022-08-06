import locale
locale.setlocale(locale.LC_ALL, 'en_US.utf-8')
def get_employee_info():
    totalhours = float(input('Enter number of hours worked: '))
    hourlyrate = float(input('Enter hourly rate: '))
    incometaxrate = input('Enter income tax rate: ')
    return totalhours, hourlyrate, incometaxrate
def get_income_tax_and_net_pay(totalhours, incometaxrate, hourlyrate):
    grosspay = hourlyrate * totalhours
    incometax = float(grosspay) * (float(incometaxrate)/100)
    netpay = float(grosspay) - float(incometax)
    return incometax, netpay, grosspay, hourlyrate
def print_all_payroll(employeecount, totalhoursworked, totalgrosspay, totalincometax, totalnetpay):
    print(f'Total number of employees:  {employeecount}')
    print(f'Total hours worked:         {totalhoursworked}')
    print(f'Total gross pay:            {totalgrosspay}')
    print(f'Total income taxes:         {totalincometax}')
    print(f'Total net play:             {totalnetpay}')
def print_single_employee(name, totalhours, hourlyrate, grosspay, incometaxrate, incometax, netpay):
    print(f'Employee Name:          {name}')
    print(f'Hours Worked:           {totalhours}')
    print(f'Hourly Rate:            {hourlyrate}')
    print(f'Gross Pay:              {grosspay}')
    print(f'Income Tax Rate:        {incometaxrate}%')
    print(f'Income Tax:             {incometax}')
    print(f'Net Pay:                {netpay}')
employeecount = 0
totalhoursworked = 0.00
totalgrosspay = 0.00
totalincometax = 0.00
totalnetpay = 0.00
while True:
    name = input('Enter employee name: ')
    if name == 'End':
        print_all_payroll(employeecount, totalhoursworked, locale.currency(totalgrosspay), locale.currency(totalincometax), locale.currency(totalnetpay))
        break
    else:
        totalhours, hourlyrate, incometaxrate = get_employee_info()
        incometax, netpay, grosspay, hourlyrate = get_income_tax_and_net_pay(totalhours, incometaxrate, hourlyrate)
        employeecount += 1
        totalhoursworked += totalhours
        totalgrosspay += grosspay
        totalincometax += incometax
        totalnetpay += netpay
        print_single_employee(name, format(totalhours,'.2f'), locale.currency(hourlyrate), locale.currency(grosspay), incometaxrate, locale.currency(incometax), locale.currency(netpay))
