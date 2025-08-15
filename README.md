# Power calculator: A Streamlit App
This mini project features a simple web application built with streamlit that calculates the power of a number. The app takes a base number and an exponent as input and displays the result.

## Features
* **Interactive UI:** The application provides a user-friendly interface using Streamlit's widgets to accept numerical inputs for the base and exponent.
* **Power Calculator:**  It calculates the result of the base number raised to the power of the exponent (e.g., base<sup>exponent</sup>).
* **Automated Testing:** The project includes a testing suite using `pytest` to ensure the core power calculation logic is correct. Tests cover various scenarios, including positive, negative, and zero inputs, as well as type-related errors.
* **Continuous Integration (CI):** A GitHub Actions workflow is configured to automatically run the `pytest` tests on every push and pull request to the main branch, ensuring code quality and preventing regressions.

## Project Structure:
* `app.py`: Contains the source code for the Streamlit web application.
* `_test.py`: Holds the unit tests written with `pytest` for the power calculation functions.
* `ci.yaml`: Defines the CI workflow for GitHub Actions, which includes steps to set up the environment, install dependencies, and run the tests.