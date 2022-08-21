from datetime import datetime
def convert_from_p_del_to_list(data,entered_date):
    line_break_split = data.split('\n')
    line_break_split.pop()
    new_list = []
    for l in line_break_split:
        new_split = l.split('|')
        from_date = new_split[0]
        to_date = new_split[1]
        name = new_split[2]
        totalhours = new_split[3]
        hourlyrate = new_split[4]
        incometaxrate = new_split[5]
        new_dict = {
            "from_date"     :   from_date,
            "to_date"       :   to_date,
            "name"          :   name,
            "hoursworked"   :   float(totalhours),
            "hourlyrate"    :   float(hourlyrate),
            "incometaxrate" :   float(incometaxrate)
            }
        if entered_date == "all" or entered_date <= datetime.strptime(new_dict["from_date"], "%m/%d/%Y"):
            new_list.append(new_dict)
    return new_list
            
def get_search_date():
    file = open("payroll.txt", 'r')
    data = file.read()
    report_search_date = input('Search Date (mm/dd/yyyy) or All: ')
    if report_search_date.lower() == "all":
        data_to_read = convert_from_p_del_to_list(data, report_search_date)
        print_all_payroll(data_to_read)
    else:
        try:
            formatted_date = datetime.strptime(report_search_date, "%m/%d/%Y")
            data_to_read = convert_from_p_del_to_list(data, formatted_date)
            print_all_payroll(data_to_read)
            file.close()
        except ValueError:
            print('Invalid date format. Try again.\n')
def write_to_file(from_date, to_date, name, hoursworked, hourlyrate, incometaxrate):
    file = open('payroll.txt', 'a+')
    file.write(f'{from_date}|{to_date}|{name}|{hoursworked}|{hourlyrate}|{incometaxrate}|\n')
    file.close()
def get_total_hours():
    totalhours = float(input('Enter number of hours worked: '))
    return totalhours
def get_hourly_rate():
    hourlyrate = float(input('Enter hourly rate: '))
    return hourlyrate
def get_income_tax_rate():
    incometaxrate = float(input('Enter income tax rate: '))
    return incometaxrate
def get_dates():
    from_date = input('Enter From Date(mm/dd/yyyy): ')
    to_date = input('Enter To Date(mm/dd/yyyy): ')
    return from_date, to_date
def calc_gross_pay(hourlyrate, totalhours):
    grosspay = hourlyrate * totalhours
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
    if len(employee_list) != 0:
        employeecount = 0
        totalhoursworked = 0.00
        totalgrosspay = 0.00
        totalincometax = 0.00
        totalnetpay = 0.00
        for e in employee_list:
            from_date      =   e['from_date']
            to_date        =   e['to_date']
            name           =   e['name']
            totalhours     =   e['hoursworked']
            hourlyrate     =   e['hourlyrate']
            incometaxrate  =   e['incometaxrate']
            incometax, netpay, grosspay = get_income_tax_and_net_pay(totalhours, incometaxrate, hourlyrate)
            print(from_date, to_date, name, f'{totalhours:,.2f}', f'{hourlyrate:,.2f}', f'{grosspay:,.2f}', f'{incometaxrate:,.2f}%', f'{incometax:,.2f}', f'{netpay:,.2f}',)
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
        print(f'Total number of employees:  {employee_totals["number_of_employees"]}')
        print(f'Total hours worked:         {employee_totals["total_hours_worked"]:,.2f}')
        print(f'Total gross pay:            {employee_totals["total_gross_pay"]:,.2f}')
        print(f'Total income taxes:         {employee_totals["total_income_tax"]:,.2f}')
        print(f'Total net pay:              {employee_totals["total_net_pay"]:,.2f}')
    else:
        print('No data returned.')
employee_totals = {}

while True:
    name = input('Enter employee name: ')
    if name.upper() == 'END':
        while True:
            get_search_date()
            break
        break
    else:
        from_date, to_date = get_dates()
        hoursworked = get_total_hours()
        hourlyrate = get_hourly_rate()
        incometaxrate = get_income_tax_rate()
        write_to_file(from_date, to_date, name, hoursworked, hourlyrate, incometaxrate)