def celsius_to_fahrenheit(celsius):
    return celsius/5*9.0 + 32.0

def celsius_to_kelvin(celsius):
    return celsius + 273.15

def fahrenheit_to_kelvin(fahrenheit):
    return (fahrenheit + 459.67) * 5/9.0

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def kelvin_to_fahrenheit(kelvin):
    return kelvin * 9/5.0 - 459.67

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32.0) * 5/9.0
