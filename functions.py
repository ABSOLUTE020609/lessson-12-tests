def hello_who(name):
    return f'Hello, {name}'

def salary(hours,salary_by_hour):
    '''
    Расчёт зп сотрудника
    :param hours: кол-во часов
    :param salary_by_hour: зарплата на час
    :return: итоговая сумма
    '''
    k= 2
    return hours * salary_by_hour*k