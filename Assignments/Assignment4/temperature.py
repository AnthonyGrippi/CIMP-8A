'''
This module contains functions for converting
temperature between degrees Fahrenheit
and degreese Celsius
'''

def to_celcius(fahrenheit):
    '''
    This converts degrees to Fahrenheit to Celsius
    :param fahrenheit: This is the degrees Fahrenheit to convert
    :return: The converted Celsius value
    '''
    celcius = (fahrenheit - 32) *5/9
    return celcius





def to_fahrenheit(celsius):
    '''
    This converts degrees Celsius to Fahrenheit
    :param celsius: This is the degrees Celsius to convert
    :return: The converted Fahrenheit value
    '''
    fahrenheit = celsius * 9/5 + 32
    return fahrenheit



# the main() function is used to test the conversion function
# this code isn't run if this isn't the main module
def main():
    for temp in range(0, 212, 40):
        print(temp, "Fahrenheit =", round(to_celcius(temp)), "Celsius")

    for temp in range(0, 100, 20):
        print(temp, "Celsius =", round(to_fahrenheit(temp)), "Fahrenheit")


# if this module is the main module, call the main()
# function tp test the conversion function
if __name__ == "__main__":
    main()