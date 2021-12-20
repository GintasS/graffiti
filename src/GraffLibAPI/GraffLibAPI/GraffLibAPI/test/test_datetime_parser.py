import pytest
import GraffLibAPI.utils.datetime_parser as DatetimeParseClass
import datetime

def test_parse_date():
    test_date = "2009:10:5"
    result_date = DatetimeParseClass.parse_date(test_date)
    assert result_date == datetime.datetime(2009, 10, 5)

