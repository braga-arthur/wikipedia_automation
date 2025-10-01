# Wikipedia Automation

This project searches for a person on Wikipedia and returns the value of the **Alma mater** field from the infobox, if it exists.

---

## Requirements

* **Python 3.9+**
* **Selenium**
* **webdriver-manager**
* **Google Chrome**

---

## Installation

1. Extract the project and open the `wikipedia_automation` folder

2. Create a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate  # Mac/Linux
.venv\Scripts\activate     # Windows
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

---

## How to Run

```bash
python -m src.runner
```

## Project Structure / Design Pattern

The project follows the **Page Object Model (POM)** pattern:

* Each web page has a class containing the page elements and actions
* The `BasePage` class holds the driver and can be extended in the future for additional methods
* `runner.py` is the main execution script

## Viewing Logs

```bash
cat logs/run.log
```
