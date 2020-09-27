import datetime
import os
import sys
import pandas as pd
import pytest
import yfinance

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from service import SearchService
from model import LostFound


@pytest.fixture
def search_service():
    ticker = LostFound(yfinance)
    return SearchService(ticker)


def test_get_maxprofit_incline(search_service):
    numdays = 10
    base = datetime.datetime.today()
    date_list = [base - datetime.timedelta(days=x) for x in range(numdays)][::-1]
    price_list = [x for x in range(10)]
    df = pd.DataFrame({'Date': date_list, 'High':price_list, 'Low':price_list,
                       'Close': price_list})
    assert  search_service.get_maxprofit_highlow('AAPL', df) == (str(date_list[0].date()),str(date_list[9].date()),9)

def test_get_maxprofit_decline(search_service):
    numdays = 10
    base = datetime.datetime.today()
    date_list = [base - datetime.timedelta(days=x) for x in range(numdays)][::-1]
    price_list = [x for x in range(10,0,-1)]
    df = pd.DataFrame({'Date': date_list, 'High':price_list, 'Low':price_list,
                       'Close': price_list})
    assert  search_service.get_maxprofit_highlow('AAPL', df) == (str(date_list[0].date()),str(date_list[1].date()),-1)

def test_get_maxprofit_camel(search_service):
    numdays = 10
    base = datetime.datetime.today()
    date_list = [base - datetime.timedelta(days=x) for x in range(numdays)][::-1]
    price_list = [1,2,7,5,9,8,6,4,3,2]
    df = pd.DataFrame({'Date': date_list, 'High':price_list, 'Low':price_list,
                       'Close': price_list})
    assert  search_service.get_maxprofit_highlow('AAPL', df) == (str(date_list[0].date()),str(date_list[4].date()),8)

def test_get_maxprofit_concavecamel(search_service):
    numdays = 10
    base = datetime.datetime.today()
    date_list = [base - datetime.timedelta(days=x) for x in range(numdays)][::-1]
    price_list = [9,8,5,2,5,2,4,6,7,8]
    df = pd.DataFrame({'Date': date_list, 'High':price_list, 'Low':price_list,
                       'Close': price_list})
    assert  search_service.get_maxprofit_highlow('AAPL', df) == (str(date_list[3].date()),str(date_list[9].date()),6)