import pytest

from src.utils import convert_string_to_list, validate_list


@pytest.fixture
def input_list():
    string = "1 _ 2 4 5 7 3 8 9 6 11 12 13 10 14 15"
    return convert_string_to_list(string)


def test_conversion(input_list):
    assert type(input_list) is list

    assert convert_string_to_list("   3 4   ") == ["3", "4"]


def test_validate_list(input_list):
    assert validate_list(input_list) is True

    with pytest.raises(Exception) as e:
        validate_list(["1", "2", "3"])

    wrong_num_list = list(input_list)
    wrong_num_list[15] = "17"
    with pytest.raises(Exception) as e:
        validate_list(wrong_num_list)

    no_blank_list = list(input_list)
    no_blank_list[1] = "18"
    with pytest.raises(Exception) as e:
        validate_list(no_blank_list)
