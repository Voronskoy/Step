import functools

def error_logger (func): 
    @functools.wraps (func)
    def wrapper(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
            return result
        except Exception as e:
            print (f"Error: (e)")
    return wrapper

@error_logger
def calculator (a, b, operation):
    if operation == '+':
        return a + b
    elif operation == '-':
        return a - b
    elif operation == '*':
        return a * b
    elif operation == '/':
        if b == 0:
            raise ValueError("Делить на ноль нельзя!")
        return a/b
    else:
         raise ValueError("Hеверная операция!")
try:
    result = calculator (11, 4, '+') 
    print("Peзультат сложения:", result)

    result2 = calculator(9, 1, '/') 
    print("Результат деления:", result2)

    result3 = calculator (4, 7, '$')
    print("Результат операции:", result3)
except Exception as e:
   print("Ошибка при выполнении операции:", e)