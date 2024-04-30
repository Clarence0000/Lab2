import Lab2

def test_find_min_max():
    input_value = [43,26,79,65,33,55]
    test_value = [26.0, 79.0]

    result = Lab2.calc_min_max_temperature(input_value)

    assert (result == test_value)

def test_calc_average():
    input_value = [43,26,79,65,33,55]
    test_value = 50.166666666666664

    result = Lab2.calc_average_temperature(input_value)

    assert (result == test_value)

def test_calc_median_temperature():
    input_value = [43,26,79,65,33,55]
    test_value = 49

    result = Lab2.calc_median_temperature(input_value)

    print(result)

    assert result == test_value