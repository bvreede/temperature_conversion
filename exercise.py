import conversion


def convert_temperature(temperature, unit):
    if _check_valid_temperature(temperature, unit) is False:
        return "Invalid temperature"
    if unit == "F":
        kelvin = conversion.fahrenheit_to_kelvin(temperature)
        celsius = conversion.fahrenheit_to_celsius(temperature)
        return celsius, kelvin
    elif unit == "C":
        kelvin = conversion.celsius_to_kelvin(temperature)
        fahrenheit = conversion.celsius_to_fahrenheit(temperature)
        return fahrenheit, kelvin
    elif unit == "K":
        celsius = conversion.kelvin_to_celsius(temperature)
        fahrenheit = conversion.kelvin_to_fahrenheit(temperature)
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
    return True