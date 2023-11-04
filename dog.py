import random

class NumberEncoder:
    def __init__(self, number):
        self.number = number

    def __repr__(self):
        result = self.perform_operation()
        return str(result)

    def perform_operation(self):
        operation = random.choice(['+', '-', '*', '/'])
        if operation == '+':
            return self.number + random.randint(1, 10)
        elif operation == '-':
            return self.number - random.randint(1, 10)
        elif operation == '*':
            return self.number * random.randint(1, 10)
        elif operation == '/':
            return self.number / random.randint(1, 10)


encoded_number = NumberEncoder(10)
print(encoded_number)

