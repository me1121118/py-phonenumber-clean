# py-phonenumber-clean

[![PyPI version](https://img.shields.io/badge/pypi-v0.1.0-blue.svg)](https://pypi.org/project/py-phonenumber-clean/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)

Zero-dependency international phone number cleaner, E.164 normalizer, and country calling code extractor in pure Python.

---

## 🚀 Features

- 🪶 **Zero Dependencies**: Pure Python regex and string manipulation.
- 📞 **E.164 Format**: Standardizes numbers like `+1 (555) 123-4567` -> `+15551234567`.
- 🌍 **Calling Code Extraction**: Identifies country prefix (`+66`, `+1`, `+44`, `+81`).

---

## 📦 Installation

```bash
pip install py-phonenumber-clean
```

---

## 🛠️ Quickstart

```python
from py_phonenumber_clean import clean_phone, is_valid_e164

print(clean_phone("+1 (555) 019-2834"))  # +15550192834
print(clean_phone("081-234-5678", default_country_code="+66"))  # +66812345678
print(is_valid_e164("+15550192834"))    # True
```

---

## ☕ Support My Studies / Buy Me a Coffee

I am an independent developer and student building open-source developer productivity tools. If this phone sanitizer cleaned up your SMS deliverability, please consider supporting my studies:

- ☕ **Buy Me a Coffee:** [ko-fi.com/me1121118](https://ko-fi.com/)
- ⭐ **Star this repository** on GitHub!

---

## 📄 License

MIT License. See [LICENSE](LICENSE) for details.
