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
