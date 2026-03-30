## Running the tests

### 1. Install Python
Make sure Python 3.10+ is installed on your machine.
https://www.python.org/downloads/

You can verify it with:

```bash
python --version
```

### 2. Install requirments
Run command
```bash
pip install -r requirements.txt
```

### 3. Run tests
Set your location to main folder. More details under link
https://docs.pytest.org/en/stable/getting-started.html

To run Selenium Test execute command
```bash
python -m pytest Automation/Selenium/test_single_bet.py
```

To run API Test exectue command
```bash
python -m pytest Automation/API/test_business_rules.py
```