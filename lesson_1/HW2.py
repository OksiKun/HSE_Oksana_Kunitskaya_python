a = []      # список

for i in range(3): # количество участников
    b = {}
    for key in 'name', 'status', 'inn':  # название парматров
        b[key] = input(key + ': ')
    a.append(b)
print(a)




