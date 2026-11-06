# Python Hybrid Test Framework

A comprehensive test automation framework combining Playwright (UI), Requests (API), and LLM validation capabilities.

## Features
- UI Testing with **Playwright**
- API Testing validation
- LLM Output Validation
- **Allure** Reporting integration
- **Pytest** runner with async support

## Prerequisites
- [uv](https://github.com/astral-sh/uv) (Fast Python package installer and resolver)
- Python 3.12+

## Setup

### 1. Initialize Environment
Install dependencies and create virtual environment using `uv`:
```bash
uv sync
```

### 2. Install Playwright Browsers
```bash
uv run playwright install chromium
```

## Running Tests

### Run All Tests
```bash
uv run pytest
```

### Run Specific Tests
```bash
# Run web tests
uv run pytest tests/web

# Run specific file
uv run pytest tests/web/test_sample.py
```

### Run with Headed Mode (Visible Browser)
```bash
uv run pytest --headed
```

## Allure Reports

### Generate and View Reports
```bash
# Run tests with allure results
uv run pytest --alluredir=reports/allure-results

# Generate HTML report
allure generate reports/allure-results -o reports/allure-report --clean --single-file

# Serve report
allure serve reports/allure-results
```

## Project Structure
- `config/` - Configuration settings
- `framework/` - Core framework utilities and wrappers
- `tests/`
  - `web/` - Playwright UI tests
  - `api/` - API tests
  - `llm/` - LLM validation tests
- `reports/` - Test execution reports
- `conftest.py` - Pytest fixtures and hooks
- `pytest.ini` - Global pytest configuration