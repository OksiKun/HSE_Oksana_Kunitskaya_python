n = input('Введите ИНН: ')

def sum_of_10INN(x):
    s = 0
    INN = str(x)
    c = 0
    for i in [2,4,10,3,5,9,4,6,8]:
        s = s + i*int(INN[c])
        c = c + 1
    return s

def sum_of_12INN10(x):
    s = 0
    INN = str(x)
    c = 0
    for i in [7,2,4,10,3,5,9,4,6,8]:
        s = s + i*int(INN[c])
        c = c + 1
    return s

def sum_of_12INN11(x):
    s = 0
    INN = str(x)
    c = 0
    for i in [3,7,2,4,10,3,5,9,4,6,8]:
        s = s + i*int(INN[c])
        c = c + 1
    return s

def validation_INN(INN):
    INN = int(INN)
    if len(str(INN)) == 10:
        if sum_of_10INN(INN)%11==INN%10:
            return True
        else:
           return  False
    elif len(str(INN)) == 12:
        if (sum_of_12INN10(INN)%11)==((INN%100)//10) and (sum_of_12INN11(INN)%11)==(INN%10):
            return True
        else:
            return False
    else:
        return validation_INN(input('Введён некорректный ИНН. Введите ИНН: '))

print(validation_INN(n))