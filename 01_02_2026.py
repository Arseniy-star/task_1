#!/usr/bin/python3

#Program 1
#Funcion
def filter_numbers(numbers, threshold=0, greater=True):
    result = []

    for number in numbers:
        if greater:
            if number > threshold:
                result.append(number)
        else:
            if number < threshold:
                result.append(number)

    return result

#Program
x = filter_numbers([1, -5, 10, 0, 3])
print(x)


# Program 2
# Funcion
def rectangle_area(a, b=None):
    if b is None:
        return a*a
    else:
        return a*b


#Program
z = rectangle_area(2, 3)
print(z)
