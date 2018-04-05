import operator
import functools
import re

class Negativenumber_Exception(Exception):
    pass

def Multiply(numbers, delimiter):


    flag = 0
    negative_number = []

    numbers_list = [int(number) for number in numbers_string.split(delimiter) ]

    numbers_list.sort()


    for number in numbers_list:
        if number > 100:
            return 0

    for number in numbers_list:
        if number < 0:
            negative_number.append(number)
            flag = 1

    if flag==1:
        raise Negativenumber_Exception("Negatives not allowed: "+ ', '.join(str(x) for x in negative_number))

    return (functools.reduce(operator.mul, numbers_list, 1))




if __name__ == '__main__':
    numbers_string = input("enter the numbers string" + "\n")

    first_time = 1
    for literal in numbers_string:

        if literal.isalpha():
            print("Invalid String" + "\n")
            exit()
        if not bool(re.search(r'\d', literal)):
            if literal is not "-":
                if first_time ==  1:
                    first_delimiter = literal
                    first_time = 0
                delimiter = literal

            if delimiter == first_delimiter:
                continue
            else:
                print("Invalid String with multiple deimiters" + "\n")
                exit()



    print("Resut: ")
    print (Multiply(numbers_string, delimiter))