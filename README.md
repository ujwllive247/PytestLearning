# 🧪 Pytest Learning Repository

This repository is a hands-on learning space for mastering [Pytest](https://docs.pytest.org/) — a powerful Python testing framework. It covers a wide range of real-world testing concepts using well-organized examples.

---

## 📁 Folder Overview

| Folder Name             | Description                                      |
|-------------------------|--------------------------------------------------|
| `Assertions`            | Covers soft and hard assertions                 |
| `Custom_Markers`        | Shows how to define and use custom markers      |
| `Fixture`               | Demonstrates basic usage of fixtures            |
| `FixtureScopes`         | Explores fixture scopes (`function`, `class`, etc.) |
| `Fixture_in_conftestFile` | Shares fixture reuse via `conftest.py`        |
| `Flags`                 | Uses CLI flags and command-line options         |
| `GroupingTest`          | Groups related tests for selective execution    |
| `HookFunction`          | Demonstrates usage of Pytest hooks              |
| `Markers`               | Covers marker-based test filtering              |
| `Parametrization`       | Shows how to run tests with multiple data sets  |
| `ParellelExecution`     | Implements parallel testing using plugins       |
| `Pytest`                | Contains basic examples and getting started     |
| `SeleniumTest`          | Shows Pytest usage with Selenium                |
| `SkipTest`              | Demonstrates skipping or conditionally running tests |
| `Soft_Hard_Assertion`   | Explores assertion behavior differences         |
| `samplePackage` / `samplepackage` | Examples with different naming and structuring styles |

---

## 🚀 How to Run Tests

Install dependencies:
```bash
pip install -r requirements.txt

##Run all test.......
pytest

## Run specific file ......
pytest FolderName/test_example.py

##Run specific groups
pytest -m "smoke"

🛠 Tools & Config
✅ Python & Pytest

✅ Custom markers via pytest.ini

✅ Optional plugin support (e.g., pytest-xdist for parallel execution)

