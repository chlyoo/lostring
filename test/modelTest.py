import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
from pandas._testing import assert_frame_equal
import yfinance
import datetime
from model import LostFound


@pytest.fixture
def ticker_data():
    return LostFound(yfinance)


def test_period(ticker_data):
    ticker_data.update_period()
    period1, period2 = ticker_data.get_period()
    p1 = datetime.datetime.strptime(period1, '%Y-%m-%d')
    p2 = datetime.datetime.strptime(period2, '%Y-%m-%d')
    assert (p2 - p1) == datetime.timedelta(180)


def test_gethistory(ticker_data):
    ticker_data.set_ticker('GOOG')
    ticker = ticker_data.get_ticker()
    assert_frame_equal(ticker.history(period='1d'), yfinance.Ticker('GOOG').history(period='1d'))


def test_is_yfinance(ticker_data):
    assert ticker_data.is_yfinance(yfinance) == True
