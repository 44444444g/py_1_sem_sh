# обработка исключений
while True:
    try:
        number = int(input("введите трёхзначное число"))  # ввод данных
    except ValueError:
        print("что-то пошло не так")
        continue
    break
# получение цифр сотен, десятков и единиц
hundreds = number // 100
tens = (number // 10) % 10
units = number % 10

# перестановка цифр сотен и десятков
new_number = hundreds + tens * 100 + units * 10

# вывод результата
print("Число после перестановки цифр сотен и десятков:", new_number)
