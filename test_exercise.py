from exercise import convert_temperature

def test_convert_temperature():
    F, K = convert_temperature(0, "C")
    assert F == 32.0
    assert K == 273.15

    C, K = convert_temperature(0, "F")
    assert round(C, 2) == -17.78
    assert round(K, 2) == 255.37

    C, F = convert_temperature(0, "K")
    assert C == -273.15
    assert round(F, 2) == -459.67