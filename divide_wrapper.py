from divide import do_fraction_is_correct

while True:
    print('Write fractions in N1/N2 format, where N1 and N2 - integers, and N2 isn\'t zerof:')
    filepath = r'C:\Users\User\PycharmProjects\TEST\divide.py'
    try:
        do_fraction_is_correct(input())
    except ValueError:
        print('Wrong Number')
    except ZeroDivisionError:
        print('Division by zero')
    except (FileNotFoundError, FileExistsError):
        print('File not found')
        break
    except BaseException as error:
        print(error)
        break