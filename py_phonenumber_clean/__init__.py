import re
from typing import Optional

E164_REGEX = re.compile(r"^\+[1-9]\d{1,14}$")

def clean_phone(raw_phone: str, default_country_code: Optional[str] = None) -> str:
    """Clean and normalize phone number into standard E.164 representation."""
    if not raw_phone:
        return ""
    s = raw_phone.strip()
    has_plus = s.startswith("+")

    # Keep only digits
    digits = re.sub(r"\D", "", s)
    if not digits:
        return ""

    if has_plus:
        return f"+{digits}"

    if default_country_code:
        code_digits = re.sub(r"\D", "", default_country_code)
        # Strip leading 0 in domestic national number
        if digits.startswith("0"):
            digits = digits[1:]
        return f"+{code_digits}{digits}"

    return digits

def is_valid_e164(phone: str) -> bool:
    """Check if string matches standard E.164 phone number pattern."""
    return bool(E164_REGEX.match(phone.strip()))
