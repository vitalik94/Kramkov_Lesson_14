#ДЗ на понедельник (Ivanov_Lesson_14.py):
# Простейший калькулятор c введёнными двумя числами вещественного типа.
# Ввод с клавиатуры: операции + - * / и два числа. Операции являются функциями.
# Обработать ошибку: “Деление на ноль”
# Ноль использовать в качестве завершения программы (сделать как отдельную операцию).
# Работу загружаем в репозиторий гита. Скидываем ссылку НА ФАЙЛ!

def sumNum(a, b):
    return a + b

def subNum(a, b):
    return a - b

def prodNum(a, b):
    return a * b

def divNum(a, b):
    return a / b

def is_not_zero(o):
    if o != '0':
        return True
    else:
        return False


while True:
    try:
        o = input('Введите операцию для работы с числами или 0 для завершения программы: ')
        if is_not_zero(o):
            a = float(input('Введите первое число: '))
            b = float(input('Введите второе число: '))

            if o == '+': print(sumNum(a, b))
            elif o == '-': print(subNum(a, b))
            elif o == '*': print(prodNum(a, b))
            elif o == '/':
                try:
                    print(divNum(a, b))
                except ZeroDivisionError:
                    print('Значение b равно 0, на 0 делить нельзя. Попробуйте еще раз!')
            else:
                print('Введенное значение не операция для работы с числами. Попробуйте еще раз!')
        else:
            break
    except ValueError:
        print('Введенное значение не число. Попробуйте еще раз!')