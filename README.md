$ python3 -m venv venv
$ source venv/bin/activate
$ pip -V
$ pip install -r requirements.txt

# Selenium Automation Framework (POM)

This is a **Selenium Web Automation Framework** using **Page Object Model (POM)**.  
It automates UI testing for [SauceDemo](https://www.saucedemo.com/) and includes tests for login, sorting, cart functionality, checkout, and logout.

---

## Installation & Setup

### 1️⃣ **Clone the Repository**
```sh
git clone https://github.com/paularpi66/newroztech-selenium-assignment.git
cd newroztech-selenium-assignment
```

### Set Up a Virtual Environment (venv)

```bash
python3 -m venv venv
source venv/bin/activate  # macOS/Linux
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

## Requirements

- Python 3.8+
- Google Chrome (or Firefox)
- ChromeDriver (or GeckoDriver for Firefox)
- Selenium 4.12+
- pytest for running test cases
- webdriver-manager for handling WebDrivers

All dependencies are listed in `requirements.txt` and will be installed using `pip install -r requirements.txt`.

## Environment Setup

### Verify Python Installation

```sh
python3 --version
```

### Install WebDriver

Install ChromeDriver using WebDriver Manager:

```bash
brew install chromedriver
```

> Troubleshooting
If you encounter an error, you can try: 
Using the error messages to install the appropriate versions 
Going to System Preferences -> Security & Privacy and clicking the "open this anyway" button 

## Check WebDriver Installation

```bash
chromedriver --version  # For Chrome
```

## Project Structure

```
selenium_project/
│─── pages/                # Page Classes (POM)
│    ├── login_page.py
│    ├── inventory_page.py
│    ├── cart_page.py
│    ├── checkout_page.py
│    ├── logout_page.py
│─── tests/                # Test Scripts
│    ├── test_login.py
│    ├── test_cart.py
│    ├── test_checkout.py
│    ├── test_logout.py
│    ├── test_sorting.py
│─── utils/                # Utility Functions
│    ├── driver_setup.py
│    ├── common.py
│─── requirements.txt      # Dependencies
│─── README.md             # Project Info
```

## Run the Tests

### Run All Tests Using pytest

```sh
pytest tests/
```

### Run a Specific Test File

```bash
pytest tests/test_login.py
```

### Run Tests with Detailed Output

```bash
pytest -v
```

## Key Features

- Page Object Model (POM) for better test structure.
- Reusable Components for login, cart, checkout, and logout.
- WebDriver Manager for easy WebDriver handling.
- `pytest` Integration for test execution and reporting.
