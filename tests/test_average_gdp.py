import pytest
import sys
import argparse
from unittest.mock import patch
from app.reports.average_gdp import AverageGDPReport
from app.registry import get_report
from  app.loader import get_rows
from app.parser import parse_args
from main import *



def test_calculate_average_success():
    rows = [
        {'country': 'USA', 'gdp': '100'},
        {'country': 'USA', 'gdp': '300'}, 
        {'country': 'Germany', 'gdp': '200'}, 
        {'country': 'Germany', 'gdp': '400'},
    ]
    expected = [
        ('Germany', 300.00),
        ('USA', 200.00)
    ]

    report = AverageGDPReport()
    result = report.generate(rows)

    assert result == expected

def test_get_report_success():
    report_name = 'average-gdp'

    report = get_report(report_name)
    assert isinstance(report, AverageGDPReport)


def test_get_report_failure_unknown_name():
    report_name = 'new-report'

    with pytest.raises(ValueError):
        report = get_report(report_name)

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
        
