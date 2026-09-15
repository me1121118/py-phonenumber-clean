import pytest
from py_phonenumber_clean import clean_phone, is_valid_e164

def test_clean_phone():
    assert clean_phone("+1 (555) 123-4567") == "+15551234567"
    assert clean_phone("081-234-5678", default_country_code="+66") == "+66812345678"
    assert clean_phone("+66 81 234 5678") == "+66812345678"

def test_is_valid_e164():
    assert is_valid_e164("+15551234567") is True
    assert is_valid_e164("+66812345678") is True
    assert is_valid_e164("0812345678") is False
    assert is_valid_e164("+0123") is False
