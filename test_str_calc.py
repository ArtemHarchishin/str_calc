import pytest

from str_calc import StringCalculator

def create_string_calculator():
    return StringCalculator()

def add_and_assert(numbers, output):
    calc = create_string_calculator()
    t_sum = calc.add(numbers)
    assert isinstance(t_sum, int)
    assert t_sum == output


class TestSimple(object):
    def test_create_string_calculator(self):
        create_string_calculator()

    def test_call_add_method(self):
        add_and_assert(None, 0)

    def test_call_add_with_empty_str(self):
        add_and_assert("", 0)

    def test_call_add_with_one_number_in_str(self):
        add_and_assert("1", 1)

        add_and_assert("15", 15)

    def test_call_add_with_two_numbers_in_str(self):
        add_and_assert("1,2", 3)
        add_and_assert("1 ,2", 3)
        add_and_assert("1, 2 ", 3)
        add_and_assert("10,2", 12)

    def test_call_add_with_many_numbers_in_str(self):
        add_and_assert("1,2,3,4,5,6", 21)

        add_and_assert("1,23,3,46,5,60", 138)


class TestDifferentDelimiter(object):
    def test_call_add_with_one_number_in_str(self):
        add_and_assert("1,\n", 1)

    def test_call_add_with_two_numbers_in_str(self):
        add_and_assert("1\n2,3", 6)

    def test_call_add_with_many_numbers_in_str(self):
        add_and_assert("1\n2,3\n4,5\n6", 21)


class TestCustomDelimiter(object):
    def test_call_add_with_one_number_in_str(self):
        add_and_assert(" //;\n1 ; ", 1)

    def test_call_add_with_two_numbers_in_str(self):
        add_and_assert("//;\n1;2", 3)

    def test_call_add_with_many_numbers_in_str(self):
        add_and_assert("//-\n1-2-3-4-5-6", 21)

class TestNegativeNumber(object):
    def test_call_add_with_one_number_in_str(self):
        with pytest.raises(Exception, match=r"\[-1\] negatives not allowed"):
            calc = create_string_calculator()
            calc.add("-1")

    def test_call_add_with_two_numbers_in_str(self):
        with pytest.raises(Exception, match=r"\[-2\] negatives not allowed"):
            calc = create_string_calculator()
            calc.add("1,-2")

    def test_call_add_with_many_numbers_in_str(self):
        with pytest.raises(Exception, match=r"\[-2, -5\] negatives not allowed"):
            calc = create_string_calculator()
            calc.add("1,-2,3,4,-5")