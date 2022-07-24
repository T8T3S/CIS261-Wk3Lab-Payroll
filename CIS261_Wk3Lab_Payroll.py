import locale
locale.setlocale(locale.LC_ALL, 'en_US.utf-8')
def GetEmpInfo():
    totalhours = float(input('Total Hours: '))
    hourlyrate = float(input('Hourly Rate: '))
    incometaxrate = input('Income Tax Rate: ')
    return totalhours, hourlyrate, incometaxrate
def GetIncTaxNetPay(totalhours, incometaxrate, hourlyrate):
    grosspay = hourlyrate * totalhours
    incometax = float(grosspay) * (float(incometaxrate)/100)
    netpay = float(grosspay) - float(incometax)
    return incometax, netpay, grosspay, hourlyrate
def PrintEnd(employeecount, totalhoursworked, totalgrosspay, totalincometax, totalnetpay):
    print(f'Total number of employees:  {employeecount}')
    print(f'Total hours worked:         {totalhoursworked}')
    print(f'Total gross pay:            {totalgrosspay}')
    print(f'Total income taxes:         {totalincometax}')
    print(f'Total net play:             {totalnetpay}')
def PrintEmployee(name, totalhours, hourlyrate, grosspay, incometaxrate, incometax, netpay):
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
    name = input('Employee Name: ')
    if name == 'End':
        PrintEnd(employeecount, totalhoursworked, locale.currency(totalgrosspay), locale.currency(totalincometax), locale.currency(totalnetpay))
        break
    else:
        totalhours, hourlyrate, incometaxrate = GetEmpInfo()
        incometax, netpay, grosspay, hourlyrate = GetIncTaxNetPay(totalhours, incometaxrate, hourlyrate)
        employeecount += 1
        totalhoursworked += totalhours
        totalgrosspay += grosspay
        totalincometax += incometax
        totalnetpay += netpay
        PrintEmployee(name, format(totalhours,'.2f'), locale.currency(hourlyrate), locale.currency(grosspay), incometaxrate, locale.currency(incometax), locale.currency(netpay))
