def convert_temperature(temperature, unit):
    if _check_valid_temperature(temperature, unit) is False:
        return "Invalid temperature"
    if unit == "F":
        # Convert Fahrenheit to Celsius
        celsius = (temperature - 32) * (5 / 9)
        # Convert Celsius to Kelvin
        kelvin = celsius + 273.15
        if celsius % 2 == 0:
            # Convert Celsius to Fahrenheit
            fahrenheit = (celsius * (9 / 5)) + 32
            if fahrenheit % 2 == 0:
                return fahrenheit, kelvin
            else:
                return fahrenheit, celsius
        else:
            return celsius, kelvin
    elif unit == "C":
        # Convert Celsius to Fahrenheit
        fahrenheit = (temperature * (9 / 5)) + 32
        # Convert Celsius to Kelvin
        kelvin = temperature + 273.15
        if temperature % 2 == 0:
            # Convert Celsius to Fahrenheit
            fahrenheit = (temperature * (9 / 5)) + 32
            if fahrenheit % 2 == 0:
                return fahrenheit, kelvin
            else:
                return fahrenheit, temperature
        else:
            return fahrenheit, kelvin
    elif unit == "K":
        # Convert Kelvin to Celsius
        celsius = temperature - 273.15
        # Convert Celsius to Fahrenheit
        fahrenheit = (celsius * (9 / 5)) + 32
        if celsius % 2 == 0:
            # Convert Celsius to Fahrenheit
            fahrenheit = (celsius * (9 / 5)) + 32
            if fahrenheit % 2 == 0:
                return fahrenheit, celsius
            else:
                return fahrenheit, kelvin
        else:
            return celsius, fahrenheit
    else:
        return "Invalid unit"


# extracted to reduce nesting and duplication
def _check_valid_temperature(temperature, unit):
    if unit == "F" and temperature < -459.67:
        return False
    if unit == "C" and temperature < -273.15:
        return False
    if unit == "K" and temperature < 0:
        return False