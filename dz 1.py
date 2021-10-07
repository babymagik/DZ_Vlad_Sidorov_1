
#Задание номер 1
duration = int(input())
m = duration // 60
h = duration // 3600
d = duration // 86400
if duration < 60:
    print(duration, 'сек')
elif 3600 > duration >= 60:
    s = duration % 60
    print(m, 'мин', s, 'сек')
elif 86400 > duration >= 3600:
    s = duration % 60
    m = m % 60
    print(h, 'час', m, 'мин', s, 'сек')
else:
    s = duration % 60
    m = m % 60
    h = duration % 86400 // 3600
    print(d, 'дни', h, 'час', m, 'мин', s, 'сек')



#Задание номер 3
list_a = list(range(21, 92, 10)) + [1]
list_b = list(range(2, 5,))
list_c = list(range(11, 15))
n = 1
end = n % 10
while n <= 100:
    if n in list_c:
        print(n, 'процентов')
        n = n + 1
        end = n % 10
    elif end in list_b:
        print(n, 'процента')
        n = n + 1
        end = n % 10
    elif end in list_a:
        print(n, 'процент')
        n = n + 1
        end = n % 10
    else:
        print(n, 'процентов')
        n = n + 1
        end = n % 10
