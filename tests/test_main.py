import pytest
import sys
from unittest.mock import patch
from  main import CountryData
from main import *

def test_init_success():
    gdp_values = [5, 4, 3]
    country_data =  CountryData("Test", gdp_values)
    assert country_data.country == "Test"
    assert country_data.gdp_values == gdp_values 

def test_init_fail():
    gdp_values = [5, 4, '3']
    with pytest.raises(ValueError):
        CountryData("Test", gdp_values=gdp_values)

def test_add_gdp_value_success():
    gdp_values = [5,4, 3]
    expected = [5, 4, 3, 3]

    country_data = CountryData("Test", gdp_values)
    country_data.addGdpValue(3)
    assert country_data.gdp_values == expected

def test_add_gdp_value_fail():
    gdp_values = [5, 4, 3]
    country_data = CountryData("Test", gdp_values)
    with pytest.raises(ValueError):
        country_data.addGdpValue('3')


def test_calculate_average_success():
    gdp_values = [5, 4, 3]
    expected = 4

    country_data = CountryData("Test", gdp_values)
    assert country_data.calculate_average() == expected

def test_calculate_average_empty_list():
    expected = 0
    country_data= CountryData("Test")
    assert country_data.calculate_average() == expected

def test_get_countries_data_success():
    expected_countries_data_len = 2

    rows = [
        ['USA', '2023','25462','2.1','3.4','3.7','339','North America'],
        ['China','2023','17963','5.2','2.5','5.2','1425','Asia']
    ]

    country_data = get_countries_data(rows)
    assert len(country_data) == expected_countries_data_len
    assert 'USA' in country_data
    assert 'China' in country_data

def test_get_countries_data_similar_name():
    expected_len = 2
    rows = [
        ['USA', '2023','25462','2.1','3.4','3.7','339','North America'],
        ['USA', '2024','25463','2.1','3.4','3.7','339','North America'],
        ['China','2023','17963','5.2','2.5','5.2','1425','Asia']
    ]

    country_data = get_countries_data(rows)
    assert len(country_data) == expected_len
    assert len(country_data['USA'].gdp_values) == expected_len


def test_get_rows_success():
    files = ['./files/economic1.csv', './files/economic2.csv']
    rows = get_rows(files)

    assert len(rows)>0

def test_get_rows_fail_file_not_found():
    files = ['economics.csv']

    with pytest.raises(FileNotFoundError):
        rows = get_rows(files)

def test_parse_args_success():
    testargs = ['main.py', '--files', './files/economic1.csv', './files/economic2.csv', '--report', 'average-gdp']
    expected_len = 2
    expected_report = 'average-gdp'
    with patch.object(sys, 'argv', testargs):
        parsed_args = parse_args()
        assert len(parsed_args.files) == expected_len
        assert parsed_args.report == expected_report

def test_parse_args_fail_argument_error():
    try:

        testargs = ['main.py', '--files', './files/economic1.csv', './files/economic2.csv', '--report']
        with patch.object(sys,'argv', testargs):
            parsed_args = parse_args()
    except SystemExit as e:
            assert isinstance(e.__context__, argparse.ArgumentError)
        
def test_write_to_csv_success():
    rows = {'USA': CountryData("USA",  [5, 4, 3]),
            'China':  CountryData("China",  [5, 4, 3]) }
    filename = 'average_gdp'
    expected_count = sum(1 for line in rows)+1

    write_to_csv(filename, rows)
    with open(f'{filename}.csv') as f:
        file_line_count = sum(1 for line in f)
        assert file_line_count == expected_count
