# PyTest
[![Maintainability](https://api.codeclimate.com/v1/badges/358d93aab78b3ab2c261/maintainability)](https://codeclimate.com/github/rindibudiaramdhan/pytest/maintainability) [![Test Coverage](https://api.codeclimate.com/v1/badges/358d93aab78b3ab2c261/test_coverage)](https://codeclimate.com/github/rindibudiaramdhan/pytest/test_coverage)

Pytest is a popular testing framework for Python.
## Stacks
### `Python`
pytest is a Python package and requires Python to be installed on your system. You can download Python from the official Python website (https://www.python.org/).
### `pip`
pip is the default package installer for Python. It is used to install and manage packages, including pytest. If you have Python installed, you should have pip installed as well. You can check if pip is installed by running the following command in a terminal:
```css
pip --version
```
If pip is not installed, you can download and install it from the official pip website (https://pip.pypa.io/en/stable/installing/).
### `pytest`
Finally, you will need to install the pytest package itself. You can install pytest using pip by running the following command in a terminal:
```
pip install pytest
```
This will install the latest version of pytest and any dependencies it requires.
Once you have installed these three requirements, you should be able to start using pytest to write and run tests for your Python code.

## How to Use
Here are the general steps to use pytest:

1. Install pytest: You can install pytest using pip, the Python package installer. Open a terminal and run the following command:
```
pip install pytest
```

2. Create a test file: Create a file named `test_<module>.py` in your project directory. This file will contain your test cases.

3. Write test cases: Define your test functions with names starting with `test_`. You can use assertions to check if the code under test is behaving correctly. Here's an example test case:
```python
def test_addition():
    assert 2 + 2 == 4
```

4. Run tests: Open a terminal, navigate to your project directory, and run the following command:

```
pytest
```
This will discover and run all test cases in your project. You should see output similar to the following:
```javascript
============================= test session starts =============================
platform linux -- Python 3.8.5, pytest-6.2.3, py-1.10.0, pluggy-0.13.1
rootdir: /path/to/your/project
collected 1 item                                                               

test_example.py .                                                      [100%]

============================== 1 passed in 0.01s ==============================
```
The output shows that one test passed in 0.01 seconds.

5. Write more test cases: Add more test functions to your test file to cover more code and edge cases.

6. Repeat step 4: Every time you modify your code, run pytest to ensure that your changes didn't break any existing functionality.

That's it! You should now be able to use pytest to write and run tests for your Python code.

## How to report result beautifully
By default, pytest provides a simple and easy-to-read report of the test results in the console. However, if you want to generate more beautiful and informative reports, you can use plugins or third-party tools that integrate with pytest.

Here are some popular plugins and tools that can help you generate beautiful and informative test reports:
### `pytest-html`
This plugin generates an HTML report of the test results, which includes details about each test, including its status, duration, and any error messages. You can install the plugin using pip:
```css
pip install pytest-html
```
To generate an HTML report, run pytest with the --html option and specify the output file:
```css
pytest --html=report.html
```
This will generate an HTML report named report.html in the current directory.

### `pytest-cov`
This plugin generates a coverage report that shows which lines of code were executed during the test run. You can install the plugin using pip:
```
pip install pytest-cov
```
To generate a coverage report, run pytest with the `--cov` option and specify the name of the module you want to test coverage for:
```css
pytest --cov=mymodule
```
This will generate a coverage report that shows the percentage of code coverage for each file in the `mymodule` package.
### `Pytest-bdd`
This plugin provides support for behavior-driven development (BDD) testing using the Gherkin syntax. It generates easy-to-read reports that show how well your code satisfies the requirements specified in your feature files. You can install the plugin using pip:
```
pip install pytest-bdd
```
To generate a BDD report, run pytest with the --cucumberjson option and specify the output file:
```css
pytest --cucumberjson=report.json
```
This will generate a report in the JSON format that can be easily consumed by other tools.

There are many other plugins and tools available that can help you generate beautiful and informative test reports. You can search for them on the PyPI website or by using the pytest documentation.

## Troubleshooting
TBD