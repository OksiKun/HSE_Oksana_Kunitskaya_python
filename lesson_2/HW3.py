# 1
# 1.1

def fact(x):
    n = 1
    for i in range(1, x+1):
        n = n * i
    return n

print(fact(5))
print(fact(6))
print(fact(int(input())))

# 1.2

def maximum(x):
    if x[0]>x[1] and x[0]>x[2]:
        m = x[0]
    elif x[1]>x[0] and x[1]>x[2]:
        m = x[1]
    else:
        m = x[2]
    return m
k = (11,7,3)
print(maximum(k))
a = (-12, -15, -72)
print(maximum(a))

# 1.3

# равнобедренный = прямоугольный треугольник в данном коде

a = int(input())
b = int(input())

s = int(a*b/2)

print(s)

# 2

def number_of_case(x):
    import lesson_2_data
    r = lesson_2_data.repondents
    courts = lesson_2_data.courts
    c = len(r)                                  # функция len() возвращает количество сиволов в строке или количество элементов в списке
    court_code = x[0:3]                         # если есть строка x = 'А51-15785/2017', то можно взять срез x[0:3] = 'А51'
    for i in range(c):
        if 'case_number' in r[i]:                  # проверка наличия ключа (номера дела) в словаре (базе)
            if r[i]['case_number'] == x:
                full_name = r[i]["full_name"]
                short_name = r[i]["short_name"]
                inn = r[i]["inn"]
                ogrn = r[i]["ogrn"]
                region = r[i]["region"]
                category = r[i]["category"]
                category_code = r[i]["category_code"]
                bankruptcy_id = r[i]["bankruptcy_id"]
                case_number = r[i]["case_number"]
                address = r[i]["address"]
    for j in range(len(courts)):
        if courts[j]["court_code"] == court_code:
            court_name = courts[j]["court_name"]
            court_address = courts[j]["court_address"]
            court_time_shift = courts[j]["court_time_shift"]
            court_phone_info = courts[j]["court_phone_info"]
            court_fax_info = courts[j]["court_fax_info"]
            court_email = courts[j]["court_email"]
            court_website = courts[j]["court_website"]
            court_head = courts[j]["court_head"]
    if "Арбитражного" in court_name:
        court_name = court_name.replace('Арбитражного', 'арбитражный')
    if "суда" in court_name:
        court_name = court_name.replace('суда', 'суд')
    text = f"""В {court_name}
Адрес: {court_address}

Истец: Пупкин Василий Геннадьевич
ИНН 1236182357 ОГРНИП 218431927812733
Адрес: 123534, г. Москва, ул. Опущенных водников, 13

Ответчик: {short_name}
ИНН {inn} ОГРН {ogrn}
Адрес: {address}

Номер дела {case_number}"""
    return text

print(number_of_case(input()))




