n = input('Введите ИНН: ')

def validation(INN):
    INN = int(INN)
    if len(str(INN)) == 10:


    elif len(str(INN)) == 12:


    else:
        return 'Введён некорректный ИНН.'