try:
    year=int(input('year: '))
    age=2025-year
    print(age)
    age=2025/year

except ValueError:
    print('invalid')
except ZeroDivisionError:
    print('0')
