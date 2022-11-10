# create a function to check the number is even or odd?
def check_number(number = 0):
    if number % 2 == 0:
            return 'even'
    else:
        return 'odd'


print(check_number(4))