"""
Необходимо использовать функции. Программа должна поддерживать следующие арифметические операции:
+, -, /, *, %(получение процента от числа), **(возведение в квадрат), **х(возведение в степень числа х).
Запрещено подключать дополнительные модули. Для вывода результата необходимо использовать функцию print().
"""
argums = input()

def ops(*args):
    try:
        result = eval(args[0])
    except SyntaxError:
        result = "Всё же самому нужно подумать"
    return result

print(ops(argums))
