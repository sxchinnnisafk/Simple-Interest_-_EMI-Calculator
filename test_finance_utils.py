# test_finance_utils.py
import pytest
from finance_utils import simple_interest, emi, total_amount, compound_interest


def test_simple_interest_standard():
    assert simple_interest(10000, 5, 2) == 1000.0
    assert simple_interest(50000, 8.5, 3) == 12750.0


def test_simple_interest_zero_rate():
    assert simple_interest(25000, 0, 4) == 0.0


def test_emi_standard():
    assert emi(100000, 12, 12) == 8884.88
    assert emi(500000, 10, 60) == 10623.52


def test_emi_zero_interest():
    assert emi(12000, 0, 12) == 1000.0


def test_total_amount_standard():
    assert total_amount(10000, 5, 2) == 11000.0
    assert total_amount(50000, 8.5, 3) == 62750.0


def test_compound_interest_annual_and_quarterly():
    assert compound_interest(10000, 10, 2) == 2100.0
    assert compound_interest(10000, 10, 2, freq=4) == 2184.03


def test_invalid_inputs_simple_interest():
    with pytest.raises(ValueError):
        simple_interest(-5000, 5, 2)
    with pytest.raises(ValueError):
        simple_interest(10000, -2, 2)


def test_invalid_inputs_emi_and_compound():
    with pytest.raises(ValueError):
        emi(100000, 10, 0)
    with pytest.raises(ValueError):
        compound_interest(10000, 10, 2, freq=0)
