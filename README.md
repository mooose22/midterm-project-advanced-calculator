Advanced Calculator Application
Project Description

This project is an advanced Python calculator application built with object-oriented design principles and multiple software design patterns. The calculator supports various arithmetic operations, maintains calculation history, allows undo and redo actions, logs calculations, and automatically saves history to a CSV file.

The application includes a command-line interface (REPL) where users can perform calculations interactively.

Design patterns implemented in this project include:

Factory Pattern – used to create arithmetic operations dynamically

Memento Pattern – used to support undo and redo functionality

Observer Pattern – used for logging and auto-saving calculations

The project also includes comprehensive unit testing and a CI/CD pipeline using GitHub Actions.

Features
Arithmetic Operations

The calculator supports the following operations:

add

subtract

multiply

divide

power

root

modulus

integer division

percentage

absolute difference

History Management

The calculator stores all calculations and supports:

viewing calculation history

clearing history

undo

redo

Logging

All calculations are logged using Python's logging module.

Automatic History Saving

Calculation history is automatically saved to a CSV file using pandas.

Configuration Management

Application configuration is handled through environment variables using .env.

Command Line Interface (REPL)

Users can interact with the calculator through commands such as:

add 5 3
multiply 4 6
history
undo
redo
save
load
help
exit
Project Structure
project_root/
│
├── app/
│   ├── calculator.py
│   ├── calculator_config.py
│   ├── calculator_memento.py
│   ├── calculation.py
│   ├── exceptions.py
│   ├── history.py
│   ├── input_validators.py
│   ├── logger.py
│   └── operations.py
│
├── tests/
│   ├── test_calculator.py
│   ├── test_calculation.py
│   ├── test_operations.py
│   ├── test_history.py
│   └── test_logger.py
│
├── .github/workflows/
│   └── python-app.yml
│
├── .env
├── requirements.txt
└── README.md
Installation

Clone the repository:

git clone <repository_url>
cd midterm-project-python-for-web-api-development

Create a virtual environment:

python3 -m venv venv
source venv/bin/activate

Install dependencies:

pip install -r requirements.txt
Configuration Setup

Create a .env file in the project root with the following variables:

CALCULATOR_LOG_DIR=logs
CALCULATOR_HISTORY_DIR=history
CALCULATOR_LOG_FILE=logs/calculator.log
CALCULATOR_HISTORY_FILE=history/calculations.csv
CALCULATOR_MAX_HISTORY_SIZE=100
CALCULATOR_AUTO_SAVE=true
CALCULATOR_PRECISION=2
CALCULATOR_MAX_INPUT_VALUE=1000000
CALCULATOR_DEFAULT_ENCODING=utf-8

These values configure logging, history storage, calculation precision, and input limits.

Running the Calculator

Start the interactive calculator with:

python -m app.calculator

Example session:

>>> add 2 3
Result: 5

>>> power 2 4
Result: 16

>>> history
1. add(2, 3) = 5
2. power(2, 4) = 16

>>> undo
Undo successful.

>>> redo
Redo successful.

>>> exit
Goodbye.
Running Tests

Run the full test suite with:

pytest

Run tests with coverage:

pytest --cov=app --cov-report=term-missing

The project maintains greater than 90% test coverage.

Continuous Integration

This project uses GitHub Actions for automated testing.

The workflow automatically:

Checks out the repository

Installs dependencies

Runs all tests

Verifies that test coverage remains above 90%

The workflow runs on every push or pull request to the main branch.

Technologies Used

Python

pytest

pytest-cov

pandas

python-dotenv

GitHub Actions

Author

Mostafa Moawad